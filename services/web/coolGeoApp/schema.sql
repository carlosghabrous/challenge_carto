DROP TABLE IF EXISTS postal_codes;
DROP TABLE IF EXISTS paystats;
DROP TYPE IF EXISTS gender; 

CREATE TYPE gender AS ENUM('M', 'F');

CREATE TABLE postal_codes(
    id INTEGER PRIMARY KEY, 
    code INTEGER, 
    the_geom POLYGON
    );

CREATE TABLE paystats(
    id INTEGER PRIMARY KEY,
    p_month DATE,
    p_age int4range, 
    p_gender gender, 
    postal_code_id INTEGER, 
    amount NUMERIC(20, 10), 
    CONSTRAINT fk_postal_code_id FOREIGN KEY(postal_code_id) REFERENCES postal_codes(id), 
    UNIQUE (p_month, p_age, p_gender, postal_code_id, amount)
    );