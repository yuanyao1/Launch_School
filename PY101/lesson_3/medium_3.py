

def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    print(f'function buffer is {buffer}')
    print(f'id of buffer is {id(buffer)}')
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    print(f'function buffer is {buffer}')
    print(f'id of buffer is {id(buffer)}')
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

max_size = 3
buff = ['dog']


for index in range(1, 6):
    # result_1 = add_to_rolling_buffer1(buff, max_size, index)
    # print(f'result is {result_1}')
    # print(f'buff is {buff}')
    # print(f'id of buff is {id(buff)}')

    result_2 = add_to_rolling_buffer2(buff, max_size, index)
    print(f'result is {result_2}')
    print(f'buff is {buff}')
    print(f'id of buff is {id(buff)}')