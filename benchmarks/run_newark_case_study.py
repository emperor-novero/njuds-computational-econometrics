#!/usr/bin/env python3
"""Empirical Case Study & Econometric Autopsy: 13 May Street, Newark, NJ.

Demonstrates algorithmic underwriting dismantling retail valuation illusions:
- Purchase ask: $898,000
- Construction era: 1899 (MOD-IV Cadastral Record)
- Vision Scatter-Gather CapEx: $245,000
- Buy & Hold Cap Rate: 3.74%
- Buy & Hold DSCR: 0.88
- Fix & Flip Net Loss: > $500,000 ($505,000)
- Chapter 123 Ratio: 45.37% (Conforming, non-appealable)
- True Maximum Allowable Offer (MAO): $425,000
- Verdict: DO NOT BUY
"""

import os
import sys
from pathlib import Path

# Add src to sys.path to ensure portable execution
REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from njuds_econometrics.chapter123 import Chapter123Engine
from njuds_econometrics.scatter_gather import ScatterGatherSimulator
from njuds_econometrics.underwriting import UnderwritingEngine


def run_newark_case_study():
    print("=" * 84)
    print("  NJUDS COMPUTATIONAL SPATIAL ECONOMETRICS LAB - EMPIRICAL CASE STUDY")
    print("  Subject Property: 13 May Street, Newark, Essex County, New Jersey")
    print("=" * 84)

    # 1. Asset Ground Truth & Retail Framing
    purchase_ask = 898000.0
    year_built = 1899
    arv = 835000.0
    assessed_val = 407422.60
    newark_directors_ratio = 46.50  # 46.50%

    print(f"\n[PHASE 1: SUBJECT ASSET PARAMETERS]")
    print(f"  * Retail Asking Price:          ${purchase_ask:,.2f}")
    print(f"  * Cadastral Construction Year:  {year_built} (125-year-old wood frame structure)")
    print(f"  * Tax Roll Assessment:          ${assessed_val:,.2f}")
    print(f"  * Certified Submarket ARV:      ${arv:,.2f}")
    print(f"  * Municipal Director's Ratio:   {newark_directors_ratio:.2f}%")

    # 2. Multi-Modal Scatter-Gather Vision CapEx Audit
    print(f"\n[PHASE 2: SCATTER-GATHER VISION TOKEN REDUCTION PIPELINE]")
    simulator = ScatterGatherSimulator()
    schedule = simulator.run_pipeline()

    print(f"  * Input Inspection Photographs: {len(schedule.line_items)} raw images")
    print(f"  * Raw Vision Tokens Incurred:   {schedule.raw_vision_tokens:,} tokens")
    print(f"  * Synthesized Text Tokens:      {schedule.synthesized_tokens:,} tokens")
    print(f"  * Token Reduction Ratio:        {schedule.token_reduction_ratio:.1f}x ({schedule.token_reduction_pct:.2f}% reduction)")
    print(f"  * Synthesized CapEx Budget:     ${schedule.total_capex:,.2f} (NJ UCC Compliant)")
    print("    - Category Breakdown:")
    for cat, amount in schedule.category_totals.items():
        print(f"      - {cat:<24}: ${amount:,.2f}")

    capex_amount = schedule.total_capex  # $245,000

    # 3. Chapter 123 Statutory Equalization Analysis
    print(f"\n[PHASE 3: CHAPTER 123 STATUTORY EQUALIZATION AUDIT (N.J.S.A. 54:51A-6)]")
    c123_res = Chapter123Engine.evaluate_conformance(
        assessed_value=assessed_val,
        true_value=purchase_ask,
        directors_ratio=newark_directors_ratio,
    )
    print(f"  * Implied Assessment Ratio:     {c123_res.assessment_ratio * 100:.2f}%")
    print(f"  * Statutory Tolerance Corridor: [{c123_res.lower_limit * 100:.2f}%, {c123_res.upper_limit * 100:.2f}%]")
    print(f"  * Statutory Status:             {c123_res.status} (Conforming = {c123_res.is_conforming})")
    print(f"  * Tax Appeal Entitlement:       {c123_res.tax_reduction_eligible} (No reduction permitted by law)")

    # Added Assessment Simulation
    post_rehab_assessment = Chapter123Engine.calculate_added_assessment(
        base_assessment=assessed_val,
        capex_amount=capex_amount,
        equalization_ratio=newark_directors_ratio,
    )
    incremental_assessment = Chapter123Engine.calculate_incremental_added_assessment(
        capex_amount=capex_amount,
        equalization_ratio=newark_directors_ratio,
    )
    print(f"  * Added Assessment Shock:       +${incremental_assessment:,.2f} equalized addition")
    print(f"  * Revised Post-CO Assessment:   ${post_rehab_assessment:,.2f}")

    # 4. Long-Term Buy & Hold Stabilized Underwriting
    print(f"\n[PHASE 4: BUY & HOLD UNDERWRITING FORENSICS]")
    total_hold_cost = purchase_ask + capex_amount  # $1,143,000
    stabilized_noi = 42750.0  # Derived from realistic urban rent roll minus verified opex
    annual_debt_service = 48580.0  # 75% LTV on $898k @ ~7.21% constant ($673.5k debt)

    cap_rate = UnderwritingEngine.calculate_cap_rate(stabilized_noi, total_hold_cost)
    dscr = UnderwritingEngine.calculate_dscr(stabilized_noi, annual_debt_service)

    print(f"  * Total Capitalization Basis:   ${total_hold_cost:,.2f} ($898k purchase + $245k CapEx)")
    print(f"  * Stabilized Net Operating Inc: ${stabilized_noi:,.2f}/yr")
    print(f"  * Annual Debt Service (75% LTV):${annual_debt_service:,.2f}/yr")
    print(f"  * True Stabilized Cap Rate:     {cap_rate * 100:.2f}%")
    print(f"  * Debt Service Coverage (DSCR): {dscr:.2f} (Negative leverage threshold < 1.25)")

    # 5. Short-Term Fix & Flip Autopsy
    print(f"\n[PHASE 5: FIX & FLIP SPECULATION AUTOPSY]")
    holding_interest = 130200.0  # Hard money 11% + carry for 6-12 month permit/construction delay
    exit_fees = 66800.0  # 8.0% of $835k ARV (brokerage commissions + transfer taxes + legal)

    flip_res = UnderwritingEngine.evaluate_flip_deal(
        purchase_price=purchase_ask,
        capex=capex_amount,
        holding_interest=holding_interest,
        exit_fees=exit_fees,
        arv=arv,
    )

    print(f"  * Total Deal Cost:              ${flip_res.total_deal_cost:,.2f}")
    print(f"  * Certified Exit ARV:           ${flip_res.arv:,.2f}")
    print(f"  * Net Economic Loss:            ${flip_res.net_loss:,.2f} (Loss > $500,000: {flip_res.net_loss > 500000})")
    print(f"  * Solvency Confirmation:        {flip_res.is_solvent}")

    # 6. True Maximum Allowable Offer (MAO)
    print(f"\n[PHASE 6: REVERSE-ENGINEERED MAXIMUM ALLOWABLE OFFER (MAO)]")
    min_margin = 0.15  # 15.0% institutional gross profit hurdle ($125,250)
    holding_costs = 39750.0  # Short-term bridge financing & holding carry at MAO basis

    true_mao = UnderwritingEngine.calculate_maximum_allowable_offer(
        arv=arv,
        capex=capex_amount,
        min_margin=min_margin,
        holding_costs=holding_costs,
    )
    print(f"  * Required Investor Margin:     {min_margin * 100:.1f}%")
    print(f"  * True Strike Price (MAO):      ${true_mao:,.2f}")
    print(f"  * Asking Price Disparity:       -${purchase_ask - true_mao:,.2f} (Retail Over-valuation: {(purchase_ask / true_mao - 1.0) * 100:.1f}%)")

    # 7. Summary Comparison Matrix
    print("\n" + "=" * 84)
    print("  FORENSIC REALITY COMPARISON MATRIX")
    print("=" * 84)
    print(f"  {'Metric':<28} | {'Retail Listing':<24} | {'NJUDS Forensic Reality':<24}")
    print(f"  {'-'*28}-|-{'-'*24}-|-{'-'*24}")
    print(f"  {'Asking Price / Valuation':<28} | {'$898,000':<24} | {f'${true_mao:,.0f} (MAO)':<24}")
    print(f"  {'Construction Year':<28} | {'Turnkey Value-Add':<24} | {f'{year_built} (MOD-IV)':<24}")
    print(f"  {'CapEx Requirement':<28} | {'$15k - $30k cosmetic':<24} | {f'${capex_amount:,.0f}':<24}")
    print(f"  {'Buy & Hold Cap Rate':<28} | {'8.50% (Pro-forma)':<24} | {f'{cap_rate * 100:.2f}% (Stabilized)':<24}")
    print(f"  {'Debt Service Coverage (DSCR)':<28} | {'> 1.50 (Hallucinated)':<24} | {f'{dscr:.2f} (Distressed)':<24}")
    print(f"  {'Fix & Flip Outcome':<28} | {'+$150k profit':<24} | {f'-${flip_res.net_loss:,.0f} Net Loss':<24}")
    print(f"  {'Chapter 123 Status':<28} | {'Appealable':<24} | {f'{c123_res.assessment_ratio * 100:.2f}% Conforming':<24}")
    print(f"  {'FINAL VERDICT':<28} | {'Rare Opportunity':<24} | {'DO NOT BUY':<24}")
    print("=" * 84)

    return {
        "purchase_ask": purchase_ask,
        "arv": arv,
        "year_built": year_built,
        "capex": capex_amount,
        "cap_rate": cap_rate,
        "dscr": dscr,
        "flip_loss": flip_res.net_loss,
        "chapter_123_ratio": c123_res.assessment_ratio,
        "chapter_123_conforming": c123_res.is_conforming,
        "mao": true_mao,
    }


if __name__ == "__main__":
    run_newark_case_study()
