#list some rows from the airports table:
ans: 
hive> select * from airport_data limit 5;
OK
output:
Key West Nas /Boca Chica Field (private U. S. Navy )	US	67	NQX
A L Mangham Jr. Regional	US	67	OCH
AAF Heliport	US	67	AYE
Aberdeen Regional	US	67	ABR
Abilene Regional	US	67	ABI
Time taken: 0.641 seconds, Fetched: 5 row(s)

2. run a join query to find the average delay in January 2008 for each airport and to print out the airport's name:
Ans: 
hive> select a.name, AVG(arr_delay) AS avgdelay from flights_data f JOIN airport_data a ON f.origin = a.code WHERE month = 1 AND year = 2008 GROUP BY a.name ORDER BY avgdelay desc;
Query ID = pg8464_20181014195130_8f04d129-601f-4fbe-9634-9b57b2bfa0aa
Total jobs = 1
Launching Job 1 out of 1
OUTPUT:
Rafael Hernández	-5.379032258064516
Minot International	-5.440860215053763
Bellingham International	-6.666666666666667
Jack Brooks Regional	-7.368421052631579
Time taken: 25.729 seconds, Fetched: 285 row(s)

3.Find average arrival delay for all flights departing SFO in January:
ans:
hive> select AVG(arr_delay)AS averagedelay from flights_data WHERE origin = 'SFO' AND month = 1 ORDER BY averagedelay; 
Query ID = pg8464_20181014200626_37ecbc22-ddf4-4294-9c10-b32f705a300a
Total jobs = 1
Launching Job 1 out of 1
Status: Running (Executing on YARN cluster with App id application_1539374
