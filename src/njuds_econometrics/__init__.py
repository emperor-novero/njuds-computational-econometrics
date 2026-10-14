"""NJUDS Computational Spatial Econometrics Lab.

Reference implementation of computational spatial econometrics, municipal equalization
modeling (N.J.S.A. Chapter 123), multi-modal Scatter-Gather vision token reduction,
and institutional underwriting algorithms.
"""

from .chapter123 import Chapter123Engine, ConformanceResult
from .underwriting import UnderwritingEngine
from .scatter_gather import ImageFeature, ScatterGatherSimulator

__version__ = "1.0.0"
__author__ = "New Jersey Underwriting Data Systems (NJUDS) Computational Econometrics Research Lab"
__license__ = "MIT"

__all__ = [
    "Chapter123Engine",
    "ConformanceResult",
    "UnderwritingEngine",
    "ImageFeature",
    "ScatterGatherSimulator",
]
