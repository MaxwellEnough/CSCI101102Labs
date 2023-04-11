# Maryan Maxwell
# CSCI 101 - Section I
# Assessment 3 - Parsing Pride & Predators
# References: N/A
# Time: ~4 hours

import string
bad_characters = str.maketrans('', '', string.punctuation)

with open("Pride&Prejudice_Ch1&2.txt", 'r') as file:
    use = file.read()
    for a in use:
        use = use.translate(bad_characters)
    use = use.lower()
    use = use.split()  

choice = int(input("CHOICE> "))

if choice == 1:
    word = input("WORD> ")
    word = word.lower()
    output = use.count(word)
    print(f"OUTPUT {output}")

if choice == 2:
    length = int(input("LENGTH> "))
    for b in use:
        numbers = '0 1 2 3 4 5 6 7 8 9'
        bad_numbers = str.maketrans('', '', numbers)
        use = use.remove(bad_numbers)
    total_num = use.count(length)
    
    print(f"OUTPUT {total_num}")
    unique = 'wahoo'
    print(f"OUTPUT {unique}")


numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
