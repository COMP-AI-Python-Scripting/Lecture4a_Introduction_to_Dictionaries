employees = {
    "employee1": {"name": "albert", "age": 40},
    "employee2": {"name": "rosalind", "age": 30},
    "employee3": {"name": "linus", "age": 45},
}

print("Iterate through the keys of employee" " and get the employee name and age.")

for k in employees.keys():
    print(
        f"Employee {k} is {employees[k]['name'].title()} and their age is {employees[k]['age']}"
    )
