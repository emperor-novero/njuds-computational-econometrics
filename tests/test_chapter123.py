"""Unit tests for Chapter 123 Equalization Engine and Conformance Modeling."""

import sys
import unittest
from pathlib import Path

# Add src to sys.path for direct test discovery
REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from njuds_econometrics.chapter123 import Chapter123Engine, ConformanceResult


class TestChapter123Engine(unittest.TestCase):
    """Test suite for New Jersey Chapter 123 statutory formulas and edge cases."""

    def test_corridor_calculation_decimal(self):
        """Verifies corridor limits computed from decimal Director's Ratio."""
        directors_ratio = 0.4650
        lower, upper = Chapter123Engine.calculate_corridor(directors_ratio)
        self.assertAlmostEqual(lower, 0.39525, places=5)
        self.assertAlmostEqual(upper, 0.53475, places=5)

    def test_corridor_calculation_percentage(self):
        """Verifies corridor limits computed from percentage Director's Ratio."""
        directors_ratio = 46.50
        lower, upper = Chapter123Engine.calculate_corridor(directors_ratio)
        self.assertAlmostEqual(lower, 39.525, places=3)
        self.assertAlmostEqual(upper, 53.475, places=3)

    def test_corridor_invalid_ratio(self):
        """Non-positive ratios must raise ValueError."""
        with self.assertRaises(ValueError):
            Chapter123Engine.calculate_corridor(0.0)
        with self.assertRaises(ValueError):
            Chapter123Engine.calculate_corridor(-0.5)

    def test_evaluate_conformance_conforming_newark(self):
        """Tests the canonical 13 May St Newark conforming scenario."""
        # 13 May St: Assessed $407,422.60 against $898,000 acquisition ask
        # Implied ratio: 45.37%, Newark Director's Ratio: 46.50%
        result = Chapter123Engine.evaluate_conformance(
            assessed_value=407422.60,
            true_value=898000.0,
            directors_ratio=46.50,
        )
        self.assertTrue(result.is_conforming)
        self.assertEqual(result.status, "CONFORMING")
        self.assertFalse(result.tax_reduction_eligible)
        self.assertAlmostEqual(result.assessment_ratio, 0.4537, places=4)
        self.assertAlmostEqual(result.lower_limit, 0.39525, places=5)
        self.assertAlmostEqual(result.upper_limit, 0.53475, places=5)
        self.assertEqual(result.revised_assessment, 407422.60)

    def test_evaluate_conformance_over_assessed_tax_appeal(self):
        """Tests over-assessed property where taxpayer is statutorily entitled to reduction."""
        true_value = 500000.0
        assessed_value = 400000.0  # Ratio: 80.0%
        directors_ratio = 60.0  # 60.0%, Corridor: [51.0%, 69.0%]

        result = Chapter123Engine.evaluate_conformance(
            assessed_value=assessed_value,
            true_value=true_value,
            directors_ratio=directors_ratio,
        )
        self.assertFalse(result.is_conforming)
        self.assertEqual(result.status, "OVER_ASSESSED")
        self.assertTrue(result.tax_reduction_eligible)
        # Reduced to Director's Ratio: $500,000 * 0.60 = $300,000
        self.assertAlmostEqual(result.revised_assessment, 300000.0, places=2)

    def test_evaluate_conformance_under_assessed_shield(self):
        """Tests under-assessed property shielded by Van Decker spot assessment doctrine."""
        true_value = 1000000.0
        assessed_value = 350000.0  # Ratio: 35.0%
        directors_ratio = 50.0  # 50.0%, Corridor: [42.5%, 57.5%]

        result = Chapter123Engine.evaluate_conformance(
            assessed_value=assessed_value,
            true_value=true_value,
            directors_ratio=directors_ratio,
        )
        self.assertFalse(result.is_conforming)
        self.assertEqual(result.status, "UNDER_ASSESSED")
        self.assertFalse(result.tax_reduction_eligible)
        self.assertEqual(result.revised_assessment, assessed_value)

    def test_exact_corridor_boundaries(self):
        """Boundary tests: exact lower and upper limit equality must conform."""
        director_ratio = 0.50
        lower = 0.85 * director_ratio  # 0.425
        upper = 1.15 * director_ratio  # 0.575
        true_value = 100000.0

        # Exact lower limit
        res_lower = Chapter123Engine.evaluate_conformance(
            assessed_value=true_value * lower,
            true_value=true_value,
            directors_ratio=director_ratio,
        )
        self.assertTrue(res_lower.is_conforming)
        self.assertEqual(res_lower.status, "CONFORMING")

        # Exact upper limit
        res_upper = Chapter123Engine.evaluate_conformance(
            assessed_value=true_value * upper,
            true_value=true_value,
            directors_ratio=director_ratio,
        )
        self.assertTrue(res_upper.is_conforming)
        self.assertEqual(res_upper.status, "CONFORMING")

    def test_calculate_added_assessment(self):
        """Verifies calculation of post-rehab total and incremental added assessment."""
        base_assessment = 300000.0
        capex_amount = 100000.0
        equalization_ratio = 0.50  # 50%

        total_post_assessment = Chapter123Engine.calculate_added_assessment(
            base_assessment=base_assessment,
            capex_amount=capex_amount,
            equalization_ratio=equalization_ratio,
        )
        # Expected: $300,000 + ($100,000 * 0.50) = $350,000
        self.assertAlmostEqual(total_post_assessment, 350000.0, places=2)

        incremental = Chapter123Engine.calculate_incremental_added_assessment(
            capex_amount=capex_amount,
            equalization_ratio=equalization_ratio,
        )
        self.assertAlmostEqual(incremental, 50000.0, places=2)

        # Percentage equalization ratio format (50.0%)
        total_pct = Chapter123Engine.calculate_added_assessment(
            base_assessment=base_assessment,
            capex_amount=capex_amount,
            equalization_ratio=50.0,
        )
        self.assertAlmostEqual(total_pct, 350000.0, places=2)

    def test_invalid_arguments_raise_value_error(self):
        """Verifies input validation and exception handling."""
        with self.assertRaises(ValueError):
            Chapter123Engine.evaluate_conformance(-100.0, 500000.0, 50.0)
        with self.assertRaises(ValueError):
            Chapter123Engine.evaluate_conformance(100000.0, 0.0, 50.0)
        with self.assertRaises(ValueError):
            Chapter123Engine.evaluate_conformance(100000.0, 500000.0, -10.0)
        with self.assertRaises(ValueError):
            Chapter123Engine.calculate_added_assessment(-1000.0, 50000.0, 0.5)
        with self.assertRaises(ValueError):
            Chapter123Engine.calculate_added_assessment(100000.0, -500.0, 0.5)
        with self.assertRaises(ValueError):
            Chapter123Engine.calculate_added_assessment(100000.0, 50000.0, 0.0)


if __name__ == "__main__":
    unittest.main()
