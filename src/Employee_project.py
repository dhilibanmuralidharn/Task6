# Step 1: Base Class
class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary  # Default, overridden in subclasses


# Step 2: Subclasses

# Regular Employee
class RegularEmployee(Employee):
    def __init__(self, name, salary, bonus, deductions):
        super().__init__(name, salary)
        self.bonus = bonus
        self.deductions = deductions

    def calculate_salary(self):
        return self.salary + self.bonus - self.deductions


# Contract Employee
class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


# Manager
class Manager(Employee):
    def __init__(self, name, salary, incentives, bonus):
        super().__init__(name, salary)
        self.incentives = incentives
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.incentives + self.bonus
