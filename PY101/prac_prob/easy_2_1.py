def greetings(name_parts, role):
    name = " ".join(name_parts)
    return (f'Hello, {name}! Nice to have a {role["title"]} '
            f'{role["occupation"]} around')
            



greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.