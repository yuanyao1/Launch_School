import copy

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    # sub_list_copy = copy.deepcopy(sub_list)
    matrix.append(copy.deepcopy(sub_list))

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]

matrix[1][0] = 'O'
print(matrix)