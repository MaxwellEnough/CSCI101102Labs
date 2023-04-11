print("Put in yer rows you heathen")
row0 = input("ROW0> ")
row1 = input("ROW1> ")
row2 = input("ROW2> ")
wins = 0
if len(row0) > 3 or len(row0) < 3 or len(row1) > 3 or len(row1) < 3 or len(row2) > 3 or len(row2) < 3:
    wins = wins - 1
allowed_letters = ['X', 'O', 'E']
check0 = [i in allowed_letters for i in row0]
check0 = all(check0)
check1 = [i in allowed_letters for i in row1]
check1 = all(check1)
check2 = [i in allowed_letters for i in row2]
check2 = all(check2)
if check0 is True and check1 is True and check2 is True:
    wins = wins 
else:
    wins = wins - 1
if wins <= -1:
    print("OUTPUT ERROR")
if row0 == 'XXX' or row1 == 'XXX' or row2 == 'XXX':
    wins = 1    
elif row0 == 'OOO' or row1 == 'OOO' or row2 == 'OOO':
    wins = 2  
if row0[0] == 'X' and row1[0] == 'X' and row2[0] == 'X':
    wins = 1
elif row0[0] == 'O' and row1[0] == 'O' and row2[0] == 'O':
    wins = 2
elif row0[1] == 'X' and row1[1] == 'X' and row2[1] == 'X':
    wins = 1
elif row0[1] == 'O' and row1[1] == 'O' and row2[1] == 'O':
    wins = 2
elif row0[2] == 'X' and row1[2] == 'X' and row2[2] == 'X':
    wins = 1
elif row0[2] == 'O' and row1[2] == 'O' and row2[2] == 'O':
    wins = 2
if row0[0] == 'X' and row1[1] == 'X' and row2[2] == 'X':
    wins = 1
elif row0[0] == 'O' and row1[1] == 'O' and row2[2] == 'O':
    wins = 2
elif row0[2] == 'X' and row1[1] == 'X' and row2[0] == 'X':
    wins = 1
elif row0[2] == 'O' and row1[1] == 'O' and row2[0] == 'O':
    wins = 2
if wins == 1:
    print("OUTPUT X")
elif wins == 2:
    print("OUTPUT O")
elif wins >= 0:
    print("OUTPUT T")
