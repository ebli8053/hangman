import random

words_list = ["CAT", "MOON", "HAPPY", "PYTHON", "LADYBUG", "DINOSAUR", "CHOCOLATE", "PROGRAMMER"]
incorrect_letters = []
correct_letters = []

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

def random_word():
    n = random.randint(0, len(words_list) - 1)
    rand_word_split = list(words_list[n]) 
    print(rand_word_split)
    correct_letter(rand_word_split)

def choose_word():
    word = input("Enter your word: ").upper()
 #kontrollera att det är en bokstav
    word_split = list(word)
    correct_letter(word_split)

def guess_letter(word):
    letter = input("Guess a letter: ").upper()
    while letter in incorrect_letters:
        letter = input("You have already tried this letter.\nGuess a letter: ")
    return(letter in word, letter)

def correct_letter(word_list):
    index = 0
    original_word = word_list
    guessed_word = ['_'] * len(original_word)

    while len(word_list) > 0 and index < 6:
        guess = guess_letter(original_word)
        if guess[0]:
            correct_letters.append(guess[1])
            for x in range(len(original_word)):
                if original_word[x] == guess[1]:
                    guessed_word[x] = guess[1]            
            print(hangman(index))
            print(f"Incorrect letters: {add_incorrect_letters()}\n")
            print(f"Correct letters: {' '.join(guessed_word)}\n")
            
            if "_" not in guessed_word:
                winner()
                return
        else:
            incorrect_letters.append(guess[1])
            index += 1
            print(hangman(index))
            print(f"Incorrect letters: {add_incorrect_letters()}\n")
            print(f"Correct letters: {' '.join(guessed_word)}\n")
    loser()
    
def add_incorrect_letters():
    return ", ".join(incorrect_letters)

def hangman(n):
    hangman_0 = (f"----------------\n|   /          |\n|  /           |\n| /\n|/\n|\n|\n|\n|\n|\n|\n|\n|\n")
    hangman_1 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |   |\n|             ---\n|\n|\n|\n|\n|\n|\n|\n")
    hangman_2 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |   |\n|             ---\n|              |\n|              |\n|              |\n|              |\n|\n|\n|\n")
    hangman_3 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |   |\n|             ---\n|              |\n|             /|\n|            / |\n|           /  |\n|\n|\n|\n")
    hangman_4 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |   |\n|             ---\n|              |\n|             /|\ \n|            / | \ \n|           /  |  \ \n|\n|\n|\n")
    hangman_5 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |   |\n|             ---\n|              |\n|             /|\ \n|            / | \ \n|           /  |  \ \n|             /\n|            /\n|           /\n") 
    hangman_6 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |   |\n|             ---\n|              |\n|             /|\ \n|            / | \ \n|           /  |  \ \n|             / \ \n|            /   \ \n|           /     \ \n")
    hangman_7 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |x x|\n|             ---\n|              |\n|             /|\ \n|            / | \ \n|           /  |  \ \n|             / \ \n|            /   \ \n|           /     \ \n")
    
    hangman_list = [hangman_0, hangman_1, hangman_2, hangman_3, hangman_4, hangman_5, hangman_6, hangman_7]
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
    

random_word()