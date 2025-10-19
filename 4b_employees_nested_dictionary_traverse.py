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


def traverse_dict_with_path(dictionary, path=""):
    for key, value in dictionary.items():
        new_path = path + "/" + key if path else key
        if isinstance(value, dict):
            traverse_dict_with_path(value, new_path)
        elif isinstance(value, list):
            for item in value:
                print(new_path, item)
        else:
            print(new_path, value)


traverse_dict_with_path(employees)
