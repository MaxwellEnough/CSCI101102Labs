# Maryan Maxwell
# CSCI 102 - Section D
# References: N/A
# Time: 14 mins

# INPUTS

numbers_list = []

print("Enter some numbers. Enter quit when you're done.")

number = input("NUMBER> ")

while number != 'quit':
    numbers_list.append(int(number))
    number = input("NUMBER> ")

# NUMBER OF NUMBERS

num_numbers = len(numbers_list)

# ADDITION OF THE FOUR NUMBERS

added_numbers = sum(numbers_list)

# OUTPUTS

print(f"The addition of the {num_numbers} numbers entered is:")
print(f"OUTPUT {num_numbers} numbers")
print(f"OUTPUT {added_numbers} total")
