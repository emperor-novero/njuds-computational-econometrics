# NJUDS Computational Spatial Econometrics Lab
**Independent Open-Science Research Initiative in Spatial Econometrics, Multi-Modal Real Estate Forensics, and Municipal Equalization Modeling**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Research: Non-Commercial](https://img.shields.io/badge/Research-Open%20Science-success.svg)](#open-science-mandate)
[![Domain: Spatial Econometrics](https://img.shields.io/badge/Domain-Spatial%20Econometrics-purple.svg)](#core-research-pillars)

---

## Executive Summary & Mission
The **NJUDS Computational Spatial Econometrics Lab** is an independent research initiative focused on auditing and resolving systemic algorithmic pricing failures in legacy urban housing stock. 

Modern Automated Valuation Models (AVMs) and retail real estate algorithms rely on generic hedonic pricing formulas (price-per-square-foot multipliers) that fail catastrophically in pre-1940 urban centers. These legacy environments—such as New Jersey’s 564 autonomous municipal taxing districts and 3.14 million parcels—are characterized by deeply entangled mechanical systems (shared MEP), unrecorded physical depreciation, hyper-local spatial externalities, and statutory property tax reassessment distortions.

Our mission is to establish deterministic, multi-modal, and statutory-grounded computational methods to quantify true economic value, latent structural depreciation, and municipal assessment equity.

---

## Open-Science Mandate
All research papers, benchmark methodologies, spatial data schemas, and mathematical formulations published in this repository are released openly under the **MIT License** and **Creative Commons Attribution 4.0 International (CC BY 4.0)** for non-commercial academic, municipal, and public policy research. 

---

## Core Research Pillars

### 1. Multi-Modal Map-Reduce Scatter-Gather Vision Pipeline
Traditional visual assessment models suffer from the "Vision Token Tax"—sending high-resolution inspection imagery directly into massive multi-modal foundation models incurs excessive latency and prohibitive operational costs.

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
* **Empirical Benchmark**: 24 multi-room forensic inspection photographs parsed, categorized, and synthesized into a line-item rehabilitation budget in **10.00 seconds flat**.

---

### 2. Statutory Equalization & Chapter 123 Ratio Modeling
Property tax assessments in New Jersey are governed by **Chapter 123 of the Laws of 1973 (N.J.S.A. 54:51A-6)**. The statute establishes an equalization corridor around each municipality's Director's Ratio:

$$\text{Lower Limit} = \text{Director's Ratio} \times 0.85$$

$$\text{Upper Limit} = \text{Director's Ratio} \times 1.15$$

$$\text{Assessment Ratio} = \frac{\text{Assessed Value}}{\text{True Market Value}}$$

* **Legal Conformance Rule**:
  * If $\text{Assessment Ratio} > \text{Upper Limit}$, the taxpayer has a statutory right to an assessment reduction to the Director's Ratio.
  * If $\text{Lower Limit} \le \text{Assessment Ratio} \le \text{Upper Limit}$, the property is legally **conforming**, and no tax appeal reduction is permitted by law, regardless of nominal tax burden.
* **Added Assessment Dynamics**: Capital expenditures triggering municipal building permits cause a mandatory statutory reassessment upon issuance of a Certificate of Occupancy, creating an "added assessment shock" that retail investors routinely overlook.

---

### 3. Spatial & Environmental Multi-Layer Cross-Validation
Valuation models must query physical ground truth beneath the parcel, not merely listing descriptions:
* **NOAA Geocoding**: High-precision coordinate resolution.
* **FEMA National Flood Hazard Layer (NFHL)**: Direct 100-year and 500-year floodplain geometric intersection.
* **NJDEP Hydrography**: Category 1 (C1) water body proximity and mandatory 150-foot and 300-foot development buffer overlays.
* **Micro-Locational Crime vs. Transit Gravity**: Combining NJ Transit rail/light rail accessibility vectors against localized FBI Uniform Crime Reporting (UCR) property crime frequencies to quantify real tenant retention elasticity.

---

## Empirical Case Study: 13 May Street, Newark, NJ

A forensic walkthrough demonstrating how algorithmic underwriting dismantles retail valuation illusions:

| Metric | Retail Broker Listing | NJUDS Forensic Reality | Mathematical Rationale |
|---|---|---|---|
| **Asking Price / Valuation** | **$898,000** | **$425,000 (MAO)** | Reverse-engineered against true cost of capital and CapEx. |
| **Asset Year of Construction** | Marketed as "Turnkey Value-Add" | **1899 (MOD-IV Tax Record)** | 125-year-old wood frame structure; shared MEP infrastructure. |
| **CapEx Requirement** | "$15k - $30k cosmetic refresh" | **$245,000** | Mandatory utility separation, lead/asbestos abatement, structural leveling. |
| **Holding Horizon** | "Immediate Cash Flow" | **6+ Months Hold** | Mandatory 20-day NJ UCC municipal permit review cycle. |
| **Buy & Hold Cap Rate** | 8.5% (Pro-forma) | **3.74% (True Stabilized)** | Negative leverage against 6.00% debt yield ($0.88$ DSCR). |
| **Fix & Flip Outcome** | Projected $150k+ profit | **Net Loss > $500,000** | Total deal cost: $1.34M against $835,000 ARV. |
| **Chapter 123 Assessment** | "High Taxes - Appealable" | **Conforming (45.37%)** | Falls squarely inside Newark's Chapter 123 statutory corridor; no reduction granted. |
| **Verdict** | *"Rare Investment Opportunity"* | **DO NOT BUY** | Deterministic insolvency under true debt service and depreciation reality. |

---

## 2026–2027 Research Roadmap (Google Antigravity Frontier Science)

With the support of Google Antigravity and the Gemini 4 Argon High ecosystem, our lab is pursuing a 3-phase statewide computational study:

1. **Phase 1: Statewide Assessment Disparity & Regressivity Index (3.14M Parcels)**
   * Ingesting 10+ years of New Jersey SR1A verified sales deeds and MOD-IV assessment books across all 564 municipalities.
   * Computing Gini coefficients of assessment regressivity to quantify whether lower-tier properties carry disproportionate tax burdens compared to luxury properties.
2. **Phase 2: High-Throughput Multi-Modal Structural Depreciation Modeling**
   * Scaling the Scatter-Gather Map-Reduce pipeline across 500,000+ historical MLS and satellite images to establish the first open latent structural depreciation index for aging East Coast urban centers.
3. **Phase 3: Autonomous Zero-Shot Spatial Underwriting Agents**
   * Utilizing Antigravity multi-agent orchestration and Gemini 4 Argon High's massive context window to synthesize full municipal master plans, zoning ordinances, and environmental GIS shapefiles into an open-source autonomous underwriting framework.

---

## Principal Investigator & Contact
* **Principal Researcher**: Dorian Mario Gonzalez
* **Organization**: New Jersey Underwriting Data Systems (NJUDS) — Computational Econometrics Research Lab
* **Email**: `dorianmariogonzalez@gmail.com`
* **Repository**: [https://github.com/emperor-novero/njuds-computational-econometrics](https://github.com/emperor-novero/njuds-computational-econometrics)
