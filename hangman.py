word_list = ['Boolean', 'Hyperactive','Witty','Emotion']

import random

chosen_word = random.choice(word_list)

guess = input("Guess a letter:").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
