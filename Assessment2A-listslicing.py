# Maryan Maxwell
# CSCI 102 - Section D
# Assessment 01B
# References: 
# Time: 
import math
print("Give me a string:")
the_string = input("STRING> ")

a = int(input("A> "))
b = int(input("B> "))
c = int(input("C> "))
d = int(input("D> "))
 
sliced_string1 = the_string[a + 1:b]
sliced_string2 = the_string[c + 1:d]
print(f"OUTPUT {sliced_string1} {sliced_string2}")
