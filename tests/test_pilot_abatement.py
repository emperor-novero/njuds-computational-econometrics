"""Unit tests for NJ PILOT & Five-Year Abatement Modeling."""

import unittest
from njuds_econometrics.pilot_abatement import NJPILOTEngine


class TestNJPILOTEngine(unittest.TestCase):
    """Test suite for Long-Term Tax Exemption (PILOT) and Abatement models."""

    def test_standard_pilot_vs_conventional_tax(self):
        """Standard 10% AGR PILOT in Newark compared to conventional ad valorem tax."""
        # Project: $2,000,000 AGR, Assessed Value $25,000,000, Tax Rate 3.80% ($3.80 per $100)
        # Conventional Tax = ($25,000,000 / 100) * 3.80 = $950,000
        # PILOT ASC (10% of AGR) = $200,000
        # Land Tax (Land Assessed $1,000,000) = ($1,000,000 / 100) * 3.80 = $38,000
        # Net ASC = max($200,000, $38,000) = $200,000
        # Savings = $950,000 - $200,000 = $750,000
        res = NJPILOTEngine.evaluate_pilot_agreement(
            property_name="Ironbound Tower",
            municipality="Newark",
            annual_gross_revenue=2000000.0,
            total_project_cost=30000000.0,
            conventional_assessed_value=25000000.0,
            general_tax_rate=3.80,
            pilot_asc_rate=0.10,
            land_assessed_value=1000000.0
        )
        self.assertEqual(res.conventional_tax_liability, 950000.00)
        self.assertEqual(res.pilot_asc_amount, 200000.00)
        self.assertEqual(res.annual_tax_savings, 750000.00)
        self.assertAlmostEqual(res.tax_savings_percentage, 78.95, places=2)
        
        # Statutory Splits: County 5%, Muni 95%, Schools 0%
        self.assertEqual(res.county_5pct_share, 10000.00)
        self.assertEqual(res.municipal_95pct_retention, 190000.00)
        self.assertEqual(res.school_direct_allocation, 0.00)

    def test_pilot_tpc_basis(self):
        """PILOT calculated on 2% of Total Project Cost (TPC)."""
        # TPC: $20,000,000 -> 2% = $400,000 ASC
        res = NJPILOTEngine.evaluate_pilot_agreement(
            property_name="Journal Square Heights",
            municipality="Jersey City",
            annual_gross_revenue=3000000.0,
            total_project_cost=20000000.0,
            conventional_assessed_value=18000000.0,
            general_tax_rate=2.20,  # $2.20 per $100
            pilot_asc_rate=0.02,
            calc_basis="TPC"
        )
        self.assertEqual(res.pilot_asc_amount, 400000.00)
        self.assertEqual(res.conventional_tax_liability, 396000.00)
        # In this edge case, PILOT is higher than conventional
        self.assertEqual(res.annual_tax_savings, -4000.00)

    def test_five_year_abatement_schedule(self):
        """5-Year phase-in schedule under N.J.S.A. 40A:21."""
        # Land: $100,000, Added Improvement: $400,000, Tax Rate 3.00%
        # Land tax = $3,000/yr every year
        # Full improvement tax = $12,000/yr
        # Year 1: 0% imp tax -> Total tax = $3,000 (Savings $12,000)
        # Year 2: 20% imp tax = $2,400 -> Total tax = $5,400 (Savings $9,600)
        # Year 3: 40% imp tax = $4,800 -> Total tax = $7,800 (Savings $7,200)
        # Year 4: 60% imp tax = $7,200 -> Total tax = $10,200 (Savings $4,800)
        # Year 5: 80% imp tax = $9,600 -> Total tax = $12,600 (Savings $2,400)
        schedule = NJPILOTEngine.calculate_five_year_abatement_schedule(
            pre_rehab_land_assessed_value=100000.0,
            improvement_added_value=400000.0,
            general_tax_rate=3.00
        )
        self.assertEqual(len(schedule), 5)
        self.assertEqual(schedule[0].total_tax_due, 3000.00)
        self.assertEqual(schedule[0].annual_savings, 12000.00)
        self.assertEqual(schedule[1].total_tax_due, 5400.00)
        self.assertEqual(schedule[2].total_tax_due, 7800.00)
        self.assertEqual(schedule[3].total_tax_due, 10200.00)
        self.assertEqual(schedule[4].total_tax_due, 12600.00)
        self.assertEqual(schedule[4].annual_savings, 2400.00)

    def test_pilot_net_present_value(self):
        """NPV of 30-year abatement tax shield at 7% discount rate."""
        npv = NJPILOTEngine.calculate_pilot_net_present_value(
            initial_annual_savings=500000.0,
            duration_years=30,
            discount_rate=0.07,
            annual_growth_rate=0.02
        )
        self.assertGreater(npv, 5000000.0)  # Multi-million dollar equity value creation


if __name__ == "__main__":
    unittest.main()
