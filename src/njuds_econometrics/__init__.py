"""NJUDS Computational Spatial Econometrics Lab.

Reference implementation of computational spatial econometrics, municipal equalization
modeling (N.J.S.A. Chapter 123), municipal rent control ordinances, PILOT and abatement
incentives (N.J.S.A. 40A:20 / 40A:21), assessment regressivity diagnostics (PRD/COD/G_tax),
multi-modal Scatter-Gather vision token reduction, and institutional underwriting algorithms.
"""

from .chapter123 import Chapter123Engine, ConformanceResult
from .underwriting import UnderwritingEngine
from .scatter_gather import ImageFeature, ScatterGatherSimulator
from .rent_control import (
    NJRentControlEngine,
    RentIncreaseEvaluation,
    CapitalImprovementSurchargeResult,
)
from .pilot_abatement import (
    NJPILOTEngine,
    PILOTComparisonResult,
    FiveYearPhaseInResult,
)
from .regressivity import (
    NJRegressivityEngine,
    RatioStudyDiagnostics,
)

__version__ = "1.1.0"
__author__ = "New Jersey Underwriting Data Systems (NJUDS) Computational Econometrics Research Lab"
__license__ = "MIT"

__all__ = [
    "Chapter123Engine",
    "ConformanceResult",
    "UnderwritingEngine",
    "ImageFeature",
    "ScatterGatherSimulator",
    "NJRentControlEngine",
    "RentIncreaseEvaluation",
    "CapitalImprovementSurchargeResult",
    "NJPILOTEngine",
    "PILOTComparisonResult",
    "FiveYearPhaseInResult",
    "NJRegressivityEngine",
    "RatioStudyDiagnostics",
]
