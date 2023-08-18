from employee_pb2 import Employees as EmployeeList, EmployeeType, Employee
from pathlib import Path


employee1 = Employee()
employee1.name = "Rajesh"
employee1.age = 30
employee1.city = "Bangalore"

employee2 = Employee()
employee2.name = "Snehangshu"
employee2.age = 30
employee2.city = "Bangalore"
employee2.employee_type = EmployeeType.PART_TIME

employee3 = Employee()
employee3.name = "Somangshu"
employee3.age = 11
employee3.city = "Bangalore"
employee3.employee_type = EmployeeType.INTERN


employee_list = EmployeeList()
employee_list.employees.extend([employee1, employee2, employee3])
serialized_employee = employee_list.SerializeToString()


output_path = Path('output')
# Create the directory if it doesn't exist
output_path.mkdir(exist_ok=True)
file_path = output_path / 'binary.bin'
# Write binary data into file
with file_path.open('wb') as file:
    file.write(serialized_employee)
