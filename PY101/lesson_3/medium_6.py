import copy

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    working_dict = copy.deepcopy(demo_dict)
    for key, value in working_dict.items():
        value["age"] += 42
        value["gender"] = "other"

mess_with_demographics(munsters)
print(munsters)