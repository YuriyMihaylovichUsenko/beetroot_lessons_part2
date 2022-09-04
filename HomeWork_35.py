from HomeWork_34 import create_connect, execute_select
from pprint import pprint

connection = create_connect('hr.db')

# 1. write a query in SQL to display the first name, last name, department
# number, and department name for each employee
query = """SELECT first_name, last_name, depart_name, department_id
 FROM employees left join departments using (department_id)
 """

# pprint(execute_select(connection, query))

# 2. write a query in SQL to display the first and last name, department,
# city, and state province for each employee
query = """
SELECT first_name || ' ' || last_name, depart_name, city, state_province
FROM employees left join departments using (department_id)
join locations using (location_id)
"""

# pprint(execute_select(connection, query))

# 3. write a query in SQL to display the first name, last name, department
# number, and department name, for all employees for departments 80 or 40
query = """SELECT first_name, last_name, depart_name, department_id
 FROM employees left join departments using (department_id)
 where department_id = 40 or department_id = 80
"""

# pprint(execute_select(connection, query))

# 4. write a query in SQL to display all departments including those where
# does not have any employee
query = """SELECT distinct depart_name FROM departments
"""

# pprint(execute_select(connection, query))

# 5. write a query in SQL to display the first name of all employees including
# the first name of their manager
query = """SELECT employees.first_name, em.first_name
FROM employees
join employees as em on employees.employee_id = em.manager_id
"""

pprint(execute_select(connection, query))

# 6. write a query in SQL to display the job title, full name (first and last
# name ) of the employee, and the difference between the maximum salary for the
# job and the salary of the employee
query = """SELECT job_title,  first_name || ' ' || last_name, 
max_salary - salary
FROM employees join jobs using (job_id)
"""

# pprint(execute_select(connection, query))

# 7. write a query in SQL to display the job title and the average salary of
# employees
query = """SELECT job_title, avg(salary) 
FROM employees join jobs using (job_id)
group by job_title
"""

# pprint(execute_select(connection, query))

# 8. write a query in SQL to display the full name (first and last name), and
# salary of those employees who work in any department located in London
query = """SELECT first_name || ' ' || last_name, salary 
FROM employees join departments using (department_id)
join locations using (location_id)
where city = 'London'
"""

# pprint(execute_select(connection, query))

# 9. write a query in SQL to display the department name and the number of
# employees in each department
query = """SELECT depart_name, count(*) 
FROM departments join employees using (department_id)
group by depart_name
order by count(*) desc 
"""

# pprint(execute_select(connection, query))

