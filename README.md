# INFRA SHEILD

GIS-based infrastructure intelligence platform for road condition analysis,
risk assessment and predictive maintenance.

## Current Prototype

Location:
Lucknow, Uttar Pradesh

Infrastructure:
Road Network

## Technology Stack

- Python
- PostgreSQL
- PostGIS
- OpenStreetMap
- GeoPandas
- SQL
- GIS

## Current Architecture

OpenStreetMap
        ↓
Lucknow Road Network
        ↓
PostgreSQL + PostGIS
        ↓
Road Damage Data
        ↓
Risk / Health Analysis
        ↓
Repair Priority
        ↓
GIS Dashboard

## Current Progress

### Completed

- [x] PostgreSQL setup
- [x] PostGIS setup
- [x] Python PostgreSQL connection
- [x] Lucknow OSM road data collection
- [x] Road data cleaning
- [x] 181,305 road records imported
- [x] Geometry verification
- [x] SRID verification
- [x] road_id validation
- [x] Primary key
- [x] Spatial index
- [x] Road damage table
- [x] Foreign key relationship
- [x] Road + damage JOIN testing

### In Progress

- [ ] Rainfall dataset
- [ ] Environmental data integration
- [ ] Road health/risk model
- [ ] Repair priority model
- [ ] GIS dashboard

## Database

Main tables:

- roads
- road_damage

Relationship:

roads.road_id
        ↓
road_damage.road_id

## Road Dataset

Location:
Lucknow, Uttar Pradesh

Records:
181,305

Geometry:
LineString

CRS:
EPSG:4326

## Important Note

The current road damage record is test/demo data.
It is not being presented as actual AI-generated damage detection.

## Project Status

The database and geospatial road-data foundation are currently implemented.
The final SIH 2026 problem-statement alignment is currently being evaluated.
