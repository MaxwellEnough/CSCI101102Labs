# Maryan Maxwell
# CSCI 102 – Section A
# Assessment 07 - Checkerboard
# References: Random dude helped me write pseudocode for pattern after class
# Time: 2 hours

# Collecting numbers of columns and rows to use for checkerboard pattern
# And also first and second strings ("black and white") for board pattern.
# +2 CHA for flavor text

columns = int(input("COLUMNS> "))
rows = int(input("ROWS> "))
first = input("FIRST> ")
second = input("SECOND> ")

# Establishing even_odd (which determines which pattern the rows will have)
# Establishing row0 and row1 (the row lists to be pattern in for loop ahead)
# Establishing num_columns (show how many columns output should have)
# And the counter (for how many items in each row of the checkerboard)

even_odd = (rows + columns) % 2
row0 = []
row1 = []
num_columns = columns
counter = 0
counter2 = 0
twoD_array = []

# Printing OUTPUTS to the user! Fun for y'all
# Also is the least stressful part of this.
# Besides inputs obviously. Inputs are a given.
# L O O P S

if even_odd == 0:
    for counter in range(columns):
            row0.append(first)
            row0.append(second)
            counter2 += 1

    row0 = row0[:len(row0)//2]     

    for counter in range(columns):
            row1.append(second)
            row1.append(first)
            counter2 += 1

    row1 = row1[:len(row1)//2]

    for counter2 in range(rows):
        if (counter2 % 2) == 0:
            print(f"OUTPUT {row0}")
        else:
            print(f"OUTPUT {row1}")

    for counter2 in range(rows):
        if (counter2 % 2) == 0:
            twoD_array.append(row0)
        else:
            twoD_array.append(row1)

else:
    for counter in range(columns):
            row0.append(second)
            row0.append(first)
            counter2 += 1

    row0 = row0[:len(row0)//2]

    for counter in range(columns):
            row1.append(first)
            row1.append(second)
            counter2 += 1

    row1 = row1[:len(row1)//2]

    for counter2 in range(rows):
        if (counter2 % 2) == 0:
            print(f"OUTPUT {row1}")
        else:
            print(f"OUTPUT {row0}")

    for counter2 in range(rows):
        if (counter2 % 2) == 0:
            twoD_array.append(row1)
        else:
            twoD_array.append(row0)

print(f"OUTPUT {twoD_array}")
