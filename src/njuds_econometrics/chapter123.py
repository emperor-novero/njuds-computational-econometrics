"""New Jersey Statutory Equalization and Chapter 123 Engine.

Implements statutory property tax assessment corridor modeling and added assessment
mechanics governed by Chapter 123 of the Laws of 1973 (N.J.S.A. 54:51A-6) and
the Added Assessment Act (N.J.S.A. 54:4-63.1 et seq.).
"""

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class ConformanceResult:
    """Encapsulates the statutory Chapter 123 evaluation result.

    Attributes:
        assessed_value: The municipal taxable assessed value on the MOD-IV tax roll.
        true_value: The certified market value or arms-length transaction price.
        directors_ratio: The certified Director's Ratio published by the NJ Division of Taxation.
        assessment_ratio: The implied assessment ratio (assessed_value / true_value).
        lower_limit: The statutory lower corridor threshold (0.85 * Director's Ratio).
        upper_limit: The statutory upper corridor threshold (1.15 * Director's Ratio).
        is_conforming: True if the assessment ratio falls within [lower_limit, upper_limit].
        status: Categorical status ("CONFORMING", "OVER_ASSESSED", or "UNDER_ASSESSED").
        tax_reduction_eligible: True if the taxpayer is statutorily entitled to a tax reduction.
        revised_assessment: The statutory equalized assessment if an appeal succeeds,
            otherwise the existing assessed value.
        explanation: Detailed statutory rationale citing N.J.S.A. 54:51A-6.
    """

    assessed_value: float
    true_value: float
    directors_ratio: float
    assessment_ratio: float
    lower_limit: float
    upper_limit: float
    is_conforming: bool
    status: str
    tax_reduction_eligible: bool
    revised_assessment: float
    explanation: str


class Chapter123Engine:
    """Engine for New Jersey Chapter 123 equalization corridor and added assessment calculations."""

    @staticmethod
    def calculate_corridor(directors_ratio: float) -> Tuple[float, float]:
        """Calculates the statutory Chapter 123 tolerance corridor.

        Under N.J.S.A. 54:51A-6:
            Lower Corridor Limit = 0.85 * Director's Ratio
            Upper Corridor Limit = 1.15 * Director's Ratio

        Args:
            directors_ratio: The municipal Director's Ratio (either as a decimal [0, 1]
                or percentage [0, 100]).

        Returns:
            Tuple[float, float]: (lower_limit, upper_limit) matching the scale of the input ratio.

        Raises:
            ValueError: If directors_ratio is non-positive.
        """
        if directors_ratio <= 0:
            raise ValueError(f"Director's Ratio must be strictly positive, got {directors_ratio}")

        lower_limit = 0.85 * directors_ratio
        upper_limit = 1.15 * directors_ratio
        return lower_limit, upper_limit

    @classmethod
    def evaluate_conformance(
        cls,
        assessed_value: float,
        true_value: float,
        directors_ratio: float,
    ) -> ConformanceResult:
        """Evaluates whether an assessment conforms to the Chapter 123 statutory corridor.

        Under N.J.S.A. 54:51A-6:
        - If assessment_ratio > 1.15 * Director's Ratio: The property is OVER-ASSESSED.
          The Tax Court or County Board of Taxation will reduce the assessment to:
              revised_assessment = true_value * Director's Ratio
        - If 0.85 * Director's Ratio <= assessment_ratio <= 1.15 * Director's Ratio:
          The assessment is legally CONFORMING. No tax appeal reduction is permitted by law.
        - If assessment_ratio < 0.85 * Director's Ratio:
          The property is UNDER-ASSESSED. Tax appeal is barred; the property is shielded
          against spot assessment under the Van Decker doctrine (N.J. Const. art. VIII).

        Args:
            assessed_value: Municipal taxable assessment in dollars (>= 0).
            true_value: True market value or arm's-length acquisition price in dollars (> 0).
            directors_ratio: Municipal Director's Ratio (decimal or percentage).

        Returns:
            ConformanceResult containing all corridor parameters, status, and legal remedies.

        Raises:
            ValueError: If true_value <= 0, assessed_value < 0, or directors_ratio <= 0.
        """
        if true_value <= 0:
            raise ValueError(f"true_value must be strictly positive, got {true_value}")
        if assessed_value < 0:
            raise ValueError(f"assessed_value must be non-negative, got {assessed_value}")
        if directors_ratio <= 0:
            raise ValueError(f"directors_ratio must be strictly positive, got {directors_ratio}")

        # Normalize director's ratio to decimal [0, 1]
        norm_ratio = directors_ratio / 100.0 if directors_ratio > 1.0 else directors_ratio
        assessment_ratio = assessed_value / true_value

        lower_limit, upper_limit = cls.calculate_corridor(norm_ratio)

        if assessment_ratio > upper_limit:
            status = "OVER_ASSESSED"
            is_conforming = False
            tax_reduction_eligible = True
            revised_assessment = true_value * norm_ratio
            explanation = (
                f"Assessment ratio of {assessment_ratio:.4f} ({assessment_ratio * 100:.2f}%) "
                f"exceeds the upper corridor limit of {upper_limit:.4f} ({upper_limit * 100:.2f}%). "
                f"Taxpayer has a statutory right under N.J.S.A. 54:51A-6 to reduce the assessment "
                f"to the Director's Ratio benchmark (${revised_assessment:,.2f})."
            )
        elif assessment_ratio < lower_limit:
            status = "UNDER_ASSESSED"
            is_conforming = False
            tax_reduction_eligible = False
            revised_assessment = assessed_value
            explanation = (
                f"Assessment ratio of {assessment_ratio:.4f} ({assessment_ratio * 100:.2f}%) "
                f"is below the lower corridor limit of {lower_limit:.4f} ({lower_limit * 100:.2f}%). "
                f"The property is legally under-assessed. Tax appeal is strictly counter-indicated "
                f"(risks municipal counter-claim under F.M.C. Stores Co. v. Morris Plains). "
                f"Valuation is shielded against spot reassessment under the Van Decker doctrine."
            )
        else:
            status = "CONFORMING"
            is_conforming = True
            tax_reduction_eligible = False
            revised_assessment = assessed_value
            explanation = (
                f"Assessment ratio of {assessment_ratio:.4f} ({assessment_ratio * 100:.2f}%) "
                f"falls squarely inside the statutory Chapter 123 corridor "
                f"[{lower_limit:.4f}, {upper_limit:.4f}] ({lower_limit * 100:.2f}% to {upper_limit * 100:.2f}%). "
                f"Under N.J.S.A. 54:51A-6, the assessment is statutorily presumed correct; "
                f"no tax reduction may be granted."
            )

        return ConformanceResult(
            assessed_value=assessed_value,
            true_value=true_value,
            directors_ratio=norm_ratio,
            assessment_ratio=assessment_ratio,
            lower_limit=lower_limit,
            upper_limit=upper_limit,
            is_conforming=is_conforming,
            status=status,
            tax_reduction_eligible=tax_reduction_eligible,
            revised_assessment=revised_assessment,
            explanation=explanation,
        )

    @staticmethod
    def calculate_added_assessment(
        base_assessment: float,
        capex_amount: float,
        equalization_ratio: float,
    ) -> float:
        """Calculates post-improvement assessment incorporating mandatory Added Assessment.

        Under N.J.S.A. 54:4-63.1 et seq. (The Added Assessment Act):
        Capital expenditures triggering municipal building permits cause a statutory
        reassessment equalized by the municipality's equalization ratio upon issuance
        of a Certificate of Occupancy:
            Added Assessment = CapEx Amount * Equalization Ratio
            Total Post-Improvement Assessment = Base Assessment + Added Assessment

        Args:
            base_assessment: Prior municipal taxable assessment in dollars (>= 0).
            capex_amount: Capital expenditures / improvement cost in dollars (>= 0).
            equalization_ratio: Equalization ratio / Director's Ratio (decimal or percentage).

        Returns:
            float: Total post-improvement taxable assessment in dollars.

        Raises:
            ValueError: If base_assessment < 0, capex_amount < 0, or equalization_ratio <= 0.
        """
        if base_assessment < 0:
            raise ValueError(f"base_assessment must be non-negative, got {base_assessment}")
        if capex_amount < 0:
            raise ValueError(f"capex_amount must be non-negative, got {capex_amount}")
        if equalization_ratio <= 0:
            raise ValueError(f"equalization_ratio must be strictly positive, got {equalization_ratio}")

        norm_ratio = equalization_ratio / 100.0 if equalization_ratio > 1.0 else equalization_ratio
        added_amount = capex_amount * norm_ratio
        return base_assessment + added_amount

    @staticmethod
    def calculate_incremental_added_assessment(
        capex_amount: float,
        equalization_ratio: float,
    ) -> float:
        """Calculates the standalone incremental added assessment amount.

        Args:
            capex_amount: Capital expenditures / improvement cost in dollars.
            equalization_ratio: Equalization ratio (decimal or percentage).

        Returns:
            float: Incremental taxable assessment addition.
        """
        if capex_amount < 0:
            raise ValueError(f"capex_amount must be non-negative, got {capex_amount}")
        if equalization_ratio <= 0:
            raise ValueError(f"equalization_ratio must be strictly positive, got {equalization_ratio}")

        norm_ratio = equalization_ratio / 100.0 if equalization_ratio > 1.0 else equalization_ratio
        return capex_amount * norm_ratio
