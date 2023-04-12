# Maryan Maxwell
# CSCI 102 - Git Assignment C
# References: N/A
# Time: is an illusion

def load_file(file_input):
   with open(file_input) as file:
       print(f"OUTPUT {file.readline()}")

#def update_string(aaa, bbb):
    #nope 

def find_word_count(the_list, the_string):
    summation = 0
    for a in the_list:
        summation += a.count(the_string)
    print(summation)

def score_finder(names, scores, player):
    for item in names:
        if player in names:
            score = scores[item]
            print(f"OUTPUT {player} got a score of {score}")
        else:
            print("OUTPUT player not found")

def union(list1, list2):
    list3 = list1 + list2
    print(f"OUTPUT {list3}")

def intersect(list1, list2):
    intersection = []
    for thing in list1:
        if thing in list2:
            intersection.append(thing)
    print(intersection)
    
def not_in(list1, list2):
    okay = []
    for thing in list1:
        if thing not in list2:
            okay.append(thing)
    print(okay)

def is_prime(integer):
    import math
    if integer == 1:
        return False
    if integer == 2:
        return True
    range2 = (int(math.ceil(math.sqrt(integer))))
    for b in range(2, range2):
        if integer % 1 == 0:
            return False
    return True
