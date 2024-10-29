import random
import getpass

words_list = ["CAT", "MOON", "HAPPY", "PYTHON", "LADYBUG", "DINOSAUR", "CHOCOLATE", "PROGRAMMER"]
incorrect_letters = []
options1 = {"s":"Single player", "m":"Multiplayer"}
options2 = {"a":"one", "b": "three", "c": "five"}
points_list = []

def random_word():
    n = random.randint(0, len(words_list) - 1)
    rand_word_split = list(words_list[n])
    words_list.remove(words_list[n])
    correct_letter(rand_word_split)

def choose_word():
    #word = input("Enter your word: ").upper()
    word = getpass.getpass("Enter your word: ").upper()
    print()
    word_split = list(word)
    correct_letter(word_split)

def guess_letter(word):
    letter = input("Guess a letter: ").upper()
    while not letter.isalpha() or len(letter) != 1:
        letter = input("You have to enter a letter.\nGuess a letter: ").upper()
    while letter in incorrect_letters: # or in correct_letters
        letter = input("You have already tried this letter.\nGuess a letter: ")
    return(letter in word, letter)

def correct_letter(word_list):
    index = 0
    while len(word_list) > 0 and index < 5:
        guess = guess_letter(word_list)
        if guess[0] == True:
            while guess[1] in word_list:
                word_list.remove(guess[1])
            print(hangman(index))
        else:
            incorrect_letters.append(guess[1])
            index += 1
            print(hangman(index))
    if index == 5:
        print(hangman(6))
        return loser()
    else:
        point_counter()
        return winner()

def hangman(n):
    hangman_0 = (f"----------------\n|   /          |\n|  /           |\n| /\n|/\n|\n|\n|\n|\n|\n|\n|\n|\n")
    hangman_1 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |   |\n|             ---\n|\n|\n|\n|\n|\n|\n|\n")
    hangman_2 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |   |\n|             ---\n|              |\n|              |\n|              |\n|              |\n|\n|\n|\n")
    hangman_3 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |   |\n|             ---\n|              |\n|             /|\n|            / |\n|           /  |\n|\n|\n|\n")
    hangman_4 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |   |\n|             ---\n|              |\n|             /|\ \n|            / | \ \n|           /  |  \ \n|\n|\n|\n")
    hangman_5 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |   |\n|             ---\n|              |\n|             /|\ \n|            / | \ \n|           /  |  \ \n|             /\n|            /\n|           /\n") 
    hangman_6 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |x x|\n|             ---\n|              |\n|             /|\ \n|            / | \ \n|           /  |  \ \n|             / \ \n|            /   \ \n|           /     \ \n")
    
    hangman_list = [hangman_0, hangman_1, hangman_2, hangman_3, hangman_4, hangman_5, hangman_6]
    return(hangman_list[n])

def winner():
    print("                             ___  __")
    print("|   |   | |   |   |   |   | |    |  |")
    print(" | | | |  |  | | |   | | |  |--  |-|")
    print("  |   |   | |   |   |   |   |___ |  |")
    print("              _____ ")
    print("             | O O |")
    print("             |  U  |")
    print("             |_____|")

def loser():
    print(" ___   __             ___ ")
    print("|     |  |   |   |   |")
    print("|---| |--|  | | | |  |--")
    print("|___| |  | |   |   | |___ ")
    print("   ___         ___  __")
    print("  |   | |   | |    |  |")
    print("  |   |  | |  |--  |-|")
    print("  |___|   |   |___ |  |")
    print("          _____")
    print("         | x x |")
    print("         |  -  |")
    print("         |_____|")

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

def point_counter():
    points_list.append(1)
            

def main():
    global incorrect_letters
    opt1 = game_options("Select an action", "Action: ", options1)
    if opt1 == "m":
        print("Multiplayer selected\n")
        while True:
            incorrect_letters.clear()
            choose_word()
            game = input("\nWould you like to play again (y/n)?: ")
            while game != "n" and game != "y":
                game = input("\nYou have to enter 'y' or 'n'.\nWould you like to play again (y/n)?: ")
            if game == "n":
                print("\nGame over!")
                break
    else:
        print("Single player selected\n")
        opt2 = game_options("Select number of rounds", "Rounds: ", options2)
        print(f"You selected {options2[opt2]} round(s)")
        if options2[opt2] == "one":
            rounds = 1
        elif options2[opt2] == "three":
            rounds = 3
        else:
            rounds = 5
        
        turn = 1
        while turn <= rounds:
            incorrect_letters.clear()
            print(f"\nRound {turn}/{rounds}:\n")
            random_word()
            turn += 1
        print(f"\nYou won {len(points_list)}/{rounds} rounds")

main()