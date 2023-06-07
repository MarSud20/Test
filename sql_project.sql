select * from project;

TRUNCATE TABLE project;

SELECT user, host, plugin, authentication_string FROM mysql.user;

show variables where Variable_name like '%host%';

insert into project(day, month, numbers_of_sale) values
(1, 'May', 76),
(2, 'May', 88),
(3, 'May', 99),
(4, 'May', 110),
(5, 'May', 120),
(6, 'May', 91),
(7, 'May', 79),
(8, 'May', 49),
(9, 'May', 86),
(10, 'May', 100),
(11, 'May', 150);