# Understand the problem
# input: number of blocks
# output: number of remaining blocks

# explicit requirements:
# - top layer is 1 block
# - each block must be supported by 4 blocks in lower layer
#     - lower layer 4 blocks, upper layer 1-4 blocks
# - lower layer block can support more than 1 block in upper layer
# - no empty layers

# implicit requirements:
# - each lower layer must have number of blocks = layer number squared
# - start with 1 block on 1st layer
# - each successive layer does not have any extra blocks of support


# '''
# Data Structure:
# - List of integers representing number of blocks in each successive layer
# starting with the upper layer with 1 block
# - 1 block = [1]
# - 6 blocks = [1, 4]
# - 14 blocks = [1, 4, 9]
# - variable representing how many remaining blocks

# - or dictionary with key: value as row: blocks
# - 1 block = {1: 1}
# - 6 blocks = {1: 1, 2: 4}               # 1 blocks remaining
# - 14 blocks = {1: 1, 2: 4, 3: 9}        # 0 blocks remaining
# - 40 blocks = {1: 1, 2: 4, 3: 9, 4: 16}     # 10 blocks remaining
# '''

# """
# Algorithm:
# - initialize variable tower to empty dictionary
# - initiate variable blocks_remaining to initial number of blocks given
# - initialize variable layer_num to 1
# - loop through the number of blocks_remaining until it is less than the square
# of the layer number
# - append each layer to the tower dictionary with layer_num : layer_num squared
# - update the blocks_remaining by subtracting the layer_num squared
# - update the layer_num to next layer
# - after the loop stops, return the blocks_remaining
# """

def calculate_leftover_blocks(blocks):
    layers = {}
    blocks_remaining = blocks
    layer_num = 1
    blocks_required = layer_num**2

    while blocks_remaining >= blocks_required:
        layers[layer_num] = blocks_required
        blocks_remaining -= blocks_required
        layer_num += 1
        blocks_required = layer_num**2

    print(layers)
    return blocks_remaining

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
print(calculate_leftover_blocks(40) == 10) # True