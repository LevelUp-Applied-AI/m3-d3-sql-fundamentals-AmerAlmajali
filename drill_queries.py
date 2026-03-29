import sqlite3


# Task 1
def top_departments(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = """
    SELECT d.name, SUM(e.salary) AS total_salary
    FROM employees e
    JOIN departments d ON e.department_id = d.id
    GROUP BY d.name
    ORDER BY total_salary DESC
    LIMIT 3;
    """

    cursor.execute(query)
    result = cursor.fetchall()

    conn.close()
    return result


# Task 2
def employees_with_projects(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = """
    SELECT e.name, p.name
    FROM employees e
    INNER JOIN project_assignments pa ON e.id = pa.employee_id
    INNER JOIN projects p ON pa.project_id = p.id;
    """

    cursor.execute(query)
    result = cursor.fetchall()

    conn.close()
    return result


# Task 3
def salary_rank_by_department(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = """
    SELECT 
        e.name,
        d.name,
        e.salary,
        RANK() OVER(
            PARTITION BY e.department_id
            ORDER BY e.salary DESC
        ) AS rank
    FROM employees e
    JOIN departments d ON e.department_id = d.id
    ORDER BY d.name, rank;
    """

    cursor.execute(query)
    result = cursor.fetchall()

    conn.close()
    return result