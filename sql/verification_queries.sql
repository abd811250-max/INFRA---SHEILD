-- ============================================
-- INFRA SHEILD
-- Database Verification Queries
-- ============================================


-- 1. Check total number of roads
SELECT COUNT(*) AS total_roads
FROM roads;


-- 2. Check geometry type of roads
SELECT
    COUNT(*) AS total_roads,
    ST_GeometryType(geometry) AS geometry_type
FROM roads
GROUP BY ST_GeometryType(geometry);


-- 3. Check SRID
SELECT DISTINCT ST_SRID(geometry) AS srid
FROM roads;


-- 4. Validate road_id
SELECT
    COUNT(*) AS total_rows,
    COUNT(road_id) AS non_null_ids,
    COUNT(DISTINCT road_id) AS unique_ids
FROM roads;


-- 5. Check duplicate road IDs
SELECT
    road_id,
    COUNT(*) AS duplicate_count
FROM roads
GROUP BY road_id
HAVING COUNT(*) > 1;


-- 6. Check NULL road IDs
SELECT COUNT(*) AS null_road_ids
FROM roads
WHERE road_id IS NULL;


-- 7. Test roads and road_damage relationship
SELECT
    r.road_id,
    r.road_name,
    r.road_type,
    d.damage_type,
    d.severity,
    d.confidence
FROM roads r
JOIN road_damage d
    ON r.road_id = d.road_id;
