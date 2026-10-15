"""NJ Municipal Rent Control & Vacancy Decontrol Modeling.

Statutory and municipal framework for residential rent stabilization in New Jersey,
governed locally under Inganamort v. Borough of Fort Lee, 62 N.J. 521 (1973).
Models municipal CPI-indexed rent caps, capital improvement surcharges,
substantial rehabilitation exemptions, and owner-occupant exclusions
(e.g., Newark Title XIX, Jersey City Chapter 260).
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


@dataclass
class RentIncreaseEvaluation:
    """Evaluation result for an allowable municipal rent increase."""
    municipality: str
    base_rent: float
    cpi_rate: float
    statutory_cap_rate: float
    effective_increase_rate: float
    allowable_increase_dollars: float
    new_max_legal_rent: float
    is_exempt: bool
    exemption_reason: Optional[str] = None


@dataclass
class CapitalImprovementSurchargeResult:
    """Result of a municipal capital improvement rent surcharge application."""
    total_eligible_capex: float
    useful_life_months: int
    num_benefiting_units: int
    monthly_cost_per_unit: float
    max_allowable_surcharge_pct: float
    applied_monthly_surcharge: float
    is_approved: bool
    denial_reason: Optional[str] = None


class NJRentControlEngine:
    """Computational modeling engine for New Jersey municipal rent control ordinances.
    
    In New Jersey, rent regulation is governed at the municipal level pursuant to
    municipal police powers upheld in Inganamort v. Fort Lee (1973).
    Currently, over 100 New Jersey municipalities have active rent leveling ordinances.
    """

    # Municipal parameters: (hard_cap_percent, min_units_for_coverage, default_cpi_cap)
    MUNICIPAL_STANDARDS: Dict[str, Dict[str, float]] = {
        "Newark": {
            "max_cap": 0.05,            # Newark Title XIX: Lower of CPI or 5.0%
            "min_units": 4,             # Exempts 1-3 family owner-occupied; 4+ covered
            "substantial_rehab_threshold": 0.50, # CapEx >= 50% of assessed value for exemption
            "capex_amortization_years": 7.0,
            "max_surcharge_ratio": 0.15 # Max 15% surcharge over base rent
        },
        "Jersey City": {
            "max_cap": 0.04,            # Jersey City Ch. 260: Lower of CPI or 4.0%
            "min_units": 5,             # 5+ units covered (commercial exemptions apply)
            "substantial_rehab_threshold": 0.50,
            "capex_amortization_years": 10.0,
            "max_surcharge_ratio": 0.15
        },
        "Hoboken": {
            "max_cap": 0.075,           # Hoboken Rent Leveling Ch. 155
            "min_units": 4,
            "substantial_rehab_threshold": 0.50,
            "capex_amortization_years": 5.0,
            "max_surcharge_ratio": 0.20
        },
        "East Orange": {
            "max_cap": 0.05,
            "min_units": 4,
            "substantial_rehab_threshold": 0.40,
            "capex_amortization_years": 7.0,
            "max_surcharge_ratio": 0.15
        },
        "Paterson": {
            "max_cap": 0.05,
            "min_units": 3,
            "substantial_rehab_threshold": 0.50,
            "capex_amortization_years": 8.0,
            "max_surcharge_ratio": 0.15
        }
    }

    @classmethod
    def evaluate_allowable_increase(
        cls,
        base_rent: float,
        cpi_rate: float,
        municipality: str = "Newark",
        unit_count: int = 4,
        is_owner_occupied: bool = False
    ) -> RentIncreaseEvaluation:
        """Calculates allowable annual rent increase under municipal ordinance.
        
        Args:
            base_rent: Current lawful monthly contract rent in USD.
            cpi_rate: Regional CPI-U increase rate as a decimal (e.g., 0.032 for 3.2%).
            municipality: Target NJ municipality name.
            unit_count: Total residential dwelling units in the structure.
            is_owner_occupied: True if owner resides in one of the units.
            
        Returns:
            RentIncreaseEvaluation with statutory caps and new allowable rent.
        """
        # State-level and municipal owner-occupancy exemption check
        if is_owner_occupied and unit_count <= 3:
            return RentIncreaseEvaluation(
                municipality=municipality,
                base_rent=base_rent,
                cpi_rate=cpi_rate,
                statutory_cap_rate=1.0,
                effective_increase_rate=cpi_rate,
                allowable_increase_dollars=round(base_rent * cpi_rate, 2),
                new_max_legal_rent=round(base_rent * (1.0 + cpi_rate), 2),
                is_exempt=True,
                exemption_reason="Exempt under N.J.S.A. 2A:18-61.1(1) (Owner-occupied 1-3 family dwelling)"
            )

        rules = cls.MUNICIPAL_STANDARDS.get(municipality, cls.MUNICIPAL_STANDARDS["Newark"])
        
        # Check unit count threshold
        if unit_count < rules["min_units"]:
            return RentIncreaseEvaluation(
                municipality=municipality,
                base_rent=base_rent,
                cpi_rate=cpi_rate,
                statutory_cap_rate=1.0,
                effective_increase_rate=cpi_rate,
                allowable_increase_dollars=round(base_rent * cpi_rate, 2),
                new_max_legal_rent=round(base_rent * (1.0 + cpi_rate), 2),
                is_exempt=True,
                exemption_reason=f"Exempt: Building size ({unit_count} units) below municipal threshold ({rules['min_units']} units)"
            )

        # Allowable increase is minimum of positive CPI or municipal hard cap
        effective_cpi = max(0.0, cpi_rate)
        hard_cap = rules["max_cap"]
        effective_rate = min(effective_cpi, hard_cap)
        
        increase_dollars = round(base_rent * effective_rate, 2)
        new_rent = round(base_rent + increase_dollars, 2)

        return RentIncreaseEvaluation(
            municipality=municipality,
            base_rent=base_rent,
            cpi_rate=cpi_rate,
            statutory_cap_rate=hard_cap,
            effective_increase_rate=effective_rate,
            allowable_increase_dollars=increase_dollars,
            new_max_legal_rent=new_rent,
            is_exempt=False
        )

    @classmethod
    def calculate_capital_improvement_surcharge(
        cls,
        total_capex: float,
        num_units: int,
        base_rent: float,
        municipality: str = "Newark",
        custom_amortization_years: Optional[float] = None
    ) -> CapitalImprovementSurchargeResult:
        """Calculates municipal Capital Improvement Surcharge pass-through.
        
        In cities like Newark and Jersey City, landlords who execute major capital
        improvements (e.g. new heating plant, roof replacement, MEP re-piping) may
        petition the Rent Leveling Board to pass through the cost amortized over 5-10 years.
        
        Args:
            total_capex: Total validated capital expenditure in USD.
            num_units: Total units benefiting from the capital improvement.
            base_rent: Unit base monthly rent in USD.
            municipality: Target municipality.
            custom_amortization_years: Override for amortization schedule if permitted.
            
        Returns:
            CapitalImprovementSurchargeResult with monthly surcharge and limit compliance.
        """
        if num_units <= 0 or total_capex <= 0:
            return CapitalImprovementSurchargeResult(
                total_eligible_capex=total_capex,
                useful_life_months=0,
                num_benefiting_units=num_units,
                monthly_cost_per_unit=0.0,
                max_allowable_surcharge_pct=0.0,
                applied_monthly_surcharge=0.0,
                is_approved=False,
                denial_reason="Invalid CapEx amount or non-positive unit count"
            )

        rules = cls.MUNICIPAL_STANDARDS.get(municipality, cls.MUNICIPAL_STANDARDS["Newark"])
        amort_years = custom_amortization_years or rules["capex_amortization_years"]
        amort_months = int(amort_years * 12)

        # Monthly unconstrained cost per unit
        monthly_cost_per_unit = total_capex / (num_units * amort_months)
        
        # Max allowable surcharge ceiling (typically 15% to 20% of base rent)
        max_pct = rules["max_surcharge_ratio"]
        max_monthly_dollars = base_rent * max_pct

        applied_surcharge = round(min(monthly_cost_per_unit, max_monthly_dollars), 2)

        return CapitalImprovementSurchargeResult(
            total_eligible_capex=total_capex,
            useful_life_months=amort_months,
            num_benefiting_units=num_units,
            monthly_cost_per_unit=round(monthly_cost_per_unit, 2),
            max_allowable_surcharge_pct=max_pct,
            applied_monthly_surcharge=applied_surcharge,
            is_approved=True
        )

    @classmethod
    def evaluate_substantial_rehabilitation(
        cls,
        capex_amount: float,
        pre_rehab_assessed_value: float,
        municipality: str = "Newark"
    ) -> Tuple[bool, float, float]:
        """Evaluates whether rehabilitation qualifies for substantial rehab exemption.
        
        Under many NJ ordinances (e.g. Newark Title XIX), an owner who expends at least
        50% of the pre-rehab assessed value on gut-rehabilitation may petition for
        temporary exemption from rent leveling for a period of up to 5 years.
        
        Returns:
            Tuple of (is_qualifying, actual_ratio, required_threshold_ratio).
        """
        rules = cls.MUNICIPAL_STANDARDS.get(municipality, cls.MUNICIPAL_STANDARDS["Newark"])
        threshold = rules["substantial_rehab_threshold"]
        
        if pre_rehab_assessed_value <= 0:
            return False, 0.0, threshold
            
        ratio = capex_amount / pre_rehab_assessed_value
        return ratio >= threshold, round(ratio, 4), threshold

    @classmethod
    def simulate_rent_control_margin_compression(
        cls,
        initial_gross_rent: float,
        initial_operating_expenses: float,
        cpi_rent_cap: float,
        actual_expense_inflation: float,
        years: int = 5
    ) -> List[Dict[str, float]]:
        """Simulates multi-year Net Operating Income (NOI) decay under rent control.
        
        Demonstrates the econometric trap where real operating expenses (property taxes,
        insurance, utilities) inflate faster than the statutory rent ceiling.
        
        Returns:
            Year-by-year schedule of Gross Rent, Expenses, NOI, and Profit Margin.
        """
        schedule = []
        rent = initial_gross_rent
        expenses = initial_operating_expenses

        for year in range(1, years + 1):
            rent = rent * (1.0 + cpi_rent_cap)
            expenses = expenses * (1.0 + actual_expense_inflation)
            noi = rent - expenses
            margin = (noi / rent) if rent > 0 else 0.0

            schedule.append({
                "year": year,
                "gross_rent": round(rent, 2),
                "expenses": round(expenses, 2),
                "noi": round(noi, 2),
                "operating_margin_pct": round(margin * 100, 2)
            })

        return schedule
