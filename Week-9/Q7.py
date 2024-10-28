def add_hra_column(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open('updated_employees.csv', 'w') as file:
        for line in lines:
            name, emp_id, salary, dname = line.strip().split(',')
            hra = round(0.18 * float(salary), 2)
            file.write(f"{name},{emp_id},{salary},{dname},{hra}\n")

# Example usage
add_hra_column('Week-9/employees.csv')
