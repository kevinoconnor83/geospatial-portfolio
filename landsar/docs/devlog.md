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
