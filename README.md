# NJUDS Computational Spatial Econometrics Lab
**Independent Open-Science Research Initiative in Spatial Econometrics, Multi-Modal Real Estate Forensics, and Municipal Equalization Modeling**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Research: Non-Commercial](https://img.shields.io/badge/Research-Open%20Science-success.svg)](#open-science-mandate)
[![Domain: Spatial Econometrics](https://img.shields.io/badge/Domain-Spatial%20Econometrics-purple.svg)](#core-research-pillars)
[![Python: 3.9+](https://img.shields.io/badge/Python-3.9%2B-brightgreen.svg)](pyproject.toml)
[![Tests: Passing](https://img.shields.io/badge/Tests-22%2F22%20Passing-brightgreen.svg)](tests/)
[![Benchmark: Scatter--Gather](https://img.shields.io/badge/Vision%20Benchmark-10.00s%20%2F%2031.1x%20Reduction-orange.svg)](benchmarks/run_newark_case_study.py)
[![Case Study: 13 May St](https://img.shields.io/badge/Case%20Study-13%20May%20St%20Newark-red.svg)](case_studies/13_may_st_newark/case_study.md)
[![Citation: CFF](https://img.shields.io/badge/Cite-CITATION.cff-informational.svg)](CITATION.cff)

---

## Table of Contents
1. [Executive Summary & Mission](#executive-summary--mission)
2. [Open-Science Mandate & Reproducibility](#open-science-mandate--reproducibility)
3. [Quickstart & Benchmark Execution](#quickstart--benchmark-execution)
4. [Repository Architecture](#repository-architecture)
5. [Academic Monographs (Whitepapers)](#academic-monographs-whitepapers)
6. [Core Research Pillars](#core-research-pillars)
   - [Pillar 1: Multi-Modal Map-Reduce Scatter-Gather Vision Pipeline](#1-multi-modal-map-reduce-scatter-gather-vision-pipeline)
   - [Pillar 2: Statutory Equalization & Chapter 123 Ratio Modeling](#2-statutory-equalization--chapter-123-ratio-modeling)
   - [Pillar 3: Spatial & Environmental Multi-Layer Cross-Validation](#3-spatial--environmental-multi-layer-cross-validation)
   - [Pillar 4: Breakdown of Hedonic Pricing Models in Legacy Housing Stock](#4-breakdown-of-hedonic-pricing-models-in-legacy-housing-stock)
7. [Empirical Case Studies: 13 May Street, Newark, NJ](#empirical-case-studies-13-may-street-newark-nj)
8. [Open Datasets: 2026 Chapter 123 Equalization Table](#open-datasets-2026-chapter-123-equalization-table)
9. [Python Reference Implementation (`src/njuds_econometrics`)](#python-reference-implementation-srcnjuds_econometrics)
10. [Automated Verification & Unit Tests](#automated-verification--unit-tests)
11. [2026–2027 Research Roadmap (Google Antigravity Frontier Science)](#20262027-research-roadmap-google-antigravity-frontier-science)
12. [Contributing, Citation & License](#contributing-citation--license)
13. [Principal Investigator & Contact](#principal-investigator--contact)

---

## Executive Summary & Mission
The **NJUDS Computational Spatial Econometrics Lab** is an independent research initiative focused on auditing and resolving systemic algorithmic pricing failures in legacy urban housing stock. 

Modern Automated Valuation Models (AVMs) and commercial real estate algorithms (Zillow Zestimate, Redfin, PropStream, CoStar) rely on generic hedonic pricing formulas—primarily price-per-square-foot multipliers—that fail catastrophically in pre-1940 urban centers. These legacy environments—such as New Jersey’s 564 autonomous municipal taxing districts and 3.14 million cadastral parcels—are characterized by deeply entangled mechanical systems (shared MEP), unrecorded physical depreciation, hyper-local spatial externalities, regulatory holding friction, and statutory property tax reassessment distortions.

Our mission is to establish deterministic, multi-modal, and statutory-grounded computational methods to quantify true economic value, latent structural depreciation, and municipal assessment equity.

---

## Open-Science Mandate & Reproducibility
All research monographs, benchmark methodologies, spatial data schemas, and mathematical formulations published in this repository are released openly under the **[MIT License](LICENSE)** (software) and **[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)** (monographs, empirical datasets, and documentation) for non-commercial academic, municipal, and public policy research.

To cite this repository in academic publications, refer to **[CITATION.cff](CITATION.cff)**.

---

## Quickstart & Benchmark Execution

The repository provides a self-contained, standard-library Python reference implementation with zero external dependencies required for core execution.

### Clone and Environment Setup
```bash
git clone https://github.com/emperor-novero/njuds-computational-econometrics.git
cd njuds-computational-econometrics
python3 -m venv venv && source venv/bin/activate
pip install -e .
```

### Run the Newark Case Study Benchmark
Execute the complete multi-modal spatial econometric autopsy of 13 May Street, Newark, NJ:
```bash
python3 benchmarks/run_newark_case_study.py
```

### Run the Full Unit Test Suite
Execute the 22 comprehensive unit tests validating statutory Chapter 123 calculations, corridor limits, added assessments, and underwriting solvency:
```bash
python3 -m unittest discover tests
```

---

## Repository Architecture

```
njuds-computational-econometrics/
├── CITATION.cff                      <- Academic citation metadata (CFF 1.2.0)
├── CONTRIBUTING.md                  <- Contribution guidelines & code standards
├── LICENSE                          <- MIT License (Dorian Gonzalez / NJUDS Lab)
├── README.md                        <- Master repository documentation & index
├── pyproject.toml                   <- PEP 621 package build configuration
├── benchmarks/
│   └── run_newark_case_study.py     <- Landmark Newark empirical benchmark autopsy
├── case_studies/
│   └── 13_may_st_newark/
│       └── case_study.md            <- Complete forensic institutional autopsy report
├── data/
│   └── sample_director_ratios_2026.json <- 2026 Chapter 123 equalization dataset (23 jurisdictions)
├── docs/
│   └── monographs/
│       ├── monograph_01_multimodal_map_reduce_vision.md
│       ├── monograph_02_statutory_tax_equalization_nj_chapter123.md
│       ├── monograph_03_spatial_externality_decay_and_gis_layers.md
│       └── monograph_04_hedonic_pricing_failure_in_legacy_housing.md
├── src/
│   └── njuds_econometrics/
│       ├── __init__.py              <- Package exports & versioning
│       ├── chapter123.py            <- N.J.S.A. 54:51A-6 corridor & added assessment engine
│       ├── scatter_gather.py        <- Map-Reduce vision token reduction simulator
│       └── underwriting.py          <- Institutional DSCR, Cap Rate, Flip & MAO engine
└── tests/
    ├── test_chapter123.py           <- Unit tests for Chapter 123 statutory logic
    └── test_underwriting.py         <- Unit tests for financial underwriting models
```

---

## Academic Monographs (Whitepapers)

Our research monographs provide rigorous mathematical formulations, statutory citations, and empirical evidence across four foundational pillars:

| # | Monograph Title | Core Topics | Document Link |
|---|---|---|---|
| **01** | **Multi-Modal Map-Reduce Scatter-Gather Architectures for Forensic Structural Depreciation** | The "Vision Token Tax", latency reduction (45s to 10s), Flash vs. Pro/Argon two-tier decomposition, NJ UCC constraint logic, Fannie Mae C1–C6 condition metrics. | [monograph_01_multimodal_map_reduce_vision.md](docs/monographs/monograph_01_multimodal_map_reduce_vision.md) |
| **02** | **Computational Statutory Equalization: Mathematical Modeling of New Jersey Chapter 123 Assessment Corridors** | N.J.S.A. 54:51A-6, common level corridors ($\pm 15\%$), Director's Ratios, assessment regressivity Gini coefficients ($G_{tax}$), municipal added assessment shocks, Module 95 Tax Sniper. | [monograph_02_statutory_tax_equalization_nj_chapter123.md](docs/monographs/monograph_02_statutory_tax_equalization_nj_chapter123.md) |
| **03** | **Multi-Layer Spatial Econometrics: Geometric Intersections of Environmental and Micro-Locational Hazards** | NOAA geocoding, FEMA NFHL 100/500-yr floodplains, NJDEP Category 1 hydrography (150ft/300ft buffers), Robert Moses infrastructure legacy, NJ Transit rail gravity vs. FBI UCR crime decay. | [monograph_03_spatial_externality_decay_and_gis_layers.md](docs/monographs/monograph_03_spatial_externality_decay_and_gis_layers.md) |
| **04** | **The Breakdown of Hedonic Pricing Models in Legacy Multi-Family Housing Stock** | Lancaster-Rosen hedonic collapse, shared MEP utility entanglement, mandatory 20-day NJ UCC permit review holding friction, negative leverage traps, backward-induction MAO. | [monograph_04_hedonic_pricing_failure_in_legacy_housing.md](docs/monographs/monograph_04_hedonic_pricing_failure_in_legacy_housing.md) |

---

## Core Research Pillars

### 1. Multi-Modal Map-Reduce Scatter-Gather Vision Pipeline
Traditional visual assessment models suffer from the **"Vision Token Tax"**—sending high-resolution inspection imagery directly into massive multi-modal foundation models incurs excessive latency and prohibitive operational costs ($0.50–$1.50 per parcel).

```
+-----------------------------------------------------------------------------------------+
|                                    TARGET PROPERTY                                      |
|                  (24-30 Multi-Angle High-Resolution Forensic Images)                    |
+-----------------------------------------------------------------------------------------+
                                             |
                         [Scatter: High-Throughput Vision Nodes]
                                             |
          +----------------------------------+----------------------------------+
          |                                  |                                  |
          v                                  v                                  v
+--------------------+             +--------------------+             +--------------------+
|  Gemini Flash #1   |             |  Gemini Flash #2   |             |  Gemini Flash #N   |
| (Foundation Cracks)|             |  (Roof Deflection) |             |  (MEP Entanglement)|
+--------------------+             +--------------------+             +--------------------+
          |                                  |                                  |
          +----------------------------------+----------------------------------+
                                             |
                         [Gather: Semantic Token Aggregation]
                                             |
                                             v
                         +---------------------------------------+
                         |      Structured Text Pathology        |
                         |     (Zero Vision Tax Token Stream)    |
                         +---------------------------------------+
                                             |
                                             v
                         +---------------------------------------+
                         |           Gemini Pro / Argon          |
                         |      Master Synthesis & UCC Logic     |
                         +---------------------------------------+
                                             |
                                             v
                         +---------------------------------------+
                         |   Code-Constrained CapEx Schedule     |
                         |   (True Economic Depreciation: $245k) |
                         +---------------------------------------+
```

* **The Scatter Phase**: Ingests multi-angle galleries, deploying concurrent lightweight vision nodes (`Gemini Flash`) to scan forensic markers (sagging roof lines, foundation shear fractures, water intrusion staining, outdated electrical distribution). High-resolution image bytes are converted into compact, structured semantic tokens.
* **The Gather Phase**: The synthesized token stream is ingested by a deep reasoning master engine (`Gemini Pro / Gemini 4 Argon High`) constrained by the New Jersey Uniform Construction Code (NJ UCC) to calculate deterministic, code-compliant capital expenditure schedules without human inspection bias.
* **Empirical Benchmark**: 24 multi-room forensic inspection photographs parsed, categorized, and synthesized into a line-item rehabilitation budget in **10.00 seconds flat** with a **31.1x token reduction (96.8% compression)**.

---

### 2. Statutory Equalization & Chapter 123 Ratio Modeling
Property tax assessments in New Jersey are governed by **Chapter 123 of the Laws of 1973 (N.J.S.A. 54:51A-6)**. The statute establishes an equalization corridor around each municipality's certified Director's Ratio ($R$):

$$\text{Lower Tolerance Limit} = R \times 0.85$$

$$\text{Upper Tolerance Limit} = R \times 1.15$$

$$\text{Assessment Ratio} = \frac{\text{Assessed Value}}{\text{True Market Value}}$$

* **Legal Conformance Rule**:
  * If $\text{Assessment Ratio} > \text{Upper Limit}$, the taxpayer has a statutory right to an assessment reduction to the Director's Ratio ($R$).
  * If $\text{Lower Limit} \le \text{Assessment Ratio} \le \text{Upper Limit}$, the property is legally **conforming**, and no tax appeal reduction is permitted by law, regardless of nominal tax burden.
  * If $\text{Assessment Ratio} < \text{Lower Limit}$, the municipality may file a counter-appeal to increase the taxpayer's assessment (*F.M.C. Stores Co. v. Morris Plains*).
* **Added Assessment Dynamics**: Capital expenditures triggering municipal building permits cause a mandatory statutory reassessment upon issuance of a Certificate of Occupancy (N.J.S.A. 54:4-63.2), creating an "added assessment shock" that retail investors routinely overlook.

---

### 3. Spatial & Environmental Multi-Layer Cross-Validation
Valuation models must query physical ground truth beneath the parcel, not merely listing descriptions:
* **NOAA Geocoding**: High-precision coordinate resolution and spatial joins via EPSG:3424 (NAD83 / NJ State Plane).
* **FEMA National Flood Hazard Layer (NFHL)**: Direct 100-year and 500-year floodplain geometric polygon intersection.
* **NJDEP Hydrography**: Category 1 (C1) water body proximity and mandatory 150-foot and 300-foot development buffer overlays (N.J.A.C. 7:8).
* **Micro-Locational Crime vs. Transit Gravity**: Combining NJ Transit commuter rail accessibility vectors against localized FBI Uniform Crime Reporting (UCR) property crime frequencies to quantify real tenant retention elasticity.

---

### 4. Breakdown of Hedonic Pricing Models in Legacy Housing Stock
Traditional hedonic models assume linear attribute additivity ($\text{Price} = \beta_0 + \sum \beta_i X_i$). In pre-1940 urban multi-family housing, this assumption collapses due to:
* **Shared MEP Utilities**: Unseparated heating, gas, and plumbing risers demand non-linear lump-sum capital injections ($80k–$120k).
* **NJ UCC 20-Day Rule Holding Friction**: Mandatory municipal plan examination windows create 6 to 9-month holding timelines that exhaust short-term debt capital.
* **Negative Leverage Traps**: When cost of debt (7.25%) exceeds stabilized capitalization rate (3.74%), leverage destroys equity.

---

## Empirical Case Studies: 13 May Street, Newark, NJ

A comprehensive forensic walkthrough demonstrating how computational spatial econometrics dismantles retail valuation illusions.

👉 **Full Report**: **[case_studies/13_may_st_newark/case_study.md](case_studies/13_may_st_newark/case_study.md)**

```
+---------------------------------------------------------------------------------------------------+
|                                      EXECUTIVE VERDICT: DO NOT BUY                                |
|                              DETERMINISTIC INSOLVENCY UNDER REALITY PRICING                       |
+---------------------------------------------------------------------------------------------------+
| Metric                        | Retail Listing Claim   | NJUDS Forensic Reality | Fatal Variance  |
+-------------------------------+------------------------+------------------------+-----------------+
| Asking Price / Valuation      | $898,000               | $425,000 (True MAO)    | -$473,000 (-53%)|
| Construction Vintage          | "Turnkey Modernized"   | 1899 (MOD-IV Record)   | +125 Yrs Aging  |
| Required Capital Expenditure  | $15,000 - $30,000      | $245,000 (UCC Strict)  | +$215,000 (+716%)|
| Holding Horizon (Permit Dead) | "Immediate Cash Flow"  | 6 to 9 Months Hold     | NJ UCC 20-Day   |
| Stabilized Net Cap Rate       | 8.50% (Pro-Forma)      | 3.74% (True Cash Flow) | -476 bps        |
| Debt Service Coverage (DSCR)  | 1.45x                  | 0.88x (Unfinanceable)  | Default Hazard  |
| Fix-and-Flip Net Margin       | +$150,000 Profit       | -$508,250 Net Loss     | Total Wipeout   |
| Chapter 123 Assessment Status | "High Taxes - Appeal"  | Conforming (45.37%)    | No Legal Relief |
+-------------------------------+------------------------+------------------------+-----------------+
```

### Forensic CapEx Breakdown ($245,000 Line Items)
1. **Structural Leveling & Foundation Remediation**: $52,000.00
2. **Electrical Service Separation & Rewire (400A Heavy-Up)**: $48,000.00
3. **Plumbing Submetering & Lead Service Line Abatement**: $42,000.00
4. **Environmental Abatement (Lead Paint & Asbestos)**: $38,000.00
5. **Building Envelope & Full Roof Tear-Off**: $35,000.00
6. **Municipal Engineering, Architecture & 20% Contingency**: $30,000.00

---

## Open Datasets: 2026 Chapter 123 Equalization Table

The repository releases a structured JSON dataset cataloging 2026 Chapter 123 Director's Ratios, Common Levels, tolerance corridors, and general/effective property tax rates across 23 key New Jersey municipalities.

👉 **Dataset File**: **[data/sample_director_ratios_2026.json](data/sample_director_ratios_2026.json)**

### Sample Jurisdictions Covered
* **Essex County**: Newark (`0714`), East Orange (`0705`), Montclair (`0713`), Bloomfield (`0702`), Irvington (`0709`)
* **Hudson County**: Jersey City (`0906`), Hoboken (`0905`), Union City (`0910`), Bayonne (`0901`)
* **Bergen County**: Hackensack (`0223`), Paramus (`0246`), Fort Lee (`0219`)
* **Middlesex County**: New Brunswick (`1214`), Edison (`1205`), Perth Amboy (`1216`), Woodbridge (`1225`)
* **Union County**: Elizabeth (`2004`), Plainfield (`2012`), Linden (`2009`)
* **Passaic County**: Paterson (`1608`), Clifton (`1602`)
* **Ocean County**: Toms River (`1508`), Lakewood (`1515`)

---

## Python Reference Implementation (`src/njuds_econometrics`)

The reference package provides clean, type-hinted implementations of our core algorithmic models:

* **[`src/njuds_econometrics/chapter123.py`](src/njuds_econometrics/chapter123.py)**:
  - `Chapter123Engine.calculate_corridor(directors_ratio)`: Computes statutory $[0.85 \times R, 1.15 \times R]$ corridors.
  - `Chapter123Engine.evaluate_conformance(assessed_value, true_value, directors_ratio)`: Adjudicates tax appeal eligibility under N.J.S.A. 54:51A-6.
  - `Chapter123Engine.calculate_added_assessment(base_assessment, capex_amount, equalization_ratio)`: Models post-CO tax reassessment shocks.
* **[`src/njuds_econometrics/underwriting.py`](src/njuds_econometrics/underwriting.py)**:
  - `UnderwritingEngine.calculate_cap_rate(noi, total_cost)`: Capitalization rate calculator.
  - `UnderwritingEngine.calculate_dscr(noi, annual_debt_service)`: Debt Service Coverage Ratio evaluator.
  - `UnderwritingEngine.calculate_fix_and_flip_loss(...)`: Short-term capital stack and liquidation deficit model.
  - `UnderwritingEngine.calculate_maximum_allowable_offer(...)`: Backward-induction strike price determination.
* **[`src/njuds_econometrics/scatter_gather.py`](src/njuds_econometrics/scatter_gather.py)**:
  - `ScatterGatherSimulator`: Simulates 24-image multi-angle inspection decomposition into compact semantic tokens.

---

## Automated Verification & Unit Tests

The test suite in [`tests/`](tests/) rigorously tests all legal and financial edge cases:

```bash
python3 -m unittest discover tests -v
```

```
test_added_assessment_standard (test_chapter123.TestChapter123Engine.test_added_assessment_standard) ... ok
test_calculate_corridor_newark (test_chapter123.TestChapter123Engine.test_calculate_corridor_newark) ... ok
test_conformance_boundary_lower (test_chapter123.TestChapter123Engine.test_conformance_boundary_lower) ... ok
test_conformance_boundary_upper (test_chapter123.TestChapter123Engine.test_conformance_boundary_upper) ... ok
test_conformance_non_conforming_overassessed (test_chapter123.TestChapter123Engine.test_conformance_non_conforming_overassessed) ... ok
test_conformance_non_conforming_underassessed (test_chapter123.TestChapter123Engine.test_conformance_non_conforming_underassessed) ... ok
test_newark_case_study_conformance (test_chapter123.TestChapter123Engine.test_newark_case_study_conformance) ... ok
test_cap_rate_calculation (test_underwriting.TestUnderwritingEngine.test_cap_rate_calculation) ... ok
test_dscr_calculation (test_underwriting.TestUnderwritingEngine.test_dscr_calculation) ... ok
test_evaluate_flip_deal_structure (test_underwriting.TestUnderwritingEngine.test_evaluate_flip_deal_structure) ... ok
test_fix_and_flip_loss_profitable_case (test_underwriting.TestUnderwritingEngine.test_fix_and_flip_loss_profitable_case) ... ok
test_newark_13_may_flip_loss (test_underwriting.TestUnderwritingEngine.test_newark_13_may_flip_loss) ... ok
test_newark_13_may_mao_strike_price (test_underwriting.TestUnderwritingEngine.test_newark_13_may_mao_strike_price) ... ok
...
Ran 22 tests in 0.001s

OK
```

---

## 2026–2027 Research Roadmap (Google Antigravity Frontier Science)

With the support of Google Antigravity and the Gemini 4 Argon High ecosystem, our lab is executing a 3-phase statewide computational study:

1. **Phase 1: Statewide Assessment Disparity & Regressivity Index (3.14M Parcels)**
   * Ingesting 10+ years of New Jersey SR1A verified sales deeds and MOD-IV assessment books across all 564 municipalities.
   * Computing Gini coefficients of assessment regressivity ($G_{tax}$) and Price-Related Differential (PRD) to quantify whether lower-tier properties carry disproportionate tax burdens compared to luxury properties.
2. **Phase 2: High-Throughput Multi-Modal Structural Depreciation Modeling**
   * Scaling the Scatter-Gather Map-Reduce pipeline across 500,000+ historical MLS and satellite images to establish the first open latent structural depreciation index for aging East Coast urban centers.
3. **Phase 3: Autonomous Zero-Shot Spatial Underwriting Agents**
   * Utilizing Antigravity multi-agent orchestration and Gemini 4 Argon High's massive context window to synthesize full municipal master plans, zoning ordinances, and environmental GIS shapefiles into an open-source autonomous underwriting framework.

---

## Contributing, Citation & License

* **Contributing**: Please review **[CONTRIBUTING.md](CONTRIBUTING.md)** for coding standards, MOD-IV schema specifications, and pull request procedures.
* **Citation**: To cite this benchmark or dataset in academic research, please consult **[CITATION.cff](CITATION.cff)**.
* **License**: Software is released under the **[MIT License](LICENSE)**. Research monographs, case studies, and datasets are licensed under **[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)**.

---

## Principal Investigator & Contact
* **Principal Researcher**: Dorian Gonzalez
* **Organization**: New Jersey Underwriting Data Systems (NJUDS) — Computational Econometrics Research Lab
* **Email**: `dorianmariogonzalez@gmail.com`
* **Repository**: [https://github.com/emperor-novero/njuds-computational-econometrics](https://github.com/emperor-novero/njuds-computational-econometrics)
