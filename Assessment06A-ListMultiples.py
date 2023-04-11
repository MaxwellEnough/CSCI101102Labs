# Maryan Maxwell
# CSCI 102 - Section D
# Assessment 6 - List Multiples
# References: N/A
# Time: 20 mins

print("Enter the number I gotta make multiples for:")
number = int(input("NUMBER> "))
print("And also the maximum index of this list.")
index = int(input("INDEX> "))

multiples_list = []
counter = index + 1

while counter > 0:
    multiple = number * counter
    multiples_list.insert(0, multiple)
    counter = counter - 1

print("Your list of multiples is this, my liege.")
print(f"OUTPUT {multiples_list}")
print("And obviously the first multiple was...")
print(f"OUTPUT {multiples_list[0]}")

