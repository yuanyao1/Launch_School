# Write a function that takes no arguments and
# returns a string that contains a UUID
# expected format: 8-4-4-4-12 pattern
# 'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'

import random
# CHARACTERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
#               'a', 'b', 'c', 'd', 'e', 'f')

# PATTERN = [8, 4, 4, 4, 12]

# def get_uuid():
#     uuid = []
#     sub_id = ''

#     for num in PATTERN:
#         for _ in range(num):
#             sub_id += random.choice(CHARACTERS)
#         uuid.append(sub_id)
#         sub_id = ''
    
#     return '-'.join(uuid)

characters = '0123456789abcdef'
sections = [8, 4, 4, 4, 12]

def get_uuid():
    uuid = []

    for section in sections:
        sub_id = [random.choice(characters) for _ in range(section)]
        uuid.append(''.join(sub_id))
    
    return '-'.join(uuid)

print(get_uuid())
