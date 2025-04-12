dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def get_info(produce):
    if produce['type'] == 'fruit':
        colors = [color.capitalize() for color in produce['colors']]
        return colors
    if produce['type'] == 'vegetable':
        return produce['size'].upper()

result = [get_info(value) for value in dict1.values()]
# result = []
# for value in dict1.values():
#     result.append(get_info(value))

print(result)

# Expected Output: [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]
# sizes of vegetables UPPERCASE
# colors of fruits Capitalized