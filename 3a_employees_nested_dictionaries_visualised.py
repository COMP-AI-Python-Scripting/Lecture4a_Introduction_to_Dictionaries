from lolviz import objviz

employees = {
    "employee1": {
        "name": {"firstname": "albert", "lastname": "einstein"},
        "age": 40,
        "address": {
            "number": 38,
            "street": "alclutha avenue",
            "town": "nobelprizetown",
            "county": "donegal",
        },
    },
    "employee2": {
        "name": {"firstname": "rosalind", "lastname": "franklin"},
        "age": 30,
        "address": {
            "number": 4,
            "street": "geils avenue",
            "town": "biologyprizetown",
            "county": "donegal",
        },
    },
    "employee3": {
        "name": {"firstname": "linus", "lastname": "pauling"},
        "age": 45,
        "address": {
            "number": 10,
            "street": "silverton avenue",
            "town": "chemistryprizetown",
            "county": "donegal",
        },
    },
}

g = objviz(employees)
g.view(cleanup=True, quiet=True)

for k, v in employees.items():
    print(f"{str(k).title()} Record:")
    print(
        f"Name: {employees[k]['name']['firstname'].title()} "
        f"{employees[k]['name']['lastname'].title()}"
    )
    print(f"Age: {employees[k]['age']}")
    print(
        f"Street: {employees[k]['address']['number']} "
        f"{employees[k]['address']['street'].title()}"
    )
    print(f"Town: {employees[k]['address']['town'].title()}")
    print(f"County: {employees[k]['address']['county'].title()}")
    print()
