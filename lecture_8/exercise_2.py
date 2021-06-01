class Employee:
    def __init__(self, name, age, salary):
        # Initializing class properties.
        self.name = name
        self.age = age
        self.salary = salary

    def get_details(self):
        return 'My name is {} my age is {} and I make {}'.format(self.name, self.age, self.salary)


class Company:
    def __init__(self):
        # Creating empty list of employees for each instance!
        self.employees = []

    def add_employee(self, employee):
        # Adding the employee which is an instance of the class Employee
        self.employees.append(employee)

    def get_total_salary(self):
        # Going through all the employees in the list and summing up their salaries.
        s = 0
        for i in range(len(self.employees)):
            s += self.employees[i].salary
        return s


# Creating instance of type company
company = Company()
# Creating employees instances
ethan = Employee('ethan', 26, 50)
israel = Employee('israel', 28, 100)
rasan = Employee('rasan', 29, 150)

# Adding the employees to the company.
company.add_employee(ethan)
company.add_employee(israel)
company.add_employee(rasan)
print(company.get_total_salary())
