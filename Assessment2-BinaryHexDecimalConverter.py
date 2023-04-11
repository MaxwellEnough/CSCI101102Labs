# Maryan Maxwell
# CSCI 101 - Section I
# Assessment 2 - Binary-Hex-Decimal Converter
# References: Zach YB
# Time: 5 hours

# Printed welcome and option selection menu, option input.

print("Ahoy there, welcome to the Binary-Hex-Decimal Converter!")
print("Pick yourself a conversion option:")
print("")
print("1.) Binary-Decimal Conversion")
print("2.) Decimal-Binary Conversion")
print("3.) Hexadecimal-Decimal Conversion")
print("4.) Decimal-Hexadecimal Conversion")
print("")
conversion = int(input("OPTION> "))

# if/elif statements that pick conversion method and convert number
# based on int value of "conversion" variable from selection menu.

# BINARY-DECIMAL CONVERSION SERIES
if conversion == 1:
    binary_sstr = input("BINARY-STR> ")

# Check if binary string is valid binary string before conversion
    allowed_binary = ['0', '1']
    check_binary = [i in allowed_binary for i in binary_sstr]
    check_binary = all(check_binary)
    if check_binary is False:
        print(f"{binary_sstr} is not a Binary number.")
        print("OUTPUT ERROR")

# The actual conversion process go BRR
    decimal_num = 0
    binary_str = binary_sstr
    counter = len(binary_str)
    while counter > 0:
        binary_int = int(binary_str[0])
        binary_str = binary_str.replace(binary_str[0], '', 1)
        if binary_int == 1:
            conv_num = (binary_int * 2) ** (counter - 1)
            decimal_num = decimal_num + conv_num
        else:
            decimal_num = decimal_num
        counter = len(binary_str)


# DECIMAL-BINARY CONVERSION SERIES
elif conversion == 2:
    decimal_sstr = input("DECIMAL-STR> ")

# Check if decimal string is valid decimal string before conversion
    allowed_decimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    check_decimal = [i in allowed_decimal for i in decimal_sstr]
    check_decimal = all(check_decimal)
    if check_decimal is False:
        print(f"{decimal_sstr} is not a Decimal number.")
        print("OUTPUT ERROR")
        
# More actual conversion nonsense not go BRR

    binary_num = ""
    decimal_str = decimal_sstr
    while decimal_str != 0:
        decimal_int = int(decimal_str)
        remainder = decimal_int % 2
        remainder = str(remainder)
        binary_num = str(remainder) + str(binary_num)
        decimal_int = decimal_int // 2
        decimal_str = decimal_int
        

# HEXADECIMAL-DECIMAL CONVERSION SERIES
elif conversion == 3:
    hexdec_str = input("HEXADECIMAL-STR> ")

# Check if hexadecimal string is valid hexadecimal string before conversion
    allowed_hexdec = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    check_hexdec = [i in allowed_hexdec for i in hexdec_str]
    check_hexdec = all(check_hexdec)
    if check_hexdec is False:
        print(f"{hexdec_str} is not a Hexadecimal number.")
        print("OUTPUT ERROR")


# DECIMAL-HEXADECIMAL CONVERSION SERIES
elif conversion == 4:
    decimal_str = input("DECIMAL-STR> ")

# Check if decimal string is valid decimal string before conversion
    allowed_decimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    check_decimal = [i in allowed_decimal for i in decimal_str]
    check_decimal = all(check_decimal)
    if check_decimal is False:
        print(f"{decimal_str} is not a Decimal number.")
        print("OUTPUT ERROR")




if conversion == 1:
    print(f"Binary {binary_sstr} is Decimal {decimal_num}")
    print(f"OUTPUT {decimal_num}")

if conversion == 2:
    print(f"Decimal {decimal_sstr} is Binary {binary_num}")
    print(f"OUTPUT {binary_num}")

if conversion == 3:
    print(f"Hexadecimal {hexdec_sstr} is Decimal {decimal_num}")
    print(f"OUTPUT {decimal_num}")

if conversion == 4:
    print(f"Decimal {decimal_str} is Hexadecimal {hexdec_num}")
    print(f"OUTPUT {hexdec_num}")

