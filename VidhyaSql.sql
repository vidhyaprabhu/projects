create database jstor_books;

use jstor_books;

create table jstor_books.jbooks_internal
(
book_name varchar(50) not null,
employee_id int not null,
employee_name varchar (100),
employee_date date,
file_status varchar(25) not null,
primary key (employee_id)
)

select * from jbooks_internal;
desc jbooks_internal;



create table jbooks_employeedetails
(
Employee_id int not null,
employee_Name varchar(100) not null,
Employee_dateofjoin date not null,
employee_designation varchar(25) not null,
primary key(Employee_id)
);
select * from jbooks_internal;

create table jbooksfile_process
(
file_name varchar(30),
PPA varchar(10),
PPA_status varchar(10),
Analyzer varchar(10),
Analyzer_status varchar(10),
Analyzer_QA varchar(10),
AnalyzerQA_status varchar(10),
Collate1 varchar (10),
Validation1 varchar(10),
Audit varchar (10),
client_status varchar(10),
primary key(fie_name)
);

desc jbooksfile_process;

select e.employee_name, i.employee_date
from jbooks_internal i JOIN jbooks_employeedetails e ON i.employee_id = e.employee_id;

create procedure jstor_books.everyday_work
(
 int @LastName
)
as
begin
select  employee_id, employee_name
from jbooks_internal;
end

CALL everyday_work (2012-08-09);
									










                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

























