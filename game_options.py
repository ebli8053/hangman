def letter_amount():
    print("How many letters are in your word?\n")
    amount_letters = input("Amount of letters: ")
    return amount_letters

def game_options(title, prompt, options):
    while True:
        print(title)
        print()
        for x in options:
            print(f"{x}) {options[x]}")
        print()
        s = input(f"{prompt} ")
        print()
        if s in options:
            return s
        else:
            print(f"invalid option: {s}. Please try again!")
            

options1 = {"s":"Single player", "m":"Multiplayer"}
opt1 = game_options("Select an action", "Action: ", options1)
#print(f"You selected {options1[opt1]}")

if opt1 == "m":
    letters = letter_amount()
    print(f"You selected {letters} letters.\n")
else:
    print("Single player selected.\n")
    

options2 = {"a":"one", "b": "three", "c": "five"}
opt2 = game_options("Select number of rounds", "Rounds: ", options2)
print(f"You selected {options2[opt2]} rounds")
print()