# Maryan Maxwell
# CSCI 102 - Section J
# Assessment 11 - Functions Practicality
# References: N/A
# Time: Like one (1) hour

# Printing the output function. It does exactly what it
# Says it does; it takes the input to the function. And
# It prints it. Wowie. But it prints it with "OUTPUT "
# Because we don't want gradescope to have a fit today.

def print_output(output):
    print(f"OUTPUT {output}")

# Cylindrical volume function. It takes in radius and
# Also height of a given cylinder, then uses the formula
# V = (pi)(r^2)(h) to find cylindrivcal volume. Before of
# Course calling print_output to finish the job >:) ...

def cylinder_vol(radius, height):
    volume_cyl = (height * 3.1415 * (radius ** 2))
    print_output(f"{volume_cyl:.2f}")

# Pounds to Kilograms function. Input the pounds and it
# Outputs the kilograms after some very basic conversion
# Multiplication. Now ain't that handy? It uses p_o as well
# And neatly rounds the output too, when it works right!

def lbs_to_kg(lbs):
    kg = (lbs * 0.4536)
    print_output(f"{kg:.4f}")

# Polar Coordinates function. It takes cartesian coordinates,
# x_coord and y_coord, and uses basic trig to convert them to
# Polar coordinates, which are commonly used by the navy/air
# Folks. Why? Because it's cool, okay? Jeez.

def polar_coords(x_coord, y_coord):
    import math
    rrr = math.sqrt((x_coord ** 2) + (y_coord ** 2))
    theta = (math.atan(y_coord / x_coord)) * (180 / 3.1415)
    print_output(f"r: {rrr:.2f}")
    print_output(f"theta: {theta:.2f}")

# Yen to dollars function. Converts Japanese Yen input to
# An amount of US dollars based on outdated exchange rate.
# Still cool though! Then prints dollars with print_output
# Because gotta call prior function due to assignment. :/

def yen_to_dollars(yen):
    dollars =(yen * 0.0068)
    print_output(f"{dollars:.2f}")

# Quadratic form function. Takes in values for a, b, and c.
# Then imports math for square roots. And does positive and
# Negative variations (+-) of quadratic formula, and prints
# Both values off individually for user. :D

def quad_form(a, b, c):
    import math
    positive_x = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    negative_x = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    print_output(f"{negative_x:.0f}")
    print_output(f"{positive_x:.0f}")
