use air_analysis;

CREATE TABLE IF  NOT EXISTS flights_dataclustered
(
    year INT,
   day INT,
   month INT,
   day_of_week INT,
   dep_time INT,
   crs_dep_time INT,
   arr_time INT,
   crs_arr_time INT,
   unique_carrier STRING,
   flight_num INT,
   tail_num STRING,
   actual_elapsed_time INT,
   crs_elapsed_time INT,
   air_time INT,
   arr_delay INT,
   dep_delay INT,
   origin STRING,
   dest STRING,
   distance INT,
   taxi_in INT,
   taxi_out INT,
   cancelled INT,
   cancellation_code STRING,
   diverted INT,
   carrier_delay STRING,
   weather_delay STRING,
   nas_delay STRING,
   security_delay STRING,
   late_aircraft_delay STRING
)
CLUSTERED BY (month) into 6 buckets
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ","
LOCATION '/sandbox/sandbox8/processed/air_analysis/flights_dataclustered/';

INSERT INTO flights_dataclustered  select year,month,day,day_of_week,dep_time,crs_dep_time,arr_time,crs_arr_time,unique_carrier,flight_num,tail_num,actual_elapsed_time,crs_elapsed_time,air_time,arr_delay,dep_delay,origin,dest,distance,taxi_in,taxi_out,cancelled,cancellation_code,diverted,carrier_delay,weather_delay,nas_delay,security_delay,late_aircraft_delay from flights_data;

    

