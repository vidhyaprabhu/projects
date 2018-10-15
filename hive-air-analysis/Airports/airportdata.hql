use air_analysis;

CREATE TABLE IF NOT EXISTS airport_data
(
name STRING,
country STRING,
area_code INT,
code STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION '/sandbox/sandbox8/processed/air_analysis/airport_data/';