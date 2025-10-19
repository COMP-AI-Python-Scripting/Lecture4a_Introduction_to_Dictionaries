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
        "subject": ["math", "history", "science", "physics"],
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


def traverse_dict(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            traverse_dict(value)
        elif isinstance(value, list):
            print(f"{key}", end=": ")
            for item in value:
                print(f"{item}", end=", ")
            print()
        else:
            print(f"{key} -> {value}")


traverse_dict(employees)
