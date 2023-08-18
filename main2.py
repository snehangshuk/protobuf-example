import employee_pb2 as EmployeeList
from pathlib import Path


employee1 = EmployeeList.Employee()
employee1.name = "Rajesh"
employee1.age = 30
employee1.city = "Bangalore"

employee2 = EmployeeList.Employee()
employee2.name = "Snehangshu"
employee2.age = 30
employee2.city = "Bangalore"

employee3 = EmployeeList.Employee()
employee3.name = "Somangshu"
employee3.age = 11
employee3.city = "Bangalore"


employee_list = EmployeeList.Employees()
employee_list.employees.extend([employee1, employee2, employee3])


output_path = Path('output')
# Create the directory if it doesn't exist
output_path.mkdir(exist_ok=True)
file_path = output_path / 'binary.bin'
# Write binary data into file
with file_path.open('wb') as file:
    file.write(employee_list.SerializeToString())
