# Maryan Maxwell
# CSCI 101 - Section D
# Lab 4 - Timber Regrowth
# References: N/A
# Time: 1hr 10mins

import math

years = int(input("YEARS> "))
rate = float(input("RATE> "))
og_acres = float(input("ACRES> "))

acres = og_acres
percent_forest = 100 * (acres / 20000)
print(f"OUTPUT 0, {acres:.1f}, {percent_forest:.2f}")
    
for i in range(1, years + 1):
    forest = acres + ((rate/100) * acres)
    acres = forest
    percent_forest = 100 * (forest / 20000)
    print(f"OUTPUT {i}, {acres:.1f}, {percent_forest:.2f}%")

acres = og_acres

years_elapsed = 0
while acres < 20000:
    acres = (((rate/100) + 1) * acres)
    years_elapsed = years_elapsed + 1

print(f"OUTPUT {years_elapsed}")
