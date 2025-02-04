def prompt(msg):
    print(f'>== {msg}')

prompt('Enter a noun: ')
noun = input()

prompt('Enter a verb: ')
verb = input()

prompt('Enter an adjective: ')
adj = input()

prompt('Enter an adverb: ')
adv = input()

print(f"Do you {verb} your {adj} {noun} {adv}? That's hilarious!\n"
      f"The {adj} {noun} {verb}s {adv} over the lazy {noun}.\n"
      f"The {noun} {adv} {verb}s up to Joe's {adj} turtle.")

      