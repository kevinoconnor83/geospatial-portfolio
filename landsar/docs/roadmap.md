# LandSAR Roadmap

This roadmap outlines the ongoing development and future direction of the LandSAR system.

---

## Phase 1: Core System (Completed)

- Map-based UI (PySide6 + Leaflet)
- Last Known Position (LKP) selection
- Road and trail data integration
- DEM loading and terrain preprocessing
- Slope calculation and terrain penalty modeling
- Grid-based probability surface generation

---

## Phase 2: Probabilistic Modeling (In Progress)

- Monte Carlo particle simulation
- Terrain-influenced movement behavior
- Time-based movement expansion
- Initial heatmap generation from particle endpoints

---

## Phase 3: Movement Intelligence (In Progress)

- Path-density modeling (likely movement corridors)
- Separation of:
  - Endpoint probability (current location likelihood)
  - Path probability (movement history density)
- Reduction of radial symmetry through environmental influence

---

## Phase 4: Environmental & Feature Integration (Next)

- Trail and road attraction bias
- Water and barrier modeling (rivers, lakes, cliffs)
- Terrain + feature combined movement scoring
- Spatial indexing for real-world feature interaction

---

## Phase 5: Behavioral Modeling (Planned)

- Integration of lost-person behavior profiles
- Scenario-based simulation (mobile, injured, etc.)
- Behavior-driven movement parameters:
  - step distance
  - direction variance
  - stopping probability

---

## Phase 6: Environmental Intelligence (Planned)

- Real-time weather integration
- Time-of-day and visibility modeling
- Dynamic environmental influence on movement and survivability

---

## Phase 7: Advanced Modeling & Validation (Future)

- Case-based validation (real SAR scenarios)
- Machine learning enhancements (optional)
- Route prediction refinement
- Historical scenario comparison

---

## Phase 8: Product Development (Future)

- Application deployment (desktop/web/hybrid)
- API and data pipeline development
- Cloud integration
- Agency-focused licensing and distribution

---

## Long-Term Vision

LandSAR is being developed as a terrain-aware, behavior-informed search and rescue modeling platform designed to support real-world decision-making through probabilistic analysis and geospatial intelligence.