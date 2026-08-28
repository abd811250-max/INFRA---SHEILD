# 🛣️ INFRA SHEILD

### Smart Road Infrastructure Risk Monitoring & Decision Support System

> **INFRA SHEILD** is a GIS-enabled road infrastructure monitoring system designed to identify and prioritize potentially high-risk road segments using road network data, rainfall exposure, road damage information, spatial analysis, and a weighted risk-scoring model.

---

## 📌 Project Overview

Road infrastructure can deteriorate rapidly due to rainfall, water exposure, surface damage, and other environmental and operational factors.

**INFRA SHEILD** combines spatial road-network data with rainfall and road-damage information to generate a **road-level risk score and risk classification**.

The system is being developed as a **Smart India Hackathon (SIH) MVP**, with the current focus on demonstrating the complete data-to-map workflow.

### 🎯 Core Objective

```text
Road Network
     +
Road Damage
     +
Rainfall
     +
Spatial Information
     ↓
Rainfall Exposure
     ↓
Risk Calculation
     ↓
Risk Classification
     ↓
FastAPI Backend
     ↓
React + Leaflet
     ↓
Interactive Risk Map & Dashboard
```

---

# 🚀 Key Features

| Feature                             |        Status       |
| ----------------------------------- | :-----------------: |
| 🛣️ Road network database           |      ✅ Complete     |
| 🗺️ PostGIS spatial data            |      ✅ Complete     |
| 🌧️ Historical rainfall integration |      ✅ Complete     |
| 🚧 Road damage integration          |      ✅ Complete     |
| 📍 Spatial rainfall exposure        |      ✅ Complete     |
| 📊 Risk scoring model               |      ✅ Complete     |
| 🚦 Risk classification              |      ✅ Complete     |
| 🔌 FastAPI backend                  |      ✅ Complete     |
| 🗺️ React + Leaflet frontend        |    ✅ Initial MVP    |
| 🔎 Risk-level filtering             |      ✅ Complete     |
| 📄 API pagination                   |      ✅ Complete     |
| 📊 Risk summary API                 |      ✅ Complete     |
| 🔐 Authentication / Admin system    | 🔄 Team integration |
| 🚀 Production deployment            |      ⏳ Planned      |

---

# 🏗️ System Architecture

```text
                    ┌─────────────────────────┐
                    │      ROAD NETWORK       │
                    │      181,305 Roads      │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      ROAD DAMAGE        │
                    │   Damage + Severity     │
                    │      + Confidence       │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │       RAINFALL          │
                    │  Historical Weather API │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   POSTGRESQL + POSTGIS  │
                    │                         │
                    │ Spatial Data Processing │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   RAINFALL EXPOSURE      │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      RISK ENGINE         │
                    │                         │
                    │ Rainfall Score           │
                    │ Damage Score             │
                    │ Weighted Risk Score      │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │    RISK CLASSIFICATION   │
                    │                         │
                    │ LOW / MEDIUM / HIGH     │
                    │ / CRITICAL              │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │    road_risk_view       │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │        FASTAPI           │
                    │       REST APIs          │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │     REACT + LEAFLET      │
                    │                         │
                    │ Interactive Risk Map     │
                    │ Dashboard                │
                    └─────────────────────────┘
```

---

# 🗄️ Database

### Database Technology

* **PostgreSQL**
* **PostGIS**
* **SQL**
* **Spatial SQL**

### Database Name

```text
infra_sheild_db
```

> ⚠️ The database name intentionally uses `sheild` as defined by the current project configuration.

---

## 📊 Current Database Statistics

| Dataset                   |     Records |
| ------------------------- | ----------: |
| 🛣️ Roads                 | **181,305** |
| 🚧 Road damage            |       **1** |
| 🌧️ Rainfall              |      **30** |
| 📍 Road rainfall exposure | **181,305** |
| 📊 Road risk              | **181,305** |
| 🗺️ Risk view             | **181,305** |

---

# 🛣️ Road Network

### Table

```text
public.roads
```

### Important fields

```text
road_id
geometry
```

The road geometry is stored using the PostGIS `geometry` column.

### Example Road ID

```text
LKO-000001
```

---

# 🚧 Road Damage

### Table

```text
public.road_damage
```

### Fields

```text
damage_id
road_id
damage_type
severity
confidence
detected_at
image_path
notes
```

The current MVP contains one verified damage record.

### Example

```text
Road ID       : LKO-000001
Damage Type   : pothole
Severity      : High
Confidence    : 94.50%
```

---

# 🌧️ Rainfall Data

Rainfall data is sourced from the **Open-Meteo Historical Weather API**.

### Current reference location

```text
Location : Lucknow, Uttar Pradesh, India
Latitude : 26.81898
Longitude: 80.93023
```

### Current rainfall period

```text
2026-07-28 → 2026-08-26
```

### Variables

```text
time
precipitation_sum
rain_sum
precipitation_hours
```

### Records

```text
30 daily rainfall records
```

---

# 📍 Rainfall Exposure

### Table

```text
public.road_rainfall_exposure
```

The table connects the road network with rainfall-related exposure information.

Important fields include:

```text
road_id
rainfall_reference_distance_m
total_rainfall_mm
average_daily_rainfall_mm
maximum_daily_rainfall_mm
rainy_days
heavy_rain_days
```

---

# ⚠️ MVP Spatial Rainfall Limitation

The current rainfall source provides data from **one weather reference location**.

Therefore, the MVP does not claim that every road has independently measured rainfall.

To differentiate roads spatially during prototype development, the MVP uses a **deterministic synthetic spatial exposure factor**.

### Current factor range

```text
0.75 → 1.25
```

The factor is deterministic based on `road_id`, meaning the same road receives the same factor consistently.

### Important

This synthetic factor is:

* ✅ deterministic
* ✅ reproducible
* ✅ useful for MVP differentiation
* ❌ not measured road-specific rainfall
* ❌ not a replacement for real rainfall grids

### Production Improvement

The synthetic factor can later be replaced with:

```text
Multi-point rainfall stations
        OR
Weather radar data
        OR
Gridded rainfall datasets
        OR
Satellite rainfall products
```

---

# 📊 Risk Calculation

INFRA SHEILD currently uses a weighted risk model combining rainfall exposure and road damage.

## 1️⃣ Rainfall Score

```text
rainfall_score =
((rainfall_spatial_factor - 0.75) / 0.50) × 100
```

Current verified range:

```text
Minimum : 0.00
Average : 50.04
Maximum : 100.00
```

---

## 2️⃣ Damage Score

Severity mapping:

| Severity     | Score |
| ------------ | ----: |
| 🔴 High      |   100 |
| 🟠 Medium    |    60 |
| 🟡 Low       |    30 |
| 🟢 No Damage |     0 |

Confidence is incorporated into the damage score:

```text
damage_score =
severity_score × confidence / 100
```

Example:

```text
High severity
Confidence = 94.50%

Damage Score = 94.50
```

---

## 3️⃣ Final Risk Score

Current MVP weights:

```text
Rainfall Risk = 50%
Damage Risk   = 50%
```

Formula:

```text
risk_score =
(rainfall_score × 0.50)
+
(damage_score × 0.50)
```

---

# 🚦 Risk Classification

| Risk Score | Classification  |
| ---------: | --------------- |
|     75–100 | 🔴 **CRITICAL** |
|   55–74.99 | 🟠 **HIGH**     |
|   30–54.99 | 🟡 **MEDIUM**   |
|    0–29.99 | 🟢 **LOW**      |

---

# 📈 Current Risk Distribution

Current verified MVP distribution:

| Risk Level  |       Roads |
| ----------- | ----------: |
| 🔴 CRITICAL |       **1** |
| 🟠 HIGH     |       **0** |
| 🟡 MEDIUM   |  **72,713** |
| 🟢 LOW      | **108,591** |
| **Total**   | **181,305** |

---

# 🚨 Current Critical Road

```text
Road ID        : LKO-000001
Damage Type    : pothole
Severity       : High
Confidence     : 94.50%
Rainfall Score : ~96.28
Damage Score   : 94.50
Risk Score     : ~95.39
Risk Level     : CRITICAL
```

This demonstrates how rainfall exposure and detected road damage can combine to prioritize a road segment.

---

# 🧠 Risk Data View

Backend-ready database view:

```text
public.road_risk_view
```

This view combines:

```text
public.roads
        +
public.road_damage
        +
public.road_rainfall_exposure
        +
public.road_risk
```

### Important fields

```text
road_id
geometry
damage_type
severity
confidence
detected_at
image_path
notes

total_rainfall_mm
average_daily_rainfall_mm
maximum_daily_rainfall_mm
rainy_days
heavy_rain_days

rainfall_spatial_factor
rainfall_score
damage_score
risk_score
risk_level
```

All **181,305 records** currently have valid road geometry.

---

# ⚡ Backend

The backend is built using:

* 🐍 Python 3.13
* ⚡ FastAPI
* 🚀 Uvicorn
* 🗄️ SQLAlchemy
* 🐘 PostgreSQL
* 🗺️ PostGIS
* 🔌 psycopg2
* 📐 GeoAlchemy2
* 🔐 python-dotenv

---

# 🔌 API Endpoints

## Health / Root

```http
GET /
```

Response:

```json
{
  "message": "Road Risk Detection API is running"
}
```

---

## Database Test

```http
GET /db-test
```

Used to verify:

```text
FastAPI
   ↓
SQLAlchemy
   ↓
psycopg2
   ↓
PostgreSQL
```

---

## Roads

```http
GET /roads
```

Supports pagination and risk-level filtering.

### Pagination

```http
GET /roads?limit=100
```

```http
GET /roads?limit=100&offset=100
```

### Risk filtering

```http
GET /roads?risk_level=CRITICAL
```

```http
GET /roads?risk_level=MEDIUM&limit=100
```

### Current limits

```text
Minimum limit : 1
Maximum limit : 1000
```

This prevents the API from attempting to return all 181,305 road geometries in a single response.

---

## Road Details

```http
GET /roads/{road_id}
```

Example:

```http
GET /roads/LKO-000001
```

Returns road-specific information including:

* Road ID
* Risk level
* Risk score
* Rainfall score
* Damage score
* Damage type
* Severity
* Confidence
* Rainfall information
* Geometry

---

## Risk Summary

```http
GET /risk-summary
```

Returns the current number of roads in each risk category.

---

## Damaged Roads

```http
GET /damaged-roads
```

Returns currently detected damaged-road records.

---

# 🗺️ Frontend

The frontend MVP is being developed using:

* ⚛️ React
* ⚡ Vite
* 🗺️ Leaflet
* JavaScript
* HTML/CSS

### Planned dashboard

```text
┌──────────────────────────────────────────────────────┐
│                  🛣️ INFRA SHEILD                    │
├──────────────────┬───────────────────────────────────┤
│                  │                                   │
│   RISK FILTER    │             🗺️ MAP               │
│                  │                                   │
│   All            │       Risk-colored roads         │
│   Low            │                                   │
│   Medium         │                                   │
│   High           │                                   │
│   Critical       │                                   │
│                  │                                   │
├──────────────────┴───────────────────────────────────┤
│ Total Roads | Critical | High | Medium | Low         │
└──────────────────────────────────────────────────────┘
```

### Road interaction

Selecting a road will display:

```text
Road ID
Risk Level
Risk Score
Rainfall Score
Damage Score
Damage Type
Severity
Confidence
```

---

# 🔄 Application Workflow

```text
             DATA SOURCES
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
   Road Network          Rainfall
        │                   │
        ▼                   ▼
    Road Damage       Rainfall Exposure
        │                   │
        └─────────┬─────────┘
                  ▼
          Risk Calculation
                  │
                  ▼
           Risk Classification
                  │
                  ▼
          PostgreSQL/PostGIS
                  │
                  ▼
          road_risk_view
                  │
                  ▼
               FastAPI
                  │
                  ▼
          REST / GeoJSON API
                  │
                  ▼
          React + Leaflet
                  │
                  ▼
       Interactive Risk Dashboard
```

---

# 📁 Project Structure

```text
INFRA---SHEILD/
│
├── 📂 backend/
│   ├── main.py
│   ├── database.py
│   ├── requirements.txt
│   ├── .env.example
│   └── .gitignore
│
├── 📂 frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   └── eslint.config.js
│
├── 📂 data/
│   └── README.md
│
├── 📂 database/
│   ├── schema.sql
│   ├── database/
│   │   └── indexes.sql
│   └── ...
│
├── 📂 docs/
│   └── progress.md
│
├── 📂 scripts/
│   ├── import_roads.py
│   └── test_connection.py
│
├── 📂 sql/
│   └── verification_queries.sql
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# 🔐 Environment Variables

Sensitive credentials must never be committed to GitHub.

### Local `.env`

```env
DB_HOST=127.0.0.1
DB_PORT=5432
DB_NAME=infra_sheild_db
DB_USER=your_username
DB_PASSWORD=your_password
```

### Repository

Only the template file should be committed:

```text
.env.example
```

### Never commit

```text
❌ .env
❌ database passwords
❌ API keys
❌ authentication secrets
❌ venv/
❌ node_modules/
```

---

# 🛠️ Local Development

## Backend

Navigate to:

```powershell
cd backend
```

Create/activate the virtual environment:

```powershell
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run FastAPI:

```powershell
python -m uvicorn main:app --host 127.0.0.1 --port 8000
```

API:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 💻 Frontend Development

Navigate to:

```powershell
cd frontend
```

Install dependencies:

```powershell
npm install
```

Start development server:

```powershell
npm run dev
```

Vite will provide a local development URL similar to:

```text
http://localhost:5173/
```

---

# 🔗 Frontend → Backend Communication

The intended application architecture is:

```text
React
  │
  │ HTTP / REST
  ▼
FastAPI
  │
  │ SQL
  ▼
PostgreSQL + PostGIS
```

The frontend **must not connect directly to PostgreSQL**.

All database access should go through the FastAPI backend.

---

# 👥 Team Development Workflow

```text
              GitHub Repository
                     │
                     ▼
                git pull
                     │
                     ▼
              Local Development
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
      Backend                Frontend
      FastAPI             React + Leaflet
          │                     │
          └──────────┬──────────┘
                     ▼
                  Testing
                     │
                     ▼
                 git status
                     │
                     ▼
                  git add
                     │
                     ▼
                 git commit
                     │
                     ▼
                  git pull
                     │
                     ▼
                 git push
                     │
                     ▼
              GitHub Repository
```

### Basic Git workflow

```bash
git pull origin main

git status

git add .

git commit -m "Describe your changes"

git push origin main
```

> ⚠️ Team members should coordinate before pushing directly to `main`. Feature branches and pull requests are preferable as the team grows.

---

# 🧪 Testing Strategy

The MVP should be tested across the following layers.

### Database

* Road count verification
* Geometry validity
* Rainfall records
* Damage records
* Risk distribution
* Spatial queries

### Backend

* `/`
* `/db-test`
* `/roads`
* `/roads/{road_id}`
* `/risk-summary`
* `/damaged-roads`

### API Parameters

```text
limit
offset
risk_level
road_id
```

### Frontend

* Map rendering
* Road loading
* Risk filtering
* Road selection
* Popup/details
* Dashboard statistics
* Backend connectivity

---

# 📊 Current MVP Status

## ✅ Completed

```text
PostgreSQL
PostGIS
Road network
Road damage integration
Rainfall data import
Rainfall exposure
Synthetic MVP spatial factor
Risk scoring
Risk classification
road_risk
road_risk_view
FastAPI setup
Database connectivity
Core REST APIs
API pagination
Risk-level filtering
React/Vite setup
Initial Leaflet frontend
GitHub repository integration
```

## 🔄 In Development

```text
Interactive risk map
Risk-colored road visualization
Road detail popup
Dashboard cards
Damaged-road interface
Frontend ↔ Backend integration
Team authentication/admin integration
```

## ⏳ Future

```text
Multi-point / gridded rainfall
More real road-damage records
Traffic importance
Road condition
Historical risk trends
Automated alerts
Advanced risk prediction
Production deployment
```

---

# ⚠️ Current MVP Limitations

### 1. Single Rainfall Reference Point

The current rainfall dataset is based on a single weather reference location.

### 2. Limited Damage Data

The current MVP contains only one verified road-damage record.

### 3. Synthetic Spatial Factor

A deterministic synthetic factor is currently used for prototype-level spatial differentiation.

It should not be presented as actual road-specific rainfall measurement.

### 4. Prototype Risk Model

The current 50/50 rainfall-damage weighting is an MVP model and can be recalibrated when more historical road-condition and rainfall data becomes available.

---

# 🔮 Future Enhancements

## 🌧️ Better Rainfall Intelligence

Replace the single-point approach with:

* Weather station networks
* Gridded rainfall datasets
* Radar rainfall
* Satellite precipitation
* Time-series rainfall analysis

## 🚧 Advanced Road Condition Detection

Integrate:

* Computer vision
* Pothole detection
* Crack detection
* Surface deterioration
* Image-based severity estimation

## 🚦 Additional Risk Factors

Future risk modelling can include:

```text
Rainfall
+
Road Damage
+
Road Condition
+
Traffic Volume
+
Road Importance
+
Flood Exposure
+
Historical Failures
```

## 🤖 Predictive Analytics

Future versions can use machine learning to predict:

```text
Probability of road deterioration
        +
Expected severity
        +
Maintenance priority
```

---

# 🎯 SIH MVP Demonstration Flow

```text
1. Open INFRA SHEILD
        ↓
2. Dashboard loads
        ↓
3. Risk-colored road map appears
        ↓
4. Select risk level
        ↓
5. Map filters roads
        ↓
6. Click a road
        ↓
7. Display road details
        ↓
8. Show risk calculation
        ↓
9. Identify critical/high-priority roads
        ↓
10. Demonstrate how infrastructure
    authorities can prioritize inspection
```

---

# 💡 Why INFRA SHEILD?

Traditional road monitoring can involve:

```text
Manual inspection
       +
Delayed reporting
       +
Large road networks
       +
Multiple environmental factors
```

INFRA SHEILD aims to provide a centralized spatial decision-support layer where road infrastructure data can be combined and converted into **actionable risk information**.

---

# 🧩 Technology Stack

| Layer                | Technology                        |
| -------------------- | --------------------------------- |
| 🗄️ Database         | PostgreSQL                        |
| 🗺️ Spatial Database | PostGIS                           |
| 🐍 Backend           | Python                            |
| ⚡ API Framework      | FastAPI                           |
| 🚀 Server            | Uvicorn                           |
| 🔌 Database ORM      | SQLAlchemy                        |
| 🗺️ Spatial Python   | GeoAlchemy2                       |
| ⚛️ Frontend          | React                             |
| ⚡ Frontend Tooling   | Vite                              |
| 🗺️ Mapping          | Leaflet                           |
| 🌧️ Weather Data     | Open-Meteo Historical Weather API |
| 🔧 Version Control   | Git + GitHub                      |

---

# 👨‍💻 Project Development

**Project:** INFRA SHEILD
**Purpose:** Smart India Hackathon MVP
**Focus:** GIS + Road Infrastructure + Rainfall + Risk Analysis + Web Dashboard

---

# 📜 Project Note

INFRA SHEILD is currently an **MVP/prototype** intended to demonstrate the complete technical workflow from spatial infrastructure data ingestion to road-level risk visualization.

Risk scores and classifications should be treated as **prototype decision-support outputs**, not as certified engineering assessments.

---

<p align="center">

### 🛣️ INFRA SHEILD

**Turning infrastructure data into actionable road-risk intelligence.**

⭐ Built for innovation, spatial intelligence, and smarter infrastructure monitoring.

</p>
