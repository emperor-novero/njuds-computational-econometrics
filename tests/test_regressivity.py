"""Unit tests for Assessment Regressivity & Uniformity Index Engine."""

import unittest
from njuds_econometrics.regressivity import NJRegressivityEngine


class TestNJRegressivityEngine(unittest.TestCase):
    """Test suite for statistical ratio studies and regressivity diagnostics."""

    def test_ideal_uniform_distribution(self):
        """Perfect horizontal uniformity and zero vertical regressivity (PRD=1.00, COD=0.0%)."""
        sales = [200000.0, 300000.0, 400000.0, 500000.0]
        # Assessed at exactly 80% across the board
        assessments = [160000.0, 240000.0, 320000.0, 400000.0]

        prd = NJRegressivityEngine.calculate_prd(assessments, sales)
        cod = NJRegressivityEngine.calculate_cod(assessments, sales)
        diag = NJRegressivityEngine.evaluate_ratio_study(assessments, sales)

        self.assertEqual(prd, 1.00)
        self.assertEqual(cod, 0.0)
        self.assertTrue(diag.iaao_prd_compliant)
        self.assertTrue(diag.iaao_cod_compliant)
        self.assertFalse(diag.is_regressive)
        self.assertIn("IAAO COMPLIANT", diag.verdict)

    def test_regressive_distribution_detection(self):
        """Lower-value homes assessed at 95%, luxury homes assessed at 50% (PRD > 1.03)."""
        sales = [150000.0, 200000.0, 500000.0, 1500000.0]
        assessments = [
            142500.0,  # 95%
            180000.0,  # 90%
            350000.0,  # 70%
            750000.0   # 50%
        ]

        prd = NJRegressivityEngine.calculate_prd(assessments, sales)
        diag = NJRegressivityEngine.evaluate_ratio_study(assessments, sales)

        # Mean ratio is high, weighted mean is pulled down by the $1.5M sale -> PRD > 1.03
        self.assertGreater(prd, 1.03)
        self.assertTrue(diag.is_regressive)
        self.assertFalse(diag.iaao_prd_compliant)
        self.assertIn("regressiv", diag.verdict.lower())

    def test_high_dispersion_horizontal_inequity(self):
        """Same value class, erratic assessments causing COD > 15%."""
        sales = [300000.0, 300000.0, 300000.0, 300000.0]
        assessments = [150000.0, 210000.0, 330000.0, 390000.0]  # ratios: 0.50, 0.70, 1.10, 1.30

        cod = NJRegressivityEngine.calculate_cod(assessments, sales)
        diag = NJRegressivityEngine.evaluate_ratio_study(assessments, sales)

        self.assertGreater(cod, 15.0)
        self.assertFalse(diag.iaao_cod_compliant)
        self.assertFalse(diag.is_uniform)

    def test_assessment_gini_coefficient(self):
        """Assessment Gini measures inequality of tax burden."""
        sales = [100000.0, 200000.0, 500000.0, 1000000.0]
        # Regressive burden: lower property carries disproportionate assessment
        assessments = [100000.0, 180000.0, 350000.0, 500000.0]
        gini = NJRegressivityEngine.calculate_tax_gini(assessments, sales)

        self.assertGreater(gini, 0.0)
        self.assertLessEqual(gini, 1.0)


if __name__ == "__main__":
    unittest.main()
