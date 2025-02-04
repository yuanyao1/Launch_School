# def print_in_box(text):
#     top_bottom_line = f"+-{len(text) * "-"}-+"
#     blank_line = f"| {len(text) * " "} |"
#     text_line = f"| {text} |"

#     print(top_bottom_line)
#     print(blank_line)
#     print(text_line)
#     print(blank_line)
#     print(top_bottom_line)


# def print_in_box(text, width = float('inf')):
#     top_bottom_line = f"+-{len(text) * "-"}-+"
#     blank_line = f"| {len(text) * " "} |"
#     text_line = f"| {text} |"

#     if width <= 4:
#         text = ""
#         top_bottom_line = f"+-{len(text) * "-"}-+"
#         blank_line = f"| {len(text) * " "} |"
#         text_line = f"| {text} |"
#     elif len(text) + 4 > width:
#         text = text[0:(width - 4)]
#         top_bottom_line = f"+-{len(text) * "-"}-+"
#         blank_line = f"| {len(text) * " "} |"
#         text_line = f"| {text} |"

#     print(text)
#     print(top_bottom_line)
#     print(blank_line)
#     print(text_line)
#     print(blank_line)
#     print(top_bottom_line)

def print_in_box(text, width = float('inf')):
    # text = text.strip()
    # top_bottom_line = f"+-{len(text) * "-"}-+"
    # blank_line = f"| {len(text) * " "} |"
    # text_line = f"| {text} |"

    # if text is multiple words and length is greater than width - 4, split the
    # text apart into separate words
    # insert the words into the current line within the width and print
    # maybe pop off those words into the current line and continue doing
    # the same until the words are done
    # if an individual word does not fit then put letters into separate lines

    # if len(text) + 4 > width and bool(text.find(" ")):
        working_text = ''
        remaining_text = text

        if len(remaining_text) >= width - 4 - len(text):
            print(width - 4 - len(text))
            space_index = text.rfind(" ")
            working_text += text[0:space_index]
            remaining_text = text[space_index::]
            print(f'working: {working_text}')
            print(f'remaining: {remaining_text}')



    # if width <= 4:
    #     text = ""
    #     top_bottom_line = f"+-{len(text) * "-"}-+"
    #     blank_line = f"| {len(text) * " "} |"
    #     text_line = f"| {text} |"
    # elif len(text) + 4 > width:
    #     text = text[0:(width - 4)]
    #     top_bottom_line = f"+-{len(text) * "-"}-+"
    #     blank_line = f"| {len(text) * " "} |"
    #     text_line = f"| {text} |"

    # print(text)
    # print(top_bottom_line)
    # print(blank_line)




    # print(text_line)
    # print(blank_line)
    # print(top_bottom_line)



# print_in_box("", 4)
# print_in_box('a', 4)
# print_in_box('abcd')
# print_in_box('abcd', 5)
# print_in_box('abcd', 6)
# print_in_box('abcd', 7)
# print_in_box('abcd', 8)
# print_in_box('abcd', 9)
# print_in_box('To boldly go where no one has gone before.', 10)
print_in_box('hello world', 6)
# print_in_box('')