# NJUDS Computational Spatial Econometrics Lab
**Independent Open-Science Research Initiative in Spatial Econometrics, Multi-Modal Real Estate Forensics, and Municipal Equalization Modeling**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Research: Non-Commercial](https://img.shields.io/badge/Research-Open%20Science-success.svg)](#open-science-mandate)
[![Domain: Spatial Econometrics](https://img.shields.io/badge/Domain-Spatial%20Econometrics-purple.svg)](#core-research-pillars)
[![Python: 3.9+](https://img.shields.io/badge/Python-3.9%2B-brightgreen.svg)](pyproject.toml)
[![Tests: Passing](https://img.shields.io/badge/Tests-38%2F38%20Passing-brightgreen.svg)](tests/)
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
│       ├── case_study.md            <- Complete forensic institutional autopsy report
│       └── 13_May_Street_Newark_Institutional_Report.pdf <- Original 10-page production underwriting PDF (05/29/2026)
├── artifacts/
│   └── reports/                     <- Production institutional underwriting PDFs (Feb–May 2026 across 8 NJ municipalities)
├── data/
│   └── sample_director_ratios_2026.json <- 2026 Chapter 123 equalization dataset (23 jurisdictions)
├── docs/
│   └── monographs/
│       ├── monograph_01_multimodal_map_reduce_vision.md
│       ├── monograph_02_statutory_tax_equalization_nj_chapter123.md
│       ├── monograph_03_spatial_externality_decay_and_gis_layers.md
│       ├── monograph_04_hedonic_pricing_failure_in_legacy_housing.md
│       └── monograph_05_municipal_fiscal_regressivity_pilot_and_rent_control.md
├── src/
│   └── njuds_econometrics/
│       ├── __init__.py              <- Package exports & versioning
│       ├── chapter123.py            <- N.J.S.A. 54:51A-6 corridor & added assessment engine
│       ├── pilot_abatement.py       <- N.J.S.A. 40A:20 PILOT ASC & 40A:21 5-yr abatement engine
│       ├── regressivity.py          <- IAAO PRD, COD, and G_tax ratio study diagnostics
│       ├── rent_control.py          <- NJ municipal rent leveling & CPI margin compression
│       ├── scatter_gather.py        <- Map-Reduce vision token reduction simulator
│       └── underwriting.py          <- Institutional DSCR, Cap Rate, Flip & MAO engine
└── tests/
    ├── test_chapter123.py           <- Unit tests for Chapter 123 statutory logic
    ├── test_pilot_abatement.py      <- Unit tests for PILOT & 5-year phase-in models
    ├── test_regressivity.py         <- Unit tests for PRD, COD, and tax Gini equity
    ├── test_rent_control.py         <- Unit tests for municipal rent control limits
    └── test_underwriting.py         <- Unit tests for financial underwriting models
```

---

## Academic Monographs (Whitepapers)

Our research monographs provide rigorous mathematical formulations, statutory citations, and empirical evidence across five foundational pillars:

| # | Monograph Title | Core Topics | Document Link |
|---|---|---|---|
| **01** | **Multi-Modal Map-Reduce Scatter-Gather Architectures for Forensic Structural Depreciation** | The "Vision Token Tax", latency reduction (45s to 10s), Flash vs. Pro/Argon two-tier decomposition, NJ UCC constraint logic, Fannie Mae C1–C6 condition metrics. | [monograph_01_multimodal_map_reduce_vision.md](docs/monographs/monograph_01_multimodal_map_reduce_vision.md) |
| **02** | **Computational Statutory Equalization: Mathematical Modeling of New Jersey Chapter 123 Assessment Corridors** | N.J.S.A. 54:51A-6, common level corridors ($\pm 15\%$), Director's Ratios, assessment regressivity Gini coefficients ($`G_{\text{tax}}`$), municipal added assessment shocks, Module 95 Tax Sniper. | [monograph_02_statutory_tax_equalization_nj_chapter123.md](docs/monographs/monograph_02_statutory_tax_equalization_nj_chapter123.md) |
| **03** | **Multi-Layer Spatial Econometrics: Geometric Intersections of Environmental and Micro-Locational Hazards** | NOAA geocoding, FEMA NFHL 100/500-yr floodplains, NJDEP Category 1 hydrography (150ft/300ft buffers), Robert Moses infrastructure legacy, NJ Transit rail gravity vs. FBI UCR crime decay. | [monograph_03_spatial_externality_decay_and_gis_layers.md](docs/monographs/monograph_03_spatial_externality_decay_and_gis_layers.md) |
| **04** | **The Breakdown of Hedonic Pricing Models in Legacy Multi-Family Housing Stock** | Lancaster-Rosen hedonic collapse, shared MEP utility entanglement, mandatory 20-day NJ UCC permit review holding friction, negative leverage traps, backward-induction MAO. | [monograph_04_hedonic_pricing_failure_in_legacy_housing.md](docs/monographs/monograph_04_hedonic_pricing_failure_in_legacy_housing.md) |
| **05** | **Fiscal Urban Econometrics: Long-Term Tax Abatements (PILOT), Municipal Rent Control, and Statewide Assessment Regressivity** | N.J.S.A. 40A:20 PILOT ASC formulas, 95/5 municipal-county revenue splits (0% school allocation), Inganamort v. Fort Lee municipal rent caps, CPI stagflationary margin compression, IAAO PRD/COD/G_tax standards. | [monograph_05_municipal_fiscal_regressivity_pilot_and_rent_control.md](docs/monographs/monograph_05_municipal_fiscal_regressivity_pilot_and_rent_control.md) |

---

## Core Research Pillars

### 1. Multi-Modal Map-Reduce Scatter-Gather Vision Pipeline
Traditional visual assessment models suffer from the **"Vision Token Tax"**—sending high-resolution inspection imagery directly into massive multi-modal foundation models incurs excessive latency and prohibitive operational costs (\$0.50–\$1.50 per parcel).

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
                         |   (True Economic Depreciation: \$245k) |
                         +---------------------------------------+
```

* **The Scatter Phase**: Ingests multi-angle galleries, deploying concurrent lightweight vision nodes (`Gemini Flash`) to scan forensic markers (sagging roof lines, foundation shear fractures, water intrusion staining, outdated electrical distribution). High-resolution image bytes are converted into compact, structured semantic tokens.
* **The Gather Phase**: The synthesized token stream is ingested by a deep reasoning master engine (`Gemini Pro / Gemini 4 Argon High`) constrained by the New Jersey Uniform Construction Code (NJ UCC) to calculate deterministic, code-compliant capital expenditure schedules without human inspection bias.
* **Empirical Benchmark**: 24 multi-room forensic inspection photographs parsed, categorized, and synthesized into a line-item rehabilitation budget in **10.00 seconds flat** with a **31.1x token reduction (96.8% compression)**.

---

### 2. Statutory Equalization & Chapter 123 Ratio Modeling
Property tax assessments in New Jersey are governed by **Chapter 123 of the Laws of 1973 (N.J.S.A. 54:51A-6)**. The statute establishes an equalization corridor around each municipality's certified Director's Ratio ($`R`$):

$$
\text{Lower Tolerance Limit} = R \times 0.85
$$

$$
\text{Upper Tolerance Limit} = R \times 1.15
$$

$$
\text{Assessment Ratio} = \frac{\text{Assessed Value}}{\text{True Market Value}}
$$

* **Legal Conformance Rule**:
  * If $`\text{Assessment Ratio} > \text{Upper Limit}`$, the taxpayer has a statutory right to an assessment reduction to the Director's Ratio ($`R`$).
  * If $`\text{Lower Limit} \le \text{Assessment Ratio} \le \text{Upper Limit}`$, the property is legally **conforming**, and no tax appeal reduction is permitted by law, regardless of nominal tax burden.
  * If $`\text{Assessment Ratio} < \text{Lower Limit}`$, the municipality may file a counter-appeal to increase the taxpayer's assessment (*F.M.C. Stores Co. v. Morris Plains*).
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
Traditional hedonic models assume linear attribute additivity ($`\text{Price} = \beta_0 + \sum \beta_i X_i`$). In pre-1940 urban multi-family housing, this assumption collapses due to:
* **Shared MEP Utilities**: Unseparated heating, gas, and plumbing risers demand non-linear lump-sum capital injections (\$80k–\$120k).
* **NJ UCC 20-Day Rule Holding Friction**: Mandatory municipal plan examination windows create 6 to 9-month holding timelines that exhaust short-term debt capital.
* **Negative Leverage Traps**: When cost of debt (7.25%) exceeds stabilized capitalization rate (3.74%), leverage destroys equity.

---

### 5. Municipal Rent Regulation, PILOT Tax Arbitrage & Assessment Regressivity
Urban New Jersey housing dynamics cannot be understood through unconstrained market models:
* **Municipal Rent Leveling Ordinances**: Under *Inganamort v. Fort Lee* (1973), municipalities enforce local CPI caps (e.g. Newark Title XIX 5.0% cap, Jersey City Ch. 260 4.0% cap) and 50% substantial rehabilitation exemptions. Operating expense inflation (6–9%) outpacing capped rent increases causes multi-year NOI margin compression.
* **Long-Term Tax Exemption (PILOT / N.J.S.A. 40A:20)**: Replaces ad valorem taxes with Annual Service Charges (ASC, 10–15% of AGR), creating multi-million dollar equity shields while establishing a 95% municipal / 5% county / 0% school district revenue split.
* **Assessment Regressivity & Uniformity**: Incorporating IAAO standards to compute Price-Related Differential ($PRD > 1.03$ indicates regressive taxation where lower-value homes carry higher effective ratios) and Coefficient of Dispersion ($COD > 15\%$ indicates horizontal inequity).

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
| Asking Price / Valuation      | \$898,000              | \$425,000 (True MAO)   | -\$473,000 (-53%)|
| Construction Vintage          | "Turnkey Modernized"   | 1899 (MOD-IV Record)   | +125 Yrs Aging  |
| Required Capital Expenditure  | \$15,000 - \$30,000     | \$245,000 (UCC Strict) | +\$215,000 (+716%)|
| Holding Horizon (Permit Dead) | "Immediate Cash Flow"  | 6 to 9 Months Hold     | NJ UCC 20-Day   |
| Stabilized Net Cap Rate       | 8.50% (Pro-Forma)      | 3.74% (True Cash Flow) | -476 bps        |
| Debt Service Coverage (DSCR)  | 1.45x                  | 0.88x (Unfinanceable)  | Default Hazard  |
| Fix-and-Flip Net Margin       | +\$150,000 Profit      | -\$508,250 Net Loss    | Total Wipeout   |
| Chapter 123 Assessment Status | "High Taxes - Appeal"  | Conforming (45.37%)    | No Legal Relief |
+-------------------------------+------------------------+------------------------+-----------------+
```

### Forensic CapEx Breakdown (\$245,000 Line Items)
1. **Structural Leveling & Foundation Remediation**: \$52,000.00
2. **Electrical Service Separation & Rewire (400A Heavy-Up)**: \$48,000.00
3. **Plumbing Submetering & Lead Service Line Abatement**: \$42,000.00
4. **Environmental Abatement (Lead Paint & Asbestos)**: \$38,000.00
5. **Building Envelope & Full Roof Tear-Off**: \$35,000.00
6. **Municipal Engineering, Architecture & 20% Contingency**: \$30,000.00

> [!TIP]
> **Primary Case Study PDF Artifact**:  
> The original 10-page production underwriting PDF generated on May 29, 2026 is published directly in the case study directory:  
> 📄 **[Download 13_May_Street_Newark_Institutional_Report.pdf](case_studies/13_may_st_newark/13_May_Street_Newark_Institutional_Report.pdf)**

---

## Empirical Ground Truth Artifacts: Production Underwriting PDFs

To provide unforgeable empirical evidence and eliminate reliance on synthetic or simulated outputs, this repository includes genuine, production-generated institutional underwriting reports produced by the NJUDS Engine (v1.2 Hudson) between February and June 2026. 

Each report represents an actual multi-page algorithmic forensic autopsy querying New Jersey municipal MOD-IV records, PAMS-PIN identifiers, Chapter 123 equalization ratios, and multi-modal photographic decay audits:

| Property Address | Municipality / County | Production Date | Pages | Primary Algorithmic Finding | Production Artifact |
|---|---|---|---|---|---|
| **13 May Street** | Newark (Essex) | May 29, 2026 | 10 | Landmark Case Study (\$245k CapEx, 0.88 DSCR, 45.37% Conforming Tax) | [📄 View PDF](case_studies/13_may_st_newark/13_May_Street_Newark_Institutional_Report.pdf) |
| **114 Graham Street** | Jersey City (Hudson) | April 20, 2026 | 8 | Structural Settlement & Soil Mechanics Forensic Audit | [📄 View PDF](artifacts/reports/114_Graham_Street_Jersey_City_04_20_2026.pdf) |
| **169 Walnut Street** | Bloomfield (Essex) | April 24, 2026 | 9 | Transit Gravity vs. Aging Submetering Deficit | [📄 View PDF](artifacts/reports/169_Walnut_Street_Bloomfield_04_24_2026.pdf) |
| **241 Osborne Terrace** | Newark (Essex) | May 8, 2026 | 9 | Chapter 123 Reassessment Boundary & Asbestos Friction | [📄 View PDF](artifacts/reports/241_Osborne_Ter_Newark_05_08_2026.pdf) |
| **267 Townsend Street** | New Brunswick (Middlesex) | May 5, 2026 | 10 | Student Housing Multi-Family Utility Separation Audit | [📄 View PDF](artifacts/reports/267_Townsend_Street_New_Brunswick_05_05_2026.pdf) |
| **385 Washington Street** | Perth Amboy (Middlesex) | May 14, 2026 | 7 | Category 1 Hydrography & Coastal Riparian Zoning Overlay | [📄 View PDF](artifacts/reports/385_Washington_Street_Perth_Amboy_05_14_2026.pdf) |
| **55 Smith Street** | Perth Amboy (Middlesex) | Feb 24, 2026 | 9 | Commercial Mixed-Use Environmental & MEP Split | [📄 View PDF](artifacts/reports/55_Smith_Street_Perth_Amboy_02_24_2026.pdf) |
| **71 Lindsley Avenue** | Newark (Essex) | March 2, 2026 | 9 | Foundation Lateral Shear & Roof Deflection Audit | [📄 View PDF](artifacts/reports/71_Lindsley_Avenue_Newark_03_02_2026.pdf) |
| **157 Westfield Avenue** | Clark (Union) | March 1, 2026 | 8 | Suburban Equalization Corridor Non-Conformance | [📄 View PDF](artifacts/reports/157_Westfield_Avenue_Clark_03_01_2026.pdf) |

### Longitudinal Engine Lineage (February – October 2026)

The chronological progression across these production artifacts documents the verifiable architectural maturation of the NJUDS underwriting intelligence over multi-month production deployments:

| Engine Version | Release Window | Codename | Core Innovation & Structural Milestone | Report Footprint |
|---|---|---|---|---|
| **v0.82 – v0.9** | February – Early March 2026 | **Verrazzano** | Initial multi-modal Map-Reduce photo ingestion (Gemini Flash vision parsing in 10.00s); baseline single-verdict pass/fail risk scoring. | 6 Pages (e.g., `55 Smith St`, `71 Lindsley Ave`) |
| **v1.0** | Mid – Late March 2026 | **Hudson V1** | Introduction of dual-strategy exit stress-testing (`DO NOT BUY (HOLD)` vs `DO NOT BUY (FLIP)`); preliminary environmental zoning overlays. | 7 Pages (e.g., `197 Park Pl`) |
| **v1.1** | April 2026 | **Hudson V1.1** | Full NJ UCC construction code subcode integration; line-item structural & MEP capital expenditure schedules; 20-day plan review holding decay models. | 8–9 Pages (e.g., `114 Graham St`, `169 Walnut St`) |
| **v1.2** | May – June 2026 | **Hudson V1.2** | Statutory Chapter 123 Director's Ratio integration; post-Certificate of Occupancy added assessment shocks; deterministic Maximum Allowable Offer (MAO) backward induction. | 10 Pages (e.g., `13 May St Newark`, `267 Townsend St`) |
| **v2.0 (Frontier)** | Fall 2026 – Present | **Sovereign** | Migration to dedicated Oracle Cloud Infrastructure (OCI); state-wide 3.14M parcel spatial graph; multi-agent autonomous swarms (`Chain of Gemini`); Google Antigravity Frontier Science integration. | Full Statewide Benchmark & Spatial Graph |

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
  - `Chapter123Engine.calculate_corridor(directors_ratio)`: Computes statutory $`[0.85 \times R, 1.15 \times R]`$ corridors.
  - `Chapter123Engine.evaluate_conformance(assessed_value, true_value, directors_ratio)`: Adjudicates tax appeal eligibility under N.J.S.A. 54:51A-6.
  - `Chapter123Engine.calculate_added_assessment(base_assessment, capex_amount, equalization_ratio)`: Models post-CO tax reassessment shocks.
* **[`src/njuds_econometrics/rent_control.py`](src/njuds_econometrics/rent_control.py)**:
  - `NJRentControlEngine.evaluate_allowable_increase(...)`: Evaluates municipal CPI caps, statutory maximums, and owner-occupancy exclusions (Newark, Jersey City, Hoboken).
  - `NJRentControlEngine.calculate_capital_improvement_surcharge(...)`: Amortized major CapEx pass-through schedules capped at 15% of base rent.
  - `NJRentControlEngine.simulate_rent_control_margin_compression(...)`: Multi-year NOI decay simulation under inflation.
* **[`src/njuds_econometrics/pilot_abatement.py`](src/njuds_econometrics/pilot_abatement.py)**:
  - `NJPILOTEngine.evaluate_pilot_agreement(...)`: Models N.J.S.A. 40A:20 Annual Service Charges (ASC on AGR or TPC), land tax credits, and the statutory 95/5 municipal-county revenue split.
  - `NJPILOTEngine.calculate_five_year_abatement_schedule(...)`: N.J.S.A. 40A:21 statutory 0%-20%-40%-60%-80% phase-in tax schedules.
  - `NJPILOTEngine.calculate_pilot_net_present_value(...)`: Discounted cash flow valuation of long-term abatement tax shields.
* **[`src/njuds_econometrics/regressivity.py`](src/njuds_econometrics/regressivity.py)**:
  - `NJRegressivityEngine.calculate_prd(...)`: Price-Related Differential assessing vertical regressivity ($PRD > 1.03$).
  - `NJRegressivityEngine.calculate_cod(...)`: Coefficient of Dispersion measuring horizontal assessment uniformity ($COD \le 15\%$).
  - `NJRegressivityEngine.calculate_tax_gini(...)`: Assessment Regressivity Gini coefficient ($G_{\text{tax}}$).
  - `NJRegressivityEngine.evaluate_ratio_study(...)`: Full IAAO ratio study diagnostics and compliance verdicts.
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
test_five_year_abatement_schedule (test_pilot_abatement.TestNJPILOTEngine.test_five_year_abatement_schedule) ... ok
test_pilot_net_present_value (test_pilot_abatement.TestNJPILOTEngine.test_pilot_net_present_value) ... ok
test_standard_pilot_vs_conventional_tax (test_pilot_abatement.TestNJPILOTEngine.test_standard_pilot_vs_conventional_tax) ... ok
test_assessment_gini_coefficient (test_regressivity.TestNJRegressivityEngine.test_assessment_gini_coefficient) ... ok
test_high_dispersion_horizontal_inequity (test_regressivity.TestNJRegressivityEngine.test_high_dispersion_horizontal_inequity) ... ok
test_regressive_distribution_detection (test_regressivity.TestNJRegressivityEngine.test_regressive_distribution_detection) ... ok
test_capital_improvement_surcharge_approval (test_rent_control.TestNJRentControlEngine.test_capital_improvement_surcharge_approval) ... ok
test_jersey_city_cpi_cap (test_rent_control.TestNJRentControlEngine.test_jersey_city_cpi_cap) ... ok
test_newark_cpi_above_cap (test_rent_control.TestNJRentControlEngine.test_newark_cpi_above_cap) ... ok
test_newark_13_may_flip_loss (test_underwriting.TestUnderwritingEngine.test_newark_13_may_flip_loss) ... ok
test_newark_13_may_mao_strike_price (test_underwriting.TestUnderwritingEngine.test_newark_13_may_mao_strike_price) ... ok
...
Ran 38 tests in 0.002s

OK
```

---

## 2026–2027 Research Roadmap (Google Antigravity Frontier Science)

With the support of Google Antigravity and the Gemini 4 Argon High ecosystem, our lab is executing a 3-phase statewide computational study:

1. **Phase 1: Statewide Assessment Disparity & Regressivity Index (3.14M Parcels)**
   * Ingesting 10+ years of New Jersey SR1A verified sales deeds and MOD-IV assessment books across all 564 municipalities.
   * Computing Gini coefficients of assessment regressivity ($`G_{\text{tax}}`$) and Price-Related Differential (PRD) to quantify whether lower-tier properties carry disproportionate tax burdens compared to luxury properties.
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
