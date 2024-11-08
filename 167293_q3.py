class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Updated salary for {self.name} to {self.salary}")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added {employee.name} to {self.department_name} department.")

    def total_salary_expenditure(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for {self.department_name} department: {total_salary}")
        return total_salary

    def display_all_employees(self):
        if self.employees:
            print(f"Employees in {self.department_name} department:")
            for employee in self.employees:
                employee.display_details()
        else:
            print(f"No employees in {self.department_name} department.")


# Interactive code for managing employees and departments
if __name__ == "__main__":
    # Initialize a department
    department = Department("Engineering")

    while True:
        print("\nDepartment Management System")
        print("1. Add an employee")
        print("2. Update an employee's salary")
        print("3. Display all employees")
        print("4. Display total salary expenditure")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            # Add an employee
            name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            try:
                salary = float(input("Enter employee salary: "))
                new_employee = Employee(name, employee_id, salary)
                department.add_employee(new_employee)
            except ValueError:
                print("Invalid salary. Please enter a number.")

        elif choice == '2':
            # Update an employee's salary
            employee_id = input("Enter employee ID to update salary: ")
            try:
                new_salary = float(input("Enter the new salary: "))
                employee_found = False
                for employee in department.employees:
                    if employee.employee_id == employee_id:
                        employee.update_salary(new_salary)
                        employee_found = True
                        break
                if not employee_found:
                    print("Employee not found.")
            except ValueError:
                print("Invalid salary. Please enter a number.")

        elif choice == '3':
            # Display all employees
            department.display_all_employees()

        elif choice == '4':
            # Display total salary expenditure
            department.total_salary_expenditure()

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid option. Please try again.")
