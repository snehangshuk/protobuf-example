# write a code to generate JSON file and write in a file
import json
from pathlib import Path
from enum import Enum, auto


class EmployeeType(Enum):
    FULL_TIME = auto()
    PART_TIME = auto()
    CONTRACT = auto()
    INTERN = auto()


class Employee:
    def __init__(self, name, age, city, employee_type=EmployeeType.FULL_TIME):
        self.name = name
        self.age = age
        self.city = city
        self.employee_type = employee_type.name

    # Optional: Method to represent the object as a dictionary
    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "city": self.city,
            "employee_type": self.employee_type
        }


employee1 = Employee("Rajesh", 30, "Bangalore")
employee2 = Employee("Snehangshu", 30, "Bangalore", EmployeeType.PART_TIME)
employee3 = Employee("Somangshu", 11, "Bangalore", EmployeeType.INTERN)

employees = [employee1, employee2, employee3]

# Convert the employees to a JSON-like structure
employees_json = [employee.to_dict() for employee in employees]

output_path = Path('output')
# Create the directory if it doesn't exist
output_path.mkdir(exist_ok=True)
file_path = output_path / 'data.json'
# Write JSON data into file
with file_path.open('w') as file:
    json.dump(employees_json, file, indent=4)
