"""
print("----------------")
print("|   /          |")
print("|  /           |")
print("| /           ---")
print("|/           |x x|")
print("|             ---")
print("|              |")
print("|             /|\ ")
print("|            / | \ ")
print("|           /  |  \ ")
print("|             / \ ")
print("|            /   \ ")
print("|           /     \ ")
"""

hangman_0 = ("----------------\n|   /          |\n|  /           |\n| /\n|/\n|\n|\n|\n|\n|\n|\n|\n|\n")
hangman_1 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |   |\n|             ---\n|\n|\n|\n|\n|\n|\n|\n")
hangman_2 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |   |\n|             ---\n|              |\n|              |\n|              |\n|              |\n")
hangman_3 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |   |\n|             ---\n|              |\n|             /|\n|            / |\n|           /  |\n")
hangman_4 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |   |\n|             ---\n|              |\n|             /|\ \n|            / | \ \n|           /  |  \ \n")
hangman_5 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |   |\n|             ---\n|              |\n|             /|\ \n|            / | \ \n|           /  |  \ \n|             /\n|            /\n|           /\n") 
hangman_6 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |   |\n|             ---\n|              |\n|             /|\ \n|            / | \ \n|           /  |  \ \n|             / \ \n|            /   \ \n|           /     \ \n")
hangman_7 = ("----------------\n|   /          |\n|  /           |\n| /           ---\n|/           |x x|\n|             ---\n|              |\n|             /|\ \n|            / | \ \n|           /  |  \ \n|             / \ \n|            /   \ \n|           /     \ \n")

hangman_list = [hangman_0, hangman_1, hangman_2, hangman_3, hangman_4, hangman_5, hangman_6, hangman_7]

for x in hangman_list:
    print(x)