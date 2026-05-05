# LandSAR Development Log

**Project:** LandSAR
**Type:** Reconstructed + Active Development Log
**Scope:** 2020 – Present

---

## Overview

This document captures the development of LandSAR from initial concept through current system architecture.

Entries include reconstructed historical phases and detailed recent development logs, highlighting system evolution, modeling advancements, and technical milestones.

---

## Important Note

This is a reconstructed development log based on prior work, project structure, debugging history, and development progression. It is intended to accurately represent the evolution of the system.

---

## 2020 — Concept Initiation

* Project concept developed following graduation from Texas A&M
* Focus on building a land-based search and rescue modeling platform
* Early emphasis on:

  * Last Known Position (LKP)
  * Time-based movement
  * Terrain influence on subject behavior

---

## 2021 — Foundational Modeling

### Early 2021

* Built initial grid-based search area models
* Developed coordinate handling and projection logic
* Began Python-based probability surface generation
* Implemented time-based search radius logic

### Mid–Late 2021

* Expanded grid generator and spatial logic
* Introduced weighted probability modeling
* Began incorporating terrain influence concepts (slope, elevation)

---

## 2022 — Terrain & Route Awareness

### Early–Mid 2022

* Continued refining search-grid and time-based expansion
* Introduced road and route influence concepts
* Began combining terrain penalties with accessibility

### Late 2022

* Improved visualization outputs
* Transitioned toward operationally meaningful outputs
* Strengthened modular code structure

---

## 2023 — Sectorization & Search Prioritization

### Early 2023

* Introduced sector-based search prioritization (P1, P2, P3)
* Shifted from visualization to operational decision support

### Mid–Late 2023

* Improved probability clustering and grouping
* Refined balance between movement assumptions and terrain constraints

---

## 2024 — Terrain Intelligence & Refinement

* Strengthened terrain and slope modeling
* Improved priority zone rendering and labeling
* Refactored code for maintainability and performance
* Continued progression toward user-facing system

---

## 2025 — Transition to Application

* Expanded into interactive application development
* Built modular system architecture
* Developed UI launcher and map-based workflow
* Separated modeling, visualization, and future behavioral modules

---

## 2026 — Active Development & System Evolution

### January 2026

* Continued UI and system structure development
* Refined platform direction toward operational SAR modeling

---

### March 2026 — Stabilization & Debugging Phase

* Resolved key runtime and structural issues:

  * Sector labeling errors
  * Indentation inconsistencies
  * Undefined variables impacting visualization
* Improved system stability and execution flow
* Continued development of:

  * LKP handling
  * Time and delay modeling
  * Sector prioritization
  * Heatmap visualization
  * Road and route integration
* Stabilized UI launcher and map panel integration

---

### March 30, 2026 — Stable System Checkpoint

Defined working-state baseline:

* Map loads successfully
* LKP selection functional
* Road data loading correctly
* Address and cross-street inputs operational

---

### April 1, 2026 — System Direction Expansion

* Introduced:

  * Monte Carlo particle simulation
  * Route history and projection modeling
  * Integration of IAMSAR-aligned search tactics

---

### April 2, 2026 — System Definition & Consolidation

* Consolidated full project history into structured documentation
* Defined system as a terrain-aware probabilistic SAR platform
* Core system components:

  * Probability heatmaps
  * Terrain penalties
  * Route and access bias
  * Sector prioritization
* Transitioned visualization strategy toward:

  * Particle-based modeling
  * Route-density overlays
* Defined future direction:

  * Path-density modeling (movement corridors)
  * Enhanced terrain intelligence
  * Behavioral modeling integration

---

### April 3, 2026 — Path Modeling Development (In Progress)

**Objective:** Introduce path-density modeling using Monte Carlo history

* Began implementation of path-history aggregation
* Defined separation between:

  * Endpoint probability
  * Movement corridor density
* Planned dual-layer visualization system
* Next step:

  * Generate path-density GeoJSON layer
  * Integrate with map rendering system

---

### April 4, 2026 — System Architecture Expansion

**Major Transition: Prototype → Full Modeling System**

#### Core Modeling

* Confirmed Monte Carlo as primary probability engine
* Began path-density optimization

#### Scenario Engine Design

* Introduced multi-scenario modeling framework:

  * Mobile
  * Injured
  * Sheltered
  * Water-affected
  * Vehicle-based

#### Behavioral Integration

* Began integrating lost-person behavior modeling
* Transitioned toward behavior-driven simulation

#### Environmental Intelligence

* Designed real-time environmental inputs:

  * Weather
  * Time-of-day
  * Visibility

#### Terrain Strategy

* Defined layered environmental model:

  * Terrain + weather → movement influence

#### Product Direction

* Defined future deployment strategy:

  * Desktop / Web / Hybrid
* Established long-term development pathway:

  * Prototype → Pilot → Deployment

---

### April 7, 2026 — Terrain Model Refinement

* Defined use cases for:

  * DEM (general elevation)
  * DTM (bare-earth modeling)
  * DSM (surface + obstruction modeling)

**Decision:**

* DTM → primary movement surface
* DSM → visibility and obstruction
* DEM → fallback

---

### April 8, 2026 — Simulation Behavior Analysis

* Identified radial symmetry issue in probability output
* Determined root cause:

  * Lack of terrain, route, and behavioral influence
* Implemented new development strategy:

  1. Break radial symmetry
  2. Introduce directional bias
  3. Add terrain influence
  4. Integrate decision logic
  5. Add environmental layers

---

### April 11, 2026 — Terrain Pipeline Complete

* Integrated DEM retrieval via OpenTopography
* Implemented slope and terrain penalty modeling
* Validated:

  * Realistic slope ranges
  * Effective terrain resistance

**Outcome:**

* Terrain-aware modeling foundation established

---

### April 13–14, 2026 — Movement Modeling Expansion

* Successfully integrated terrain penalties into simulation

* Began defining multi-layer movement influence system:

  * Roads/trails (positive bias)
  * Water/obstacles (negative bias)
  * Terrain (penalty-based)

* Defined next modeling phase:

  * Distance-based attraction/repulsion layers

---

### April 15, 2026 — Data Integration Breakthrough

* Monte Carlo simulation stabilized with terrain influence
* Identified gap:

  * Lack of real-world route adherence

#### Major Addition:

* Integrated NPS geospatial datasets:

  * Trails
  * Roads
  * Buildings
  * Parking
  * POIs

**Capability Upgrade:**

* System can now ingest real-world infrastructure data

**Next Steps:**

* Integrate trails/roads into movement modeling
* Add spatial indexing and route bias

---

### April 20, 2026 - Terrain Bias $ Road Overlay Breakthrough

Major progress on PATHSAR simulation realism. Successfully integrated road overlays with terrain-influenced Monte Carlo movement. The system is now producing believable directional bias based on terrain and subject behavior.

**What Changed:**

1. Road Overlay – Working State

- Road network successfully loaded and rendered on map
- Visual confirmation of road influence pathways
- Cached loading working as expected
- Roads now provide a structural reference layer for movement modeling

2. Terrain Bias – Functional

- Terrain weighting is now actively influencing particle movement
- Simulation produced a clear directional trend (NE → SW)
- Behavior aligns with:
- Slope penalties
- Terrain type (wooded)
- Lost hiker profile tendencies

3. Monte Carlo Output – Visible + Interpretable

- Particle count returning properly (150)
- Heat cells and path cells generating
- Particle lines rendering on map
- Movement patterns now tell a story, not just random spread

**Key Observation:**

Terrain + behavior bias resulted in a natural corridor forming from north-east to south-west, suggesting:

Drainage or terrain-following behavior is working
Simulation is beginning to reflect real-world lost person movement patterns, not just probability blobs

This is a critical milestone toward operational realism.

⚠️ Known Issue
TypeError: bbox_to_poly() takes 1 positional argument but 4 were given
Occurs during bounding box handling

Does not block simulation output, but needs cleanup
Likely mismatch between helper function signature and call

---

## Devlog Update: PATHSAR UI + Field Layer Evolution

### April 28–29, 2026

Continued evolving PATHSAR from a prototype map/control panel into a more operational SAR planning workspace. Work focused on application branding, startup workflow, map usability, basemap improvements, field layer visibility, and groundwork for future search object/resource planning.

Completed Updates

Application identity

- Created and integrated a PATHSAR application icon.
- Added icon support in both main.py and LandSARMainWindow.
- Confirmed the icon displays correctly in the app title bar.

Startup workflow

- Added a dedicated startup scenario intake window.
- Shifted initial scenario setup out of the main left panel.
- Main workspace now opens after scenario initialization.
- Current time is handled automatically instead of requiring manual input.
- Weather is currently marked as auto_pending for future live weather integration.

Main workspace cleanup

- Removed the heavy duplicate intake experience from the visible main panel.
- Added a cleaner scenario summary area.
- Preserved hidden backing widgets so existing geocoding and simulation functions continue working.
- Began transitioning the app from form-driven to scenario-driven workflow.

Address suggestions

- Improved address suggestion responsiveness.
- Reduced suggestion delay to make location recall feel faster while typing.
- Lowered the minimum character threshold for suggestions.

Basemap improvements

- Kept Topo as the default operational basemap.
- Added Satellite imagery.
- Added Hybrid imagery layer using satellite imagery with Esri label overlays.
- Adjusted zoom behavior to reduce disappearing/blank map tiles at high zoom levels.

Toolbar / buttonology foundation

- Began adding a top toolbar for future operational tools.
- Planned toolbar actions include:
- Update Scenario
- Add Clue / Track
- Center Map
- Load Roads / Trails / Field Layers
- Clear Overlay
- Run Monte Carlo
- Run Simulation
- Sector Tools
- Timeline

Roads, trails, and POI field layers

- Began expanding “Load Roads/Trails” into broader field layer loading.
- Added planned support for:
  - roads
  - trails
  - trailheads
  - campgrounds
  - water towers
  - ranger stations
  - parking areas
  - viewpoints
  - springs / water points
- Added logic direction for POIs to render as markers instead of line features.
- Added hover/popup labeling design for roads, trails, and landmarks.
- Defined visual layer meanings:
  - Yellow = roads / vehicle-access routes
  - Green dashed = trails / footpaths
  - Cyan = Monte Carlo particle paths
  - Red/orange = probability heat cells
  - Blue pin = LKP marker
  - POI colors planned by feature type

Monte Carlo / overlay usability

- Identified that Monte Carlo layers can visually obscure access layers if not managed carefully.
- Added direction to keep operational layers brought to front across basemap changes.
- Planned Monte Carlo layers to be non-interactive where needed so road/trail hover remains usable.
- Issues Identified / In Progress
  - OSMnx feature loading is still returning errors related to invalid bbox polygons and NaN geometry calculations.
  - Roads/trails/POI overlay depends on fixing or stabilizing feature_loader.py.
  - Satellite and Hybrid will only show trail detail once PATHSAR’s own access/field overlay loads correctly.
  - Update Scenario button exists but still needs to be fully wired.
  - Toolbar icons are placeholders and need final buttonology design.
  - Weather auto-pull is not yet implemented.
  - Search object and resource inputs still need to be added before initial search setup.

Next Planned Work
- Stabilize feature_loader.py so roads, trails, hydro, and POIs reliably load.
- Confirm field layers display across Topo, Hybrid, Satellite, Light, and Streets.
- Wire Update Scenario button.
- Add Search Object selection before initial search.

Add Search Resources / Tools available:
- walking search teams
- dogs / K9
- horses
- ATVs / four-wheelers
- UTVs
- drones

Add Add Clue / Track tool for:
- footprints
- belongings
- debris
- sightings
- other search clues

Continue toward timeline/time-lapse bar and sectorization tools.

---

## Devlog Update: PATHSAR UI + Field Layer Evolution

### April 30- May 5, 2026

Phase X – Sectorization, Terrain Bias, and Operational Workflow
Overview

This phase focused on transitioning PATHSAR from a visualization tool into a more operationally relevant SAR planning system. Core improvements include terrain-influenced movement modeling, probability-driven sectorization, and the introduction of a sector management interface.

Monte Carlo + Terrain Integration
Implemented terrain-aware movement using slope and environmental penalties
Particle movement now reflects realistic behavior (contour following, avoidance of steep terrain)
Outputs show directional bias rather than uniform spread
Reduced cell size for higher-resolution probability surfaces

Result:
More realistic subject movement modeling and tighter probability clustering

Heatmap Refinement
Reduced grid cell size for increased spatial accuracy
Adjusted visual styling to reduce blockiness and improve readability
Improved separation between probability visualization and terrain layers

Result:
Cleaner probability surfaces with more precise boundaries

Sectorization (Initial Implementation)
Built automated sector generation from heatmap extent
Implemented 3×3 grid structure as initial framework
Added:
Area calculations (sq mi and acres)
Width/height estimates
Priority ranking based on probability density
Converted sector naming from numeric → A, B, C…
Sorted sectors by probability (highest = Sector A)

Result:
Sectors now represent prioritized search areas rather than arbitrary grid divisions

Sector Interaction + Controls
Click-to-select sector highlighting
Lock/unlock functionality for assignment control
Zoom-to-sector capability
Status feedback integrated into UI

Result:
Interactive sector management aligned with SAR operational workflows

Sector Management Panel (In Progress)
Introduced structured panel for sector oversight
Designed to display:
Sector priority
Area
Status (open/locked/searched)
Panel dynamically updates with selection and state changes

Next Step:
Stabilize rendering and finalize layout (Leaflet control integration)

Weather Integration (Initial)
Live weather pulled automatically based on LKP
Weather summary displayed in UI (temp, wind, precipitation, humidity)
Radar overlay temporarily disabled due to tile compatibility issues

Result:
Weather now informs scenario context without interrupting workflow

Performance Improvements
Reduced rendering load from particle density and grid resolution
Improved responsiveness during Monte Carlo execution
Eliminated visual clutter (removed corridor lines, refined overlays)
Key Milestone

This phase marks the shift from:

static probability visualization → dynamic, decision-support SAR tool

Next Development Targets
1. SAR Probability Framework

Add operational metrics to each sector:

POA (Probability of Area)
POD (Probability of Detection)
POS (Probability of Success = POA × POD)

Dynamic updates based on:

search coverage
asset deployment
clues/finds
negative search results
2. Sector Management Expansion
Full SAROPS-style panel
Assign teams/assets to sectors
Mark sectors:
open
in progress
complete
Manual priority adjustment
Sector splitting for large/high-value areas
3. Weather Overlays (Rebuild)
Replace radar with stable tile source
Add:
precipitation influence
heat/cold effects on movement
flood/fire constraints
4. Environmental Constraints
Integrate:
water barriers
terrain difficulty
access networks
Influence both:
movement modeling
sector prioritization
5. Fully Automated Workflow

Move toward a single execution path:

Run Simulation →
  Weather →
  Terrain →
  Monte Carlo →
  Heatmap →
  Sectorization →
  Priority Assignment →
  Operational Panel
Notes
Current outputs confirm terrain bias is functioning correctly
Sector prioritization aligns with probability distribution
System is ready to transition into full SAR decision-support modeling