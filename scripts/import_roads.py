import os
import geopandas as gpd

from sqlalchemy import create_engine
from sqlalchemy.engine import URL


DB_HOST = "127.0.0.1"
DB_PORT = 5432
DB_NAME = "infra_sheild_db"
DB_USER = "postgres"
DB_PASSWORD = os.getenv("DB_PASSWORD")


geojson_file = "../data/clean/lucknow_roads_clean.geojson"


print("========================================")
print("       BHARAT INFRAGRID")
print("       ROAD DATA IMPORT")
print("========================================")


print("\n[1] Reading clean GeoJSON...")

roads = gpd.read_file(geojson_file)

print("Records found:", len(roads))
print("CRS:", roads.crs)
print("Geometry:", roads.geometry.geom_type.unique())


print("\n[2] Connecting to PostgreSQL...")


connection_url = URL.create(
    drivername="postgresql+psycopg2",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME
)

engine = create_engine(connection_url)

print("PostgreSQL connection ready.")


print("\n[3] Importing roads into PostgreSQL...")
print("This may take some time...")


roads.to_postgis(
    name="roads",
    con=engine,
    if_exists="replace",
    index=False
)


print("\n========================================")
print("IMPORT COMPLETED SUCCESSFULLY! ✅")
print("========================================")

print("Table name: roads")
print("Records imported:", len(roads))
