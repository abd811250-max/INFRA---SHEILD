from typing import Optional
from sqlalchemy import text
from fastapi import FastAPI
from sqlalchemy import text

from database import engine


app = FastAPI(
    title="Road Risk Detection API",
    description="Backend API for road damage and rainfall risk analysis",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Road Risk Detection API is running"
    }


@app.get("/db-test")
def database_test():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            value = result.scalar()

        return {
            "status": "success",
            "database": "PostgreSQL connection successful",
            "test_result": value
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
from typing import Optional


@app.get("/roads")
def get_roads(
    limit: int = 100,
    offset: int = 0,
    risk_level: Optional[str] = None
):
    try:
        # Basic validation
        if limit < 1 or limit > 1000:
            return {
                "status": "error",
                "message": "limit must be between 1 and 1000"
            }

        if offset < 0:
            return {
                "status": "error",
                "message": "offset cannot be negative"
            }

        with engine.connect() as connection:

            if risk_level is None:
                result = connection.execute(
                    text("""
                        SELECT
                            road_id,
                            rainfall_score,
                            damage_score,
                            risk_score,
                            risk_level,
                            ST_AsGeoJSON(geometry) AS geometry
                        FROM public.road_risk_view
                        ORDER BY road_id
                        LIMIT :limit
                        OFFSET :offset
                    """),
                    {
                        "limit": limit,
                        "offset": offset
                    }
                )

            else:
                result = connection.execute(
                    text("""
                        SELECT
                            road_id,
                            rainfall_score,
                            damage_score,
                            risk_score,
                            risk_level,
                            ST_AsGeoJSON(geometry) AS geometry
                        FROM public.road_risk_view
                        WHERE UPPER(risk_level) = UPPER(:risk_level)
                        ORDER BY road_id
                        LIMIT :limit
                        OFFSET :offset
                    """),
                    {
                        "risk_level": risk_level,
                        "limit": limit,
                        "offset": offset
                    }
                )

            rows = result.mappings().all()

        import json

        data = []

        for row in rows:
            item = dict(row)

            if item["geometry"] is not None:
                item["geometry"] = json.loads(item["geometry"])

            data.append(item)

        return {
            "status": "success",
            "count": len(data),
            "limit": limit,
            "offset": offset,
            "risk_level": risk_level,
            "data": data
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

@app.get("/roads/{road_id}")
def get_road_details(road_id: str):
    try:
        with engine.connect() as connection:
            result = connection.execute(
                text("""
                    SELECT
                        road_id,
                        damage_type,
                        severity,
                        confidence,
                        detected_at,
                        total_rainfall_mm,
                        average_daily_rainfall_mm,
                        maximum_daily_rainfall_mm,
                        rainy_days,
                        heavy_rain_days,
                        rainfall_spatial_factor,
                        rainfall_score,
                        damage_score,
                        risk_score,
                        risk_level,
                        ST_AsGeoJSON(geometry) AS geometry
                    FROM public.road_risk_view
                    WHERE road_id = :road_id
                """),
                {"road_id": road_id}
            )

            row = result.mappings().first()

        if row is None:
            return {
                "status": "not_found",
                "message": f"Road {road_id} not found"
            }

        import json

        data = dict(row)

        if data["geometry"] is not None:
            data["geometry"] = json.loads(data["geometry"])

        return {
            "status": "success",
            "data": data
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

@app.get("/risk-summary")
def get_risk_summary():
    try:
        with engine.connect() as connection:
            result = connection.execute(
                text("""
                    SELECT
                        risk_level,
                        COUNT(*) AS road_count
                    FROM public.road_risk
                    GROUP BY risk_level
                    ORDER BY
                        CASE risk_level
                            WHEN 'CRITICAL' THEN 1
                            WHEN 'HIGH' THEN 2
                            WHEN 'MEDIUM' THEN 3
                            WHEN 'LOW' THEN 4
                        END
                """)
            )

            rows = result.mappings().all()

        return {
            "status": "success",
            "data": [dict(row) for row in rows]
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
@app.get("/damaged-roads")
def get_damaged_roads():
    try:
        with engine.connect() as connection:
            result = connection.execute(
                text("""
                    SELECT
                        road_id,
                        damage_type,
                        severity,
                        confidence,
                        detected_at,
                        rainfall_score,
                        damage_score,
                        risk_score,
                        risk_level
                    FROM public.road_risk_view
                    WHERE damage_type IS NOT NULL
                    ORDER BY risk_score DESC
                """)
            )

            rows = result.mappings().all()

        return {
            "status": "success",
            "count": len(rows),
            "data": [dict(row) for row in rows]
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }