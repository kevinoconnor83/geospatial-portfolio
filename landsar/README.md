# LandSAR

Terrain-aware search and rescue modeling designed to support real-world decision-making through geospatial analysis and probabilistic simulation.

---

## Overview

LandSAR is a geospatial modeling system that simulates subject movement and generates probable search areas using terrain, access routes, and environmental factors.

The system is designed to move beyond simple mapping and toward operational search planning support.

---

## Key Capabilities

- Monte Carlo-based movement simulation  
- Terrain-aware modeling using elevation and slope  
- Integration of trails, roads, and access features  
- Heatmap generation of probable subject locations  
- Path-density modeling for likely movement corridors  
- Sector-based search prioritization  

---

## Why This Matters

Search and rescue operations are time-critical and resource-limited.

LandSAR is designed to:
- Improve search efficiency  
- Support better resource allocation  
- Provide data-driven search strategies  

---

## Development Status

Active development — core modeling, terrain integration, and simulation systems in progress.

---

## Development History

See full development log:  
[Development Log](docs/devlog.md)

---

## Roadmap

See full development roadmap:  
[Roadmap](docs/roadmap.md)

---

## Images

### Phase 1 - Baseline Probability Model

<p align= "center"><img src="images/figure_001_initial_probability.png" width="600"</p>

- Radial probability distribution from Last Known Position (LKP)
- No terrain, roads, or behavioral constraints
- Purely mathematical decay model

Why this matters:
This established the foundation for visualizing probability fields and validating the rendering pipeline.

### ───────────────────────────────────────────────────────────────────────

### Phase 2 - Real-World Constraints Introduced

<p align= "center"><img src="images/figure_002_roads_slope.png" width="600"</p>

- Integrated real-world road networks (OSMnx)
- Added slope penalty from DEM data
- Particle movement influenced by terrain + infrastructure

Blue lines = simulated movement paths
Heatmap = accumulated probability density

Why this matters:
This marks the transition from a theoretical model to an environment-aware simulation.

### ───────────────────────────────────────────────────────────────────────

### Phase 3 - Real-World Constraints Introduced

<p align= "center"><img src="images/figure_003_projected.png" width="600"</p>

- Converted simulation from lat/lon to projected CRS (UTM)
- Enabled accurate distance calculations
- Eliminated geographic distortion

Why this matters:
Geographic coordinates distort distance. This correction ensures real-world movement accuracy.

### ───────────────────────────────────────────────────────────────────────

### Phase 4 — Distance-Based Movement Modeling

<p align="center">
  <img src="images/figure_004_projected_distances.png" width="600"/>
</p>

**Probability Map with Real Roads + Projected Distances**

**What changed:**

- Movement distance constraints introduced  
- Transition from random dispersion to bounded travel behavior  
- Spatial clustering begins to emerge  

**What you're seeing:**

- Heatmap:
  - Concentrations now reflect reachable zones  
- Road network:
  - Still influencing directional movement  

**Why this matters:**

This is the first step toward modeling **real human movement limitations** instead of abstract spread.

---

## 🔹 Phase 5 — Time & Delay Awareness

<p align="center">
  <img src="images/figure_005_time_delay.png" width="600"/>
</p>

**Probability Map with Time Since LKP + Report Delay**

**What changed:**

- Time since last known point applied  
- Reporting delay incorporated into spread  
- Expansion becomes time-dependent  

**What you're seeing:**

- Wider probability distribution:
  - Increased uncertainty over time  
- Heat zones:
  - Reflect time-adjusted likelihood  

**Why this matters:**

Time is one of the most critical SAR variables — this introduces **temporal realism into the model**.

---

## 🔹 Phase 6 — Sectorization (Search Prioritization)

<p align="center">
  <img src="images/figure_006_sectorization.png" width="600"/>
</p>

**Probability Map with Sector Assignments (A / B / C)**

**What changed:**

- Search area divided into priority sectors  
- High-probability zones grouped spatially  
- Non-overlapping operational regions created  

**What you're seeing:**

- Sector A:
  - Highest priority  
- Sector B:
  - Moderate probability  
- Sector C:
  - Lower probability  

**Why this matters:**

This converts analysis into **actionable search assignments**, aligning with real SAR operations.

---

## 🔹 Phase 7 — Operational Search Footprint

<p align="center">
  <img src="images/figure_007_search_footprint.png" width="600"/>
</p>

**Final Search Coverage & Operational Footprint**

**What changed:**

- Search areas consolidated into continuous coverage zones  
- Redundant overlap reduced  
- Efficient sweep regions generated  

**What you're seeing:**

- Cyan boundaries:
  - Searchable operational zones  
- Red cells:
  - High-priority targets within sectors  

**Why this matters:**

This represents the transition from modeling to **deployable field strategy** — exactly what SAR teams need.

---

## Technical Stack

- Python  
- GeoPandas  
- Rasterio  
- OSMnx  
- PySide6 (UI)  
- Leaflet (mapping)

---

## Notes

Full implementation is not publicly released at this time.