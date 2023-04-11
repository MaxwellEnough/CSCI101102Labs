# Maryan Maxwell
# CSCI 102 – Section D
# Assessment 04B
# References: N/A
# Time: 20 mins

print("Input the chemical elements of the amino acid:")
carbon = int(input("CARBON> "))
hydrogen = int(input("HYDROGEN> "))
nitrogen = int(input("NITROGEN> "))
oxygen = int(input("OXYGEN> "))
sulfur = int(input("SULFUR> "))

if sulfur == 1:
    amino_total = 'Cysteine'

elif carbon == 5:
    amino_total = 'Glutamine'

elif hydrogen == 9:
    amino_total = 'Histidine'

elif hydrogen == 14:
    amino_total = 'Arginine'

elif hydrogen == 8:
    amino_total = 'Asparagine'

elif hydrogen == 7 and sulfur == 0:
    amino_total = 'Alanine'

print(f"The amino acid for {carbon}C--{hydrogen}H--{nitrogen}N--{oxygen}O--{sulfur}S is {amino_total}.")
print(f"OUTPUT {carbon}C--{hydrogen}H--{nitrogen}N--{oxygen}O--{sulfur}S")
print(f"OUTPUT {amino_total}")
