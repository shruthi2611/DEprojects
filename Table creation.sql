create table Before_after_school_information(
           Program_name varchar(200) not null,
           Capacity int,
           Vacancy varchar(20),
           Quality_rating varchar(30),
           Center_name varchar(300) not null,
           before_after_school_program varchar(20),
           Center_address varchar(300))


create table Early_years_program_information(
           Program_name varchar(200) not null,
           Capacity int,
           Vacancy varchar(20),
           Quality_rating varchar(30),
           Center_name varchar(300) not null,
           before_after_school_program varchar(20),
           Center_address varchar(300))

create table Centre_information(
           Center_name varchar(300) not null,
           Center_address varchar(300),
           Ward varchar(200),
           Age varchar(20),
           Contact varchar(200))