def select_fruit(food):
    fruit = {}
    fruit = {key: value for key, value in food.items() if value == 'Fruit'}
    # for key, value in food.items():
    #     if value == 'Fruit':
    #         fruit[key] = value

    return fruit

produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }