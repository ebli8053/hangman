import random

words_list = ["CAT", "MOON", "HAPPY", "PYTHON", "LADYBUG", "DINOSAUR", "CHOCOLATE", "PROGRAMMER"]

def random_word():
    n = random.randint(0, len(words_list) - 1)
    word = list(words_list[n])
    return word

def choose_word():
    word = input("Enter your word: ").upper()
    word_split = list(word)
    return word_split

def guess_letter(word):
    letter = input("Guess a letter: ").upper()
    return(letter in word)
    
word = choose_word()
print(word)
print(guess_letter(word))

computer_word = random_word()
print(computer_word)
print(guess_letter(computer_word))