# def repeat(string, reps):
#     for _ in range(reps):
#         print(string)

def repeat(string, reps):
    print("\n".join([string] * reps))

repeat('Hello there', 6)