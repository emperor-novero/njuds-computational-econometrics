"""Statewide Assessment Regressivity & Uniformity Index Engine.

Computational evaluation of property tax equity based on:
- IAAO Standard on Ratio Studies (International Association of Assessing Officers)
- New Jersey Division of Taxation SR1A ratio methodologies
- Price-Related Differential (PRD), Coefficient of Dispersion (COD),
  Coefficient of Variation (COV), and Assessment Gini Coefficient (G_tax).

Quantifies vertical regressivity (whether lower-value properties carry higher effective
assessment ratios than luxury assets) and horizontal inequity (dispersion within classes).
"""

from dataclasses import dataclass
import math
from typing import Dict, List, Optional, Tuple


@dataclass
class RatioStudyDiagnostics:
    """Comprehensive statistical metrics for a municipal assessment ratio study."""
    sample_size: int
    mean_ratio: float
    median_ratio: float
    weighted_mean_ratio: float
    prd: float  # Price-Related Differential
    cod: float  # Coefficient of Dispersion (%)
    cov: float  # Coefficient of Variation (%)
    tax_gini: float  # Assessment Regressivity Gini Coefficient
    is_regressive: bool
    is_progressive: bool
    is_uniform: bool
    iaao_prd_compliant: bool
    iaao_cod_compliant: bool
    verdict: str


class NJRegressivityEngine:
    """Statistical engine for spatial assessment regressivity and uniformity."""

    IAAO_PRD_LOWER: float = 0.98
    IAAO_PRD_UPPER: float = 1.03
    IAAO_COD_RESIDENTIAL_MAX: float = 15.0  # Max acceptable COD for residential (15%)

    @classmethod
    def calculate_ratios(
        cls,
        assessments: List[float],
        sales_prices: List[float]
    ) -> List[float]:
        """Calculates individual assessment-to-sales ratios (R_i = A_i / S_i)."""
        if len(assessments) != len(sales_prices):
            raise ValueError("Assessments and sales prices arrays must have equal length.")
        
        ratios = []
        for a, s in zip(assessments, sales_prices):
            if s <= 0:
                raise ValueError("Sales price must be strictly positive.")
            ratios.append(a / s)
        return ratios

    @classmethod
    def calculate_prd(
        cls,
        assessments: List[float],
        sales_prices: List[float]
    ) -> float:
        """Calculates Price-Related Differential (PRD).
        
        Formula:
            PRD = Mean Ratio / Weighted Mean Ratio
            Where Weighted Mean = Sum(Assessments) / Sum(Sales Prices)
            
        Interpretation:
            PRD > 1.03: Vertical Regressivity (lower-value homes over-assessed)
            PRD < 0.98: Vertical Progressivity (higher-value homes over-assessed)
            0.98 <= PRD <= 1.03: Acceptable equity zone
        """
        ratios = cls.calculate_ratios(assessments, sales_prices)
        n = len(ratios)
        if n == 0:
            return 0.0

        mean_ratio = sum(ratios) / n
        weighted_mean = sum(assessments) / sum(sales_prices)

        if weighted_mean == 0:
            return 0.0

        return round(mean_ratio / weighted_mean, 4)

    @classmethod
    def calculate_cod(
        cls,
        assessments: List[float],
        sales_prices: List[float]
    ) -> float:
        """Calculates Coefficient of Dispersion (COD) as a percentage.
        
        Formula:
            COD = (100 / Median Ratio) * (1 / n) * Sum(|R_i - Median Ratio|)
            
        Interpretation:
            Measures horizontal equity / uniformity.
            Residential COD <= 15.0% is acceptable by IAAO standards.
            COD > 20.0% indicates systemic assessment inequity and random dispersion.
        """
        ratios = cls.calculate_ratios(assessments, sales_prices)
        n = len(ratios)
        if n == 0:
            return 0.0

        sorted_ratios = sorted(ratios)
        mid = n // 2
        if n % 2 == 0:
            median_ratio = (sorted_ratios[mid - 1] + sorted_ratios[mid]) / 2.0
        else:
            median_ratio = sorted_ratios[mid]

        if median_ratio == 0:
            return 0.0

        abs_dev_sum = sum(abs(r - median_ratio) for r in ratios)
        cod = (100.0 / median_ratio) * (abs_dev_sum / n)
        return round(cod, 2)

    @classmethod
    def calculate_tax_gini(
        cls,
        assessments: List[float],
        sales_prices: List[float]
    ) -> float:
        """Calculates Assessment Gini Coefficient (G_tax).
        
        Measures the inequality of assessment ratios across property values.
        Sorts pairs by sales price (market value) and calculates the Lorenz curve area
        for cumulative assessment burden vs cumulative true market value.
        
        Returns:
            G_tax in range [0.0, 1.0]. Values above 0.15 indicate substantial disparity.
        """
        n = len(assessments)
        if n < 2:
            return 0.0

        # Pair and sort by market value (sales price) ascending
        pairs = sorted(zip(sales_prices, assessments), key=lambda x: x[0])
        
        total_market = sum(p[0] for p in pairs)
        total_assess = sum(p[1] for p in pairs)

        if total_market == 0 or total_assess == 0:
            return 0.0

        # Compute Gini using standard trapezoidal integration
        cum_market = 0.0
        cum_assess = 0.0
        area_under_lorenz = 0.0

        for s, a in pairs:
            prev_m = cum_market / total_market
            prev_a = cum_assess / total_assess
            cum_market += s
            cum_assess += a
            curr_m = cum_market / total_market
            curr_a = cum_assess / total_assess

            # Trapezoid area
            width = curr_m - prev_m
            height = (prev_a + curr_a) / 2.0
            area_under_lorenz += width * height

        gini = 1.0 - 2.0 * area_under_lorenz
        return round(abs(gini), 4)

    @classmethod
    def evaluate_ratio_study(
        cls,
        assessments: List[float],
        sales_prices: List[float]
    ) -> RatioStudyDiagnostics:
        """Executes full diagnostic ratio study audit conforming to IAAO standards.
        
        Returns:
            RatioStudyDiagnostics with PRD, COD, COV, G_tax, and compliance verdict.
        """
        ratios = cls.calculate_ratios(assessments, sales_prices)
        n = len(ratios)
        if n == 0:
            raise ValueError("Cannot evaluate empty ratio dataset.")

        mean_r = sum(ratios) / n
        
        sorted_r = sorted(ratios)
        mid = n // 2
        median_r = (sorted_r[mid - 1] + sorted_r[mid]) / 2.0 if n % 2 == 0 else sorted_r[mid]
        
        weighted_mean_r = sum(assessments) / sum(sales_prices)
        prd = round(mean_r / weighted_mean_r, 4) if weighted_mean_r > 0 else 0.0
        
        # COD
        abs_dev_sum = sum(abs(r - median_r) for r in ratios)
        cod = round((100.0 / median_r) * (abs_dev_sum / n), 2) if median_r > 0 else 0.0

        # COV (Coefficient of Variation)
        variance = sum((r - mean_r) ** 2 for r in ratios) / (n - 1) if n > 1 else 0.0
        std_dev = math.sqrt(variance)
        cov = round((std_dev / mean_r) * 100.0, 2) if mean_r > 0 else 0.0

        # Gini
        tax_gini = cls.calculate_tax_gini(assessments, sales_prices)

        is_regressive = prd > cls.IAAO_PRD_UPPER
        is_progressive = prd < cls.IAAO_PRD_LOWER
        is_uniform = cod <= cls.IAAO_COD_RESIDENTIAL_MAX
        iaao_prd_compliant = not is_regressive and not is_progressive
        iaao_cod_compliant = is_uniform

        if is_regressive and not is_uniform:
            verdict = "SEVERE NON-COMPLIANCE: Statistically significant vertical regressivity and high horizontal dispersion."
        elif is_regressive:
            verdict = "VERTICAL REGRESSIVITY: Lower-value properties bear higher tax ratio burden (PRD > 1.03)."
        elif not is_uniform:
            verdict = "HORIZONTAL INEQUITY: High dispersion of assessments within same class (COD > 15%)."
        else:
            verdict = "IAAO COMPLIANT: Equalized and uniform municipal assessment roll."

        return RatioStudyDiagnostics(
            sample_size=n,
            mean_ratio=round(mean_r, 4),
            median_ratio=round(median_r, 4),
            weighted_mean_ratio=round(weighted_mean_r, 4),
            prd=prd,
            cod=cod,
            cov=cov,
            tax_gini=tax_gini,
            is_regressive=is_regressive,
            is_progressive=is_progressive,
            is_uniform=is_uniform,
            iaao_prd_compliant=iaao_prd_compliant,
            iaao_cod_compliant=iaao_cod_compliant,
            verdict=verdict
        )
