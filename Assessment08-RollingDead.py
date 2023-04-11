# Maryan Maxwell
# CSCI 102 - Section D
# Assessment 8 - Rolling Dead
# References: Matthew Rottinghaus
# Time: 53 mins

# Inputs for seed, the number of rolls of the dead,
# And the sides of the dead
# Also base for num (counter) for dice rolls

import random
num = 0
allrolls = []

print("Seed the field.")
seed = int(input("SEED> "))

print("How much would you like to roll in your grave?")
num_rolls = int(input("ROLLS> "))

print("And how many sides should your death have?")
num_sides = int(input("SIDES> "))

# Seed the field, AKA the random ints list here

random.seed(seed)

# Rolls?

for num in range(0, num_rolls):
    roll = random.randint(1, num_sides)
    allrolls.append(roll)

# Print the output prompt!

print(f"Here's your {num_rolls} takes of your {num_sides} death.")

for i in range(1, num_sides + 1):
    how_many = allrolls.count(i)
    print(f"OUTPUT {i} occurred {how_many} times")
