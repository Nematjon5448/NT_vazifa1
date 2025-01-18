CREATE TABLE IF NOT EXISTS departaments(
	id SERIAL PRIMARY KEY,
	departament_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS employees(
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	position VARCHAR(100),
	salary INTEGER,
	hire_date DATE,
	departament_id INTEGER REFERENCES departaments(id)
);

CREATE TABLE IF NOT EXISTS projects(
	id SERIAL PRIMARY KEY,
	project_name VARCHAR(100),
	start_date DATE,
	end_date DATE,
	budget INTEGER
);

INSERT INTO departaments(departament_name)
VALUES	('Administration'),
	('IT'),
	('Design');

INSERT INTO employees(first_name, last_name, position, salary, hire_date, departament_id)
VALUES	('Ali', 'Karimov', 'Manager', 3000, TO_DATE('15.03.2020', 'dd.mm.yyyy'), 1),
	('Nodira', 'Toirova', 'Developer', 2500, TO_DATE('10.05.2021', 'dd.mm.yyyy'), 2),
	('Shoxruh', 'Abdullayev', 'Designer', 2200, TO_DATE('22.01.2022', 'dd.mm.yyyy'), 3),
	('Zarina', 'Abdullayeva', 'HR Specialist', 1800, TO_DATE('11.11.2019', 'dd.mm.yyyy'), 1),
	('Jasur', 'Aliyev', 'Developer', 2400, TO_DATE('01.02.2023', 'dd.mm.yyyy'), 2);

INSERT INTO projects(project_name, start_date, end_date, budget)
VALUES	('New Website', TO_DATE('10.01.2023', 'dd.mm.yyyy'), TO_DATE('30.06.2023', 'dd.mm.yyyy'), 50000),
	('Mobile App', TO_DATE('15.08.2022', 'dd.mm.yyyy'), TO_DATE('20.03.2023', 'dd.mm.yyyy'), 30000),
	('CRM System', TO_DATE('01.02.2024', 'dd.mm.yyyy'), NULL, 60000);

SELECT * FROM departaments;
SELECT * FROM employees;
SELECT * FROM projects;

SELECT first_name || ' ' || last_name as full_name FROM employees;

SELECT first_name, salary FROM employees
ORDER BY salary DESC;

SELECT first_name, salary FROM employees
WHERE salary >= 2500;

SELECT first_name, salary FROM employees
ORDER BY salary DESC
FETCH FIRST 3 ROW ONLY;

SELECT first_name, salary FROM employees
ORDER BY salary DESC
LIMIT 3;

SELECT first_name, salary FROM employees
WHERE salary IN(2400, 3000);

SELECT first_name, salary FROM employees
WHERE salary BETWEEN 2000 AND 3000;

SELECT first_name FROM employees
WHERE first_name LIKE '%a%';

SELECT * FROM projects
WHERE end_date IS NULL;

SELECT avg(salary) FROM employees;