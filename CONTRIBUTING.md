# Contributing to NJUDS Computational Spatial Econometrics Lab

Thank you for your interest in contributing to the **NJUDS Computational Spatial Econometrics Lab**. 

This repository is dedicated to advancing deterministic, open-science computational spatial econometrics, multi-modal computer vision architectures for structural depreciation, and statutory property tax equalization modeling across New Jersey's 564 municipal jurisdictions.

---

## 1. Code of Conduct & Scientific Integrity

We adhere to the highest standards of empirical rigor and computational reproducibility:
* **Zero Hallucination Tolerance**: Valuation models, statutory tax calculations, and depreciation estimates must be anchored in deterministic legal, spatial, and mechanical constraints.
* **Empirical Ground Truth Priority**: Computational claims must be substantiated by empirical data (MOD-IV assessment records, SR1A verified sales deeds, NJ UCC construction subcodes, FEMA/NJDEP GIS shapefiles).
* **Non-Commercial Open Science**: Contributions must remain accessible under the **MIT License** (code) and **Creative Commons Attribution 4.0 International (CC BY 4.0)** (monographs, datasets, and documentation).

---

## 2. Core Research Pillars for Contribution

We actively invite contributions across four primary research domains:

1. **Multi-Modal Vision & Structural Diagnostics (`src/njuds_econometrics/scatter_gather.py`)**:
   - Algorithms optimizing the Scatter-Gather map-reduce token reduction pipeline.
   - Computer vision feature extraction for foundation shear cracks, roof line deflection, MEP entanglement, and water intrusion staining.
   - Token budget compression minimizing the "Vision Token Tax."

2. **Statutory Equalization & Chapter 123 Modeling (`src/njuds_econometrics/chapter123.py`)**:
   - Mathematical modeling of N.J.S.A. 54:51A-6 (Chapter 123 tolerance corridors: $`0.85 \times R`$ to $`1.15 \times R`$).
   - Assessment regressivity modeling (Gini coefficients, PRD, PRB across municipal assessment books).
   - Dynamic added assessment calculations triggered by municipal building permits and Certificates of Occupancy (N.J.S.A. 54:4-63.2).

3. **Multi-Layer Spatial & Environmental GIS (`docs/monographs/`, `data/`)**:
   - High-precision coordinate resolution and spatial joins using the New Jersey State Plane Coordinate System (NAD83 / NJ State Plane FIPS 2900, EPSG:3424).
   - Integration with FEMA National Flood Hazard Layer (NFHL) 100-year and 500-year flood hazard vectors.
   - NJDEP Category 1 (C1) stream hydrography and 150-foot / 300-foot riparian buffer intersections.
   - Micro-locational transit gravity vectors vs. FBI UCR crime decay decay functions.

4. **Financial Underwriting & Forensic Autopsies (`src/njuds_econometrics/underwriting.py`, `case_studies/`)**:
   - Institutional debt service coverage (DSCR), capitalization rate, and maximum allowable offer (MAO) models.
   - Empirical forensic case studies documenting algorithmic pricing failures in legacy pre-1940 urban housing stock.

---

## 3. Development Environment & Standards

### Prerequisites
* **Python**: Version 3.10 or higher.
* **Core Dependencies**: Standard library preferred for reference implementations (`dataclasses`, `typing`, `json`, `math`, `unittest`). External packages for extended research: `numpy`, `pandas`, `geopandas`, `shapely`.

### Code Style Guidelines
* **Type Annotations**: All function signatures, class attributes, and method return types must have explicit Python type hints (`typing.Tuple`, `typing.Dict`, `typing.Optional`, etc.).
* **Docstrings**: Adhere to Google/NumPy docstring formats detailing parameters, return types, statutory citations, and exceptions.
* **Determinism**: Code must produce deterministic, reproducible outputs for identical inputs. Floating-point currency calculations must be rounded to two decimal places or use decimal arithmetic for statutory precision.

---

## 4. Data Schemas & Validation Standards

### MOD-IV Municipal Tax Record Schema
When contributing parcel-level data or test fixtures, adhere to the official New Jersey Division of Taxation MOD-IV fixed-width field specifications:
* `municode` (String, 4 digits): County/Municipality code (e.g., `"0714"` for Newark).
* `block` (String, max 10 chars): Tax parcel block identifier.
* `lot` (String, max 10 chars): Tax parcel lot identifier.
* `prop_class` (String, 2 chars): Property class code (`"2"` for Residential 1-4 family, `"4A"` for Commercial, `"15C"` for Public Property).
* `year_built` (Integer, 4 digits): Actual construction vintage. Do NOT use effective age unless explicitly flagged.
* `assessed_land` (Float): Current year assessed land value.
* `assessed_imp` (Float): Current year assessed improvement value.
* `assessed_total` (Float): Sum of land and improvements.

### Chapter 123 Equalization Dataset Schema (`data/sample_director_ratios_2026.json`)
Entries must include:
```json
{
  "county": "County Name",
  "county_code": "2-digit FIPS/NJ code",
  "municipality_name": "Official Municipal Name",
  "municode": "4-digit statutory code",
  "directors_ratio": 0.4537,
  "common_level_ratio": 0.4537,
  "corridor_lower_limit": 0.3856,
  "corridor_upper_limit": 0.5218,
  "general_tax_rate_per_100": 3.760,
  "effective_tax_rate_pct": 1.706,
  "last_revaluation_year": 2013,
  "revaluation_status": "Status description",
  "tax_court_venue": "Assigned Tax Court Chamber",
  "notes": "Empirical and legal commentary"
}
```

---

## 5. Municipal Construction Code (NJ UCC) Validation

Contributions modeling rehabilitation timelines, construction costs, or permit cycles must comply with the **New Jersey Uniform Construction Code (N.J.A.C. 5:23)**:
* **The 20-Day Rule**: Permit plan examinations have a statutory maximum turnaround of 20 business days per review cycle (N.J.A.C. 5:23-2.15(e)). Models must incorporate realistic iterative review cycles (average 2 to 3 iterations for multi-trade subcode modifications).
* **Trade Subcodes**: Segregate CapEx scopes into the four statutory UCC subcodes:
  1. *Building Subcode* (N.J.A.C. 5:23-3.14 / IBC/IRC NJ edition)
  2. *Electrical Subcode* (N.J.A.C. 5:23-3.16 / NEC 2023)
  3. *Plumbing Subcode* (N.J.A.C. 5:23-3.15 / National Standard Plumbing Code NJ edition)
  4. *Fire Protection Subcode* (N.J.A.C. 5:23-3.17)
* **Lead Hazard Regulations**: For structures constructed prior to 1978, models must account for New Jersey DCA Lead-Safe Certification (P.L. 2021, c. 182) and EPA Renovation, Repair, and Painting (RRP) standards.

---

## 6. Testing & Benchmark Verification

All pull requests must pass 100% of the unit test suite and maintain benchmark integrity:

```bash
# Run unit test suite
python3 -m unittest discover tests

# Execute the 13 May St, Newark benchmark autopsy
python3 benchmarks/run_newark_case_study.py
```

### Adding New Tests
* Place new tests in `tests/test_<module_name>.py`.
* Test edge cases, boundary conditions (corridor borders: exactly $`0.85 \times R`$ and $`1.15 \times R`$), and invalid inputs (negative values, zero denominators).
* Document statutory court precedents where applicable (e.g., *Murnick v. Asbury Park*, *Centorino v. Tewksbury Twp.*).

---

## 7. Submission & Pull Request Workflow

1. **Fork the Repository**: Create a personal fork on GitHub.
2. **Create a Topic Branch**: Use descriptive branch names:
   * `feat/chapter123-reassessment-decay`
   * `fix/dscr-tax-underwriting`
   * `data/passaic-county-ratios-2026`
   * `docs/monograph-spatial-decay`
3. **Commit Messages**: Follow standard conventional commits format:
   * `feat(chapter123): implement dynamic added assessment calculator`
   * `fix(underwriting): correct loan constant rounding in DSCR engine`
   * `docs(case-study): expand UCC permit schedule for 13 May St`
4. **Open a Pull Request**: Provide a clear summary of modifications, statutory rationale, and test verification output.

---

## 8. Licensing Agreement

By submitting code, documentation, datasets, or monographs to the **NJUDS Computational Spatial Econometrics Lab**, you agree that your contributions will be licensed under the repository's open-source terms:
* **Code and Software**: MIT License.
* **Monographs, Case Studies, and Datasets**: Creative Commons Attribution 4.0 International (CC BY 4.0).
