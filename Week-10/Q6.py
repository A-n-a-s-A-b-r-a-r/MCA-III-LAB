def merge_employee_department(emp_file, dept_file, output_file):
    employees = {}
    
    with open(emp_file, 'r') as ef:
        for line in ef:
            name, eid, salary, did = line.strip().split(',')
            employees[did] = (name, eid, salary)
    
    with open(dept_file, 'r') as df:
        departments = {}
        for line in df:
            did, dname, dlocation = line.strip().split(',')
            departments[did] = (dname, dlocation)
    
    with open(output_file, 'w') as of:
        for did, emp in employees.items():
            if did in departments:
                dname, dlocation = departments[did]
                of.write(f"{emp[0]},{emp[1]},{emp[2]},{did},{dname},{dlocation}\n")

# Example usage
merge_employee_department('Week-10/employees.csv', 'Week-10/departments.csv', 'merged_output.csv')
