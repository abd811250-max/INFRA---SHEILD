-- Table: public.road_damage

-- DROP TABLE IF EXISTS public.road_damage;

CREATE TABLE IF NOT EXISTS public.road_damage
(
    damage_id bigserial NOT NULL,
    road_id character varying COLLATE pg_catalog."default" NOT NULL,
    damage_type character varying(50) COLLATE pg_catalog."default" NOT NULL,
    severity character varying(20) COLLATE pg_catalog."default",
    confidence numeric(5,2),
    detected_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    image_path text COLLATE pg_catalog."default",
    notes text COLLATE pg_catalog."default",
    CONSTRAINT road_damage_pkey PRIMARY KEY (damage_id),
    CONSTRAINT fk_road_damage_road FOREIGN KEY (road_id)
        REFERENCES public.roads (road_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.road_damage
    OWNER to postgres;


-- Table: public.roads

-- DROP TABLE IF EXISTS public.roads;

CREATE TABLE IF NOT EXISTS public.roads
(
    road_id text COLLATE pg_catalog."default" NOT NULL,
    osmid text COLLATE pg_catalog."default",
    road_name text COLLATE pg_catalog."default",
    road_ref text COLLATE pg_catalog."default",
    road_type text COLLATE pg_catalog."default",
    lanes text COLLATE pg_catalog."default",
    oneway boolean,
    reversed text COLLATE pg_catalog."default",
    length double precision,
    bridge text COLLATE pg_catalog."default",
    maxspeed text COLLATE pg_catalog."default",
    junction text COLLATE pg_catalog."default",
    access text COLLATE pg_catalog."default",
    tunnel text COLLATE pg_catalog."default",
    width text COLLATE pg_catalog."default",
    service text COLLATE pg_catalog."default",
    city text COLLATE pg_catalog."default",
    state text COLLATE pg_catalog."default",
    geometry geometry(LineString,4326),
    CONSTRAINT roads_pkey PRIMARY KEY (road_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.roads
    OWNER to postgres;
-- Index: idx_roads_geometry

-- DROP INDEX IF EXISTS public.idx_roads_geometry;

CREATE INDEX IF NOT EXISTS idx_roads_geometry
    ON public.roads USING gist
    (geometry)
    TABLESPACE pg_default;
-- Index: roads_city_idx

-- DROP INDEX IF EXISTS public.roads_city_idx;

CREATE INDEX IF NOT EXISTS roads_city_idx
    ON public.roads USING btree
    (city COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: roads_geometry_idx

-- DROP INDEX IF EXISTS public.roads_geometry_idx;

CREATE INDEX IF NOT EXISTS roads_geometry_idx
    ON public.roads USING gist
    (geometry)
    TABLESPACE pg_default;
-- Index: roads_road_type_idx

-- DROP INDEX IF EXISTS public.roads_road_type_idx;

CREATE INDEX IF NOT EXISTS roads_road_type_idx
    ON public.roads USING btree
    (road_type COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: roads_state_idx

-- DROP INDEX IF EXISTS public.roads_state_idx;

CREATE INDEX IF NOT EXISTS roads_state_idx
    ON public.roads USING btree
    (state COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
