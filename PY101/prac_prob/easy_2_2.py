def prompt(msg):
    print(f'>== {msg}')

prompt("What is your name?")
name = input()

# while name.isalpha() is False:
#     prompt("Please give a real name:")
#     name = input()

if name.endswith("!"):
    print(f"HELLO {name.upper()} WHY ARE WE YELLING?")
else:
    print(f"Hello {name}")
