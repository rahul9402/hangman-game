import random

words = ["apple", "grape", "watermelon", "pineapple", "citrus", "pomegranate", "leach", "lemon", "soda", "orange",
         "mango", "jackfruit"]

random_word = random.choice(words)  # apple

list1 = []
for i in random_word:
    list1.append("_")
print(list1)

flag = True
lives = 6
while flag:

    guessed_letter = input("Enter a letter: ")

    if guessed_letter in random_word:
        for i in range(len(list1)):
            if random_word[i] == guessed_letter:
                list1[i] = guessed_letter
        print(list1)
        print()
    else:
        print(list1)
        lives -= 1
        if lives == 0:
            flag = False
            print("You Lose....")
            print(f"Correct word is {random_word}")
        else:
            print(f"You have {lives} chances left")
            print()
    if "_" not in list1:
        flag = False
        print("You Won....")
