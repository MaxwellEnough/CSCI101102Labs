# Maryan Maxwell
# CSCI 101 - Section A
# Lab 6 - Math in Another Universe
# References: Zachary Youngblood helped discuss possible approaches to problem
# Time: 3 hours

# Imports CSV module for later CSv file reading and writing
# Take input csv file of math and assign to variable 'mathfile'
# To be later used in with open(mathfile) etc. etc. to do math.
# Also take 'outputfile' to make well, file to output at end.

import csv

mathfile = input("MATHFILE> ")
outputfile = input("OUTPUTFILE> ")

# Opens mathfile (inputs) and outputfile (outputs) of the math.
# Creates reader "reader" and writer "writer" for mathfile and outputfile respectively
# Reads in mathfile by lines with new reader
things = []
with open(mathfile, 'r') as infile:
    with open(outputfile, 'w') as outfile:
        reader = csv.reader(mathfile)
        next(reader)
        for line in reader:
            for item in line:
                things.append(line)
                print(things)
        writer = csv.writer(outfile)
        operators = ['+','-','/','//','%','*','^']
        #operations = []
        #numbers = []
        
        leftresult = 3
        rightresult = 3

        for line in reader:
            for item in line:
                things.append(line)
                print(things)
                
            boolean = bool(leftresult == rightresult)

                # GOTTA MAKE THIS LAD HAVE COMMAS!
            writer.writerow(['OUTPUT', leftresult, rightresult, boolean])

            
            print(leftresult, rightresult, boolean)

        
    
