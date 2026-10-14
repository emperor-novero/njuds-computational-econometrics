"""Institutional Underwriting Engine for Spatial Econometrics & Real Estate Forensics.

Provides deterministic computational implementations for:
- Capitalization Rate (Cap Rate)
- Debt Service Coverage Ratio (DSCR)
- Fix & Flip Deal Autopsy & Net Economic Loss
- Maximum Allowable Offer (MAO) under institutional margin constraints
"""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class FlipUnderwritingResult:
    """Summary of a short-term Fix & Flip deal autopsy."""

    purchase_price: float
    capex: float
    holding_interest: float
    exit_fees: float
    total_deal_cost: float
    arv: float
    net_loss: float
    net_profit: float
    is_solvent: bool


@dataclass(frozen=True)
class HoldUnderwritingResult:
    """Summary of a long-term Buy & Hold stabilized investment."""

    purchase_price: float
    capex: float
    total_cost: float
    gross_rent_annual: float
    effective_gross_income: float
    operating_expenses: float
    noi: float
    annual_debt_service: float
    cap_rate: float
    dscr: float
    is_solvent: bool


class UnderwritingEngine:
    """Algorithmic underwriting engine for real estate acquisition forensics."""

    @staticmethod
    def calculate_cap_rate(noi: float, total_cost: float) -> float:
        """Calculates the Capitalization Rate (Cap Rate).

        Formula:
            Cap Rate = NOI / Total Cost
        Where Total Cost = Purchase Price + Mandatory CapEx.

        Args:
            noi: Net Operating Income in dollars (annualized).
            total_cost: Total basis / capital expenditure in dollars (> 0).

        Returns:
            float: Capitalization rate as a decimal (e.g., 0.0374 for 3.74%).

        Raises:
            ValueError: If total_cost <= 0.
        """
        if total_cost <= 0:
            raise ValueError(f"total_cost must be strictly positive, got {total_cost}")
        return noi / total_cost

    @staticmethod
    def calculate_dscr(noi: float, annual_debt_service: float) -> float:
        """Calculates the Debt Service Coverage Ratio (DSCR).

        Formula:
            DSCR = NOI / Annual Debt Service

        Args:
            noi: Net Operating Income in dollars (annualized).
            annual_debt_service: Total principal and interest debt service in dollars (> 0).

        Returns:
            float: Debt Service Coverage Ratio (e.g., 0.88).

        Raises:
            ValueError: If annual_debt_service <= 0.
        """
        if annual_debt_service <= 0:
            raise ValueError(f"annual_debt_service must be strictly positive, got {annual_debt_service}")
        return noi / annual_debt_service

    @staticmethod
    def calculate_fix_and_flip_loss(
        purchase_price: float,
        capex: float,
        holding_interest: float,
        exit_fees: float,
        arv: float,
    ) -> float:
        """Calculates the net economic loss on a distressed Fix & Flip acquisition.

        Formula:
            Total Deal Cost = Purchase Price + CapEx + Holding Interest + Exit Fees
            Net Loss = Total Deal Cost - ARV

        A positive result represents a financial loss; a negative result represents profit.

        Args:
            purchase_price: Initial acquisition price in dollars (>= 0).
            capex: Total rehabilitation and code-compliance expenditures in dollars (>= 0).
            holding_interest: Cost of short-term / hard money financing and taxes during hold (>= 0).
            exit_fees: Transaction closing costs, broker commissions, transfer taxes (>= 0).
            arv: Certified After Repair Value in dollars (> 0).

        Returns:
            float: Net economic loss in dollars.

        Raises:
            ValueError: If arv <= 0 or any cost parameter is negative.
        """
        if arv <= 0:
            raise ValueError(f"arv must be strictly positive, got {arv}")
        if purchase_price < 0 or capex < 0 or holding_interest < 0 or exit_fees < 0:
            raise ValueError("All cost parameters must be non-negative")

        total_deal_cost = purchase_price + capex + holding_interest + exit_fees
        net_loss = total_deal_cost - arv
        return net_loss

    @staticmethod
    def calculate_maximum_allowable_offer(
        arv: float,
        capex: float,
        min_margin: float,
        holding_costs: float,
    ) -> float:
        """Calculates the Maximum Allowable Offer (MAO) to guarantee underwriting solvency.

        Formula:
            MAO = ARV * (1 - min_margin) - CapEx - Holding Costs

        Args:
            arv: Certified After-Repair Value in dollars (> 0).
            capex: Mandatory capital expenditures / remediation budget in dollars (>= 0).
            min_margin: Required gross investor profit margin (as decimal [0, 1] or percent [0, 100]).
            holding_costs: Financing carry, municipal taxes, and exit transactional fees in dollars (>= 0).

        Returns:
            float: Maximum allowable offer strike price in dollars.

        Raises:
            ValueError: If arv <= 0, capex < 0, holding_costs < 0, or min_margin < 0.
        """
        if arv <= 0:
            raise ValueError(f"arv must be strictly positive, got {arv}")
        if capex < 0:
            raise ValueError(f"capex must be non-negative, got {capex}")
        if holding_costs < 0:
            raise ValueError(f"holding_costs must be non-negative, got {holding_costs}")
        if min_margin < 0:
            raise ValueError(f"min_margin must be non-negative, got {min_margin}")

        margin_decimal = min_margin / 100.0 if min_margin > 1.0 else min_margin
        if margin_decimal >= 1.0:
            raise ValueError(f"min_margin must be strictly less than 100%, got {min_margin}")

        mao = (arv * (1.0 - margin_decimal)) - capex - holding_costs
        return mao

    @classmethod
    def evaluate_flip_deal(
        cls,
        purchase_price: float,
        capex: float,
        holding_interest: float,
        exit_fees: float,
        arv: float,
    ) -> FlipUnderwritingResult:
        """Produces a structured FlipUnderwritingResult autopsy."""
        total_deal_cost = purchase_price + capex + holding_interest + exit_fees
        net_loss = cls.calculate_fix_and_flip_loss(
            purchase_price=purchase_price,
            capex=capex,
            holding_interest=holding_interest,
            exit_fees=exit_fees,
            arv=arv,
        )
        net_profit = arv - total_deal_cost
        is_solvent = net_profit > 0

        return FlipUnderwritingResult(
            purchase_price=purchase_price,
            capex=capex,
            holding_interest=holding_interest,
            exit_fees=exit_fees,
            total_deal_cost=total_deal_cost,
            arv=arv,
            net_loss=net_loss,
            net_profit=net_profit,
            is_solvent=is_solvent,
        )

    @classmethod
    def evaluate_hold_deal(
        cls,
        purchase_price: float,
        capex: float,
        gross_rent_annual: float,
        operating_expenses: float,
        annual_debt_service: float,
        vacancy_rate: float = 0.08,
    ) -> HoldUnderwritingResult:
        """Produces a structured HoldUnderwritingResult autopsy."""
        total_cost = purchase_price + capex
        effective_gross_income = gross_rent_annual * (1.0 - vacancy_rate)
        noi = effective_gross_income - operating_expenses
        cap_rate = cls.calculate_cap_rate(noi, total_cost)
        dscr = cls.calculate_dscr(noi, annual_debt_service)
        is_solvent = dscr >= 1.25 and noi > 0

        return HoldUnderwritingResult(
            purchase_price=purchase_price,
            capex=capex,
            total_cost=total_cost,
            gross_rent_annual=gross_rent_annual,
            effective_gross_income=effective_gross_income,
            operating_expenses=operating_expenses,
            noi=noi,
            annual_debt_service=annual_debt_service,
            cap_rate=cap_rate,
            dscr=dscr,
            is_solvent=is_solvent,
        )
