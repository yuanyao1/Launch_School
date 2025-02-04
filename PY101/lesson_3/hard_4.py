def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False
    
    while len(dot_separated_words):
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True

def is_an_ip_number(input_word):
    if input_word.isdigit():
        number = int(input_word)
        return 0 <= number <= 255
    return False

a_string = '10.4.50.300'

print(is_dot_separated_ip_address(a_string))