"""Unit tests for Underwriting Engine and Scatter-Gather Vision Pipeline."""

import sys
import unittest
from pathlib import Path

# Add src to sys.path for direct test discovery
REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from njuds_econometrics.scatter_gather import (
    CapExSchedule,
    ImageFeature,
    ScatterGatherSimulator,
)
from njuds_econometrics.underwriting import UnderwritingEngine


class TestUnderwritingEngine(unittest.TestCase):
    """Test suite for algorithmic underwriting formulas and financial edge cases."""

    def test_calculate_cap_rate_newark(self):
        """Verifies true stabilized cap rate calculation for 13 May St."""
        # Stabilized NOI: $42,750, Total Basis: $898,000 purchase + $245,000 CapEx = $1,143,000
        noi = 42750.0
        total_cost = 1143000.0
        cap_rate = UnderwritingEngine.calculate_cap_rate(noi, total_cost)
        self.assertAlmostEqual(cap_rate, 0.0374, places=4)
        self.assertAlmostEqual(cap_rate * 100, 3.74, places=2)

    def test_calculate_cap_rate_invalid_cost(self):
        """Non-positive total cost must raise ValueError."""
        with self.assertRaises(ValueError):
            UnderwritingEngine.calculate_cap_rate(50000.0, 0.0)
        with self.assertRaises(ValueError):
            UnderwritingEngine.calculate_cap_rate(50000.0, -100000.0)

    def test_calculate_dscr_newark(self):
        """Verifies debt service coverage ratio (DSCR) for 13 May St."""
        # Stabilized NOI: $42,750, Debt Service: $48,580
        noi = 42750.0
        annual_debt_service = 48580.0
        dscr = UnderwritingEngine.calculate_dscr(noi, annual_debt_service)
        self.assertAlmostEqual(dscr, 0.88, places=2)

    def test_calculate_dscr_invalid_debt_service(self):
        """Non-positive debt service must raise ValueError."""
        with self.assertRaises(ValueError):
            UnderwritingEngine.calculate_dscr(50000.0, 0.0)
        with self.assertRaises(ValueError):
            UnderwritingEngine.calculate_dscr(50000.0, -1000.0)

    def test_calculate_fix_and_flip_loss_newark(self):
        """Verifies fix and flip autopsy for 13 May St (net loss > $500,000)."""
        purchase_price = 898000.0
        capex = 245000.0
        holding_interest = 130200.0
        exit_fees = 66800.0
        arv = 835000.0

        net_loss = UnderwritingEngine.calculate_fix_and_flip_loss(
            purchase_price=purchase_price,
            capex=capex,
            holding_interest=holding_interest,
            exit_fees=exit_fees,
            arv=arv,
        )

        total_deal_cost = purchase_price + capex + holding_interest + exit_fees
        self.assertEqual(total_deal_cost, 1340000.0)
        self.assertEqual(net_loss, 505000.0)
        self.assertGreater(net_loss, 500000.0)

    def test_calculate_fix_and_flip_profitable_deal(self):
        """Verifies that profitable deals yield negative loss values."""
        purchase_price = 300000.0
        capex = 50000.0
        holding_interest = 20000.0
        exit_fees = 30000.0
        arv = 500000.0

        net_loss = UnderwritingEngine.calculate_fix_and_flip_loss(
            purchase_price=purchase_price,
            capex=capex,
            holding_interest=holding_interest,
            exit_fees=exit_fees,
            arv=arv,
        )
        self.assertEqual(net_loss, -100000.0)  # -$100k loss = $100k profit

    def test_calculate_maximum_allowable_offer_newark(self):
        """Verifies reverse-engineered $425,000 MAO strike price for 13 May St."""
        arv = 835000.0
        capex = 245000.0
        min_margin = 0.15  # 15% investor hurdle
        holding_costs = 39750.0

        mao = UnderwritingEngine.calculate_maximum_allowable_offer(
            arv=arv,
            capex=capex,
            min_margin=min_margin,
            holding_costs=holding_costs,
        )
        self.assertAlmostEqual(mao, 425000.0, places=2)

        # Passing margin as percentage (15.0%)
        mao_pct = UnderwritingEngine.calculate_maximum_allowable_offer(
            arv=arv,
            capex=capex,
            min_margin=15.0,
            holding_costs=holding_costs,
        )
        self.assertAlmostEqual(mao_pct, 425000.0, places=2)

    def test_underwriting_invalid_arguments(self):
        """Verifies exception handling across underwriting engine."""
        with self.assertRaises(ValueError):
            UnderwritingEngine.calculate_maximum_allowable_offer(
                arv=-100.0, capex=50000.0, min_margin=0.15, holding_costs=10000.0
            )
        with self.assertRaises(ValueError):
            UnderwritingEngine.calculate_maximum_allowable_offer(
                arv=500000.0, capex=50000.0, min_margin=150.0, holding_costs=10000.0
            )
        with self.assertRaises(ValueError):
            UnderwritingEngine.calculate_maximum_allowable_offer(
                arv=500000.0, capex=50000.0, min_margin=-0.05, holding_costs=10000.0
            )
        with self.assertRaises(ValueError):
            UnderwritingEngine.calculate_fix_and_flip_loss(
                purchase_price=-1000.0, capex=10000.0, holding_interest=1000.0, exit_fees=1000.0, arv=100000.0
            )

    def test_evaluate_flip_deal_structure(self):
        """Verifies structured FlipUnderwritingResult fields."""
        res = UnderwritingEngine.evaluate_flip_deal(
            purchase_price=898000.0,
            capex=245000.0,
            holding_interest=130200.0,
            exit_fees=66800.0,
            arv=835000.0,
        )
        self.assertEqual(res.total_deal_cost, 1340000.0)
        self.assertEqual(res.net_loss, 505000.0)
        self.assertEqual(res.net_profit, -505000.0)
        self.assertFalse(res.is_solvent)

    def test_evaluate_hold_deal_structure(self):
        """Verifies structured HoldUnderwritingResult fields."""
        res = UnderwritingEngine.evaluate_hold_deal(
            purchase_price=898000.0,
            capex=245000.0,
            gross_rent_annual=80000.0,
            operating_expenses=30850.0,
            annual_debt_service=48580.0,
            vacancy_rate=0.08,
        )
        self.assertEqual(res.total_cost, 1143000.0)
        self.assertAlmostEqual(res.effective_gross_income, 73600.0, places=2)
        self.assertAlmostEqual(res.noi, 42750.0, places=2)
        self.assertAlmostEqual(res.cap_rate, 0.0374, places=4)
        self.assertAlmostEqual(res.dscr, 0.88, places=2)
        self.assertFalse(res.is_solvent)


class TestScatterGatherSimulator(unittest.TestCase):
    """Test suite for the Scatter-Gather Map-Reduce vision token reduction engine."""

    def test_canonical_gallery_capex_and_tokens(self):
        """Verifies that the canonical 24-image gallery produces $245,000 CapEx and >95% token reduction."""
        simulator = ScatterGatherSimulator()
        schedule = simulator.run_pipeline()

        self.assertEqual(len(schedule.line_items), 24)
        self.assertEqual(schedule.total_capex, 245000.0)
        self.assertEqual(schedule.raw_vision_tokens, 24 * 1600)  # 38,400
        self.assertGreater(schedule.token_reduction_pct, 95.0)
        self.assertEqual(schedule.ucc_compliance_status, "NJ_UCC_COMPLIANT")

    def test_scatter_gather_custom_features(self):
        """Verifies scatter and gather with custom image features."""
        custom_features = [
            ImageFeature(
                room="Roof / Attic",
                defect_type="Rotted Rafters",
                severity="HIGH",
                estimated_cost=15000.0,
                raw_vision_tokens=1600,
                reduced_text_tokens=40,
            ),
            ImageFeature(
                room="Basement / Electrical",
                defect_type="Fuse Box",
                severity="CRITICAL",
                estimated_cost=10000.0,
                raw_vision_tokens=1600,
                reduced_text_tokens=40,
            ),
        ]
        sim = ScatterGatherSimulator(features=custom_features)
        schedule = sim.run_pipeline()

        self.assertEqual(schedule.total_capex, 25000.0)
        self.assertEqual(len(schedule.line_items), 2)
        self.assertEqual(schedule.raw_vision_tokens, 3200)

    def test_empty_scatter_gather_raises_value_error(self):
        """Verifies that empty feature inputs raise ValueError."""
        sim = ScatterGatherSimulator(features=[])
        with self.assertRaises(ValueError):
            sim.scatter()
        with self.assertRaises(ValueError):
            sim.gather([])


if __name__ == "__main__":
    unittest.main()
