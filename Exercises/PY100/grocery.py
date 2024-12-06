grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

print(grocery_list)

index = 0
while index < len(grocery_list):
    print(grocery_list[index])
    grocery_list.pop(index)



print(grocery_list)