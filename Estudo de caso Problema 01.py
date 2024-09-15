class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    
    def calculate_emp_salary(self, salary, worked_hours):
        office_hours = 50
        
        if worked_hours > 50:
            overtime = worked_hours - office_hours
            overtime_pay = 1.5 * (overtime * (salary/office_hours))
            salary_end = overtime_pay + salary
        else:
            salary_end = salary
        return salary_end
            
        
    def emp_assign_department(self, change_department):
        self.emp_department = change_department

    
    def print_employee_details(self):
        print(f"Id: {self.emp_id}")
        print(f"Name: {self.emp_name}")
        print(f"Salary: {self.emp_salary}")
        print(f"Department: {self.emp_department}")

employee1 = Employee("UZZI", "E7876", 50000, "ACCOUNTING")
employee2 = Employee("JOÃO", "E7499", 45000, "RESEARCH")
employee3 = Employee("SALVADOR", "E7900", 50000, "SALES")
employee4 = Employee("DENIS", "E7698", 55000, "OPERATIONS")


print("Detalhes do Funcionário 1:")
employee1.print_employee_details()
print("\n")
print("Detalhes do Funcionário 2:")
employee2.print_employee_details()
print("\n")
print("Detalhes do Funcionário 3:")
employee3.print_employee_details()
print("\n")
worked_hours = 60


print(f"Salário do Funcionário 1 com {worked_hours} horas trabalhadas: {employee1.calculate_emp_salary(employee1.emp_salary, worked_hours)}")
print(f"Salário do Funcionário 2 com {worked_hours} horas trabalhadas: {employee2.calculate_emp_salary(employee2.emp_salary, worked_hours)}")
print(f"Salário do Funcionário 3 com {worked_hours} horas trabalhadas: {employee3.calculate_emp_salary(employee3.emp_salary, worked_hours)}")
print(f"Salário do Funcionário 4 com {worked_hours} horas trabalhadas: {employee4.calculate_emp_salary(employee4.emp_salary, worked_hours)}")


employee1.emp_assign_department("FINANCE")
print("\nDetalhes atualizados do Funcionário 1:")
employee1.print_employee_details()
    