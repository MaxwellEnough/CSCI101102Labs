# Maryan Maxwell
# CSCI 101 - Section A
# Assessment 1 - The Sleeper
# References: N/A
# Time: 35 mins

print("How many minutes early you wanna get spooked out of bed?")
mins_early = int(input("EARLY> "))

print("Great. And what time you gotta roll out by?")
hours = int(input("HOURS> "))
mins = int(input("MINUTES> "))

total_mins = mins + (hours * 60) - mins_early

if total_mins < 0:
    total_mins = total_mins + 1440

hours = total_mins // 60
mins =  total_mins % 60

if hours < 10:
    hours = str(hours)
    hours = '0' + hours

if mins < 10:
    mins = str(mins)
    mins = '0' + mins

print("Then you gotta set the alarm for:")
print(f"OUTPUT {hours} {mins}")
