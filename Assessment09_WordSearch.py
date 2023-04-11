# Maryan Maxwell and Coulter Perkins
# CSCI 102 - Section D
# Peer Review; Assessment 9 - Woyd Soych
# References:
# Time: 10 mins

print("S e e d  t h e  f i e l d")
seed = input("SEED> ")
print("Now a lengthy number boi")
length = int(input("LENGTH> "))

import random
goodwords = []
random.seed(seed)

with open("dictionary.txt") as file:
             for word in file:
                 if len(word) == length + 1:
                     goodwords.append(word)

if len(goodwords) == 0:
    random_word = 'None'
else:
    random_word = random.choice(goodwords)

num_words = len(goodwords)

print(f"Delicious word of lengthening {length}")
print(f"OUTPUT {random_word}")
print(f"And the number of those ees")
print(f"OUTPUT {num_words}")
