# Maryan Maxwell
# CSCI 102 - Section A
# Assessment 10 - Parts Deep Rango
# References: Matthew Rottinghaus
# Time: 1 hour 24 mins

import csv

with open("formations.csv", "r") as infile:
    with open("formations_parsed.csv", "w", newline = '') as outfile:
        reader = csv.reader(infile)
        next(reader)

        writer = csv.writer(outfile)
        writer.writerow(["Depth","Start Depth","End Depth","Difference in Depth","Formation","Age of Formation"])

        for line in reader:
            depth_range = line[0]
            start1 = float(depth_range.split("-")[0])
            end = float(depth_range.split("-")[1])
            difference = '%.2f' % (end - start1)
            name = line[1]
    
            if start1 > 700:
                age = 'Cretaceous'
            else:
                age = 'Paleocene'

            writer.writerow([depth_range, start1, end, difference, name, age])
