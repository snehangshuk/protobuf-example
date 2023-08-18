from pathlib import Path
from prettytable import PrettyTable
import employee_pb2 as EmployeeList

output_path = Path('output')
# Create the directory if it doesn't exist
output_path.mkdir(exist_ok=True)
file_path = output_path / 'binary.bin'
# Write binary data into file
with file_path.open('rb') as file:
    buf = file.read()
    employee_list = EmployeeList.Employees()
    employee_list.ParseFromString(buf)
    table = PrettyTable()
    table.field_names = ["Name", "Age", "City"]

    for employee in employee_list.employees:
        table.add_row([employee.name, employee.age, employee.city])
print(table)
