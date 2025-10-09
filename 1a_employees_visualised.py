from lolviz import objviz

employees = {
    "employee1": {"name": "albert", "age": 40},
    "employee2": {"name": "rosalind", "age": 30},
    "employee3": {"name": "linus", "age": 45},
}

g = objviz(employees)
g.view(cleanup=True, quiet=True)

print(employees["employee1"]["name"])
print(employees["employee1"]["age"])
print(employees["employee2"]["name"])
print(employees["employee2"]["age"])
print(employees["employee3"]["name"])
print(employees["employee3"]["age"])
