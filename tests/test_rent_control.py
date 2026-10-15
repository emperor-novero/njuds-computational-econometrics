"""Unit tests for NJ Rent Control & Vacancy Decontrol Modeling."""

import unittest
from njuds_econometrics.rent_control import NJRentControlEngine


class TestNJRentControlEngine(unittest.TestCase):
    """Test suite for New Jersey municipal rent control logic."""

    def test_newark_cpi_below_cap(self):
        """Newark: CPI (3.2%) is below municipal hard cap (5.0%)."""
        res = NJRentControlEngine.evaluate_allowable_increase(
            base_rent=2000.0,
            cpi_rate=0.032,
            municipality="Newark",
            unit_count=4
        )
        self.assertFalse(res.is_exempt)
        self.assertEqual(res.effective_increase_rate, 0.032)
        self.assertEqual(res.allowable_increase_dollars, 64.00)
        self.assertEqual(res.new_max_legal_rent, 2064.00)

    def test_newark_cpi_above_cap(self):
        """Newark: High inflation (6.5%) is constrained by 5.0% hard cap."""
        res = NJRentControlEngine.evaluate_allowable_increase(
            base_rent=1500.0,
            cpi_rate=0.065,
            municipality="Newark",
            unit_count=6
        )
        self.assertFalse(res.is_exempt)
        self.assertEqual(res.effective_increase_rate, 0.05)
        self.assertEqual(res.allowable_increase_dollars, 75.00)
        self.assertEqual(res.new_max_legal_rent, 1575.00)

    def test_jersey_city_cpi_cap(self):
        """Jersey City: Capped at 4.0% under Chapter 260."""
        res = NJRentControlEngine.evaluate_allowable_increase(
            base_rent=2500.0,
            cpi_rate=0.048,
            municipality="Jersey City",
            unit_count=5
        )
        self.assertFalse(res.is_exempt)
        self.assertEqual(res.effective_increase_rate, 0.04)
        self.assertEqual(res.allowable_increase_dollars, 100.00)
        self.assertEqual(res.new_max_legal_rent, 2600.00)

    def test_owner_occupied_three_family_exemption(self):
        """Owner-occupied 3-family dwelling is statutory exempt under N.J.S.A. 2A:18-61.1."""
        res = NJRentControlEngine.evaluate_allowable_increase(
            base_rent=1800.0,
            cpi_rate=0.06,
            municipality="Newark",
            unit_count=3,
            is_owner_occupied=True
        )
        self.assertTrue(res.is_exempt)
        self.assertIn("Owner-occupied", res.exemption_reason)
        # Not constrained by municipal 5% cap
        self.assertEqual(res.effective_increase_rate, 0.06)

    def test_capital_improvement_surcharge_approval(self):
        """Capital improvement surcharge pass-through amortized over 7 years."""
        # $84,000 CapEx / (4 units * 84 months) = $250/month unconstrained
        # Base rent = $2,000 -> Max 15% surcharge = $300/month -> $250 is fully allowable
        res = NJRentControlEngine.calculate_capital_improvement_surcharge(
            total_capex=84000.0,
            num_units=4,
            base_rent=2000.0,
            municipality="Newark"
        )
        self.assertTrue(res.is_approved)
        self.assertEqual(res.useful_life_months, 84)
        self.assertEqual(res.monthly_cost_per_unit, 250.00)
        self.assertEqual(res.applied_monthly_surcharge, 250.00)

    def test_capital_improvement_surcharge_capped(self):
        """Capital improvement surcharge hits 15% base rent ceiling."""
        # $168,000 CapEx / (4 units * 84 months) = $500/month unconstrained
        # Base rent = $2,000 -> 15% cap = $300/month -> capped at $300
        res = NJRentControlEngine.calculate_capital_improvement_surcharge(
            total_capex=168000.0,
            num_units=4,
            base_rent=2000.0,
            municipality="Newark"
        )
        self.assertTrue(res.is_approved)
        self.assertEqual(res.monthly_cost_per_unit, 500.00)
        self.assertEqual(res.applied_monthly_surcharge, 300.00)

    def test_substantial_rehabilitation_qualification(self):
        """Substantial rehab: CapEx exceeds 50% of assessed valuation."""
        qualifies, ratio, thresh = NJRentControlEngine.evaluate_substantial_rehabilitation(
            capex_amount=245000.0,
            pre_rehab_assessed_value=300000.0,
            municipality="Newark"
        )
        self.assertTrue(qualifies)
        self.assertGreaterEqual(ratio, 0.50)
        self.assertEqual(thresh, 0.50)

    def test_margin_compression_simulation(self):
        """Multi-year simulation reveals margin decay when expense inflation > rent cap."""
        sim = NJRentControlEngine.simulate_rent_control_margin_compression(
            initial_gross_rent=100000.0,
            initial_operating_expenses=60000.0,
            cpi_rent_cap=0.03,  # 3% rent growth cap
            actual_expense_inflation=0.07,  # 7% real expense inflation
            years=3
        )
        self.assertEqual(len(sim), 3)
        # Year 1: Rent=103000, Exp=64200, NOI=38800 (Margin 37.67%)
        # Year 3: Rent=109272.7, Exp=73502.58 -> Margin shrinks substantially
        self.assertLess(sim[-1]["operating_margin_pct"], sim[0]["operating_margin_pct"])


if __name__ == "__main__":
    unittest.main()
