from pathlib import Path
from prettytable import PrettyTable
from employee_pb2 import Employees as EmployeeList, EmployeeType

output_path = Path('output')
# Create the directory if it doesn't exist
output_path.mkdir(exist_ok=True)
file_path = output_path / 'binary.bin'
# Write binary data into file
with file_path.open('rb') as file:
    buf = file.read()
    deserialized_employee = EmployeeList()
    deserialized_employee.ParseFromString(buf)
    table = PrettyTable()
    table.field_names = ["Name", "Age", "City", "Employee Type"]

    for employee in deserialized_employee.employees:
        table.add_row([
            employee.name,
            employee.age,
            employee.city,
            EmployeeType.Name(employee.employee_type)
        ])
print(table)
