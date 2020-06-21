
lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10],
       ['green', 'yellow', 'purple', 'red']]

# Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
for i in lst[2]:
    if i == 'yellow':
        yellow = True
        break
    else:
        yellow = False

print(yellow)


# Test to see if 4 is in the second list of lst. Save to variable ``four``
for j in lst[1]:
    if j == 4:
        four = True
        break
    else:
        four = False

print(four)


# Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
for k in lst[0]:
    if k == 'orange':
        orange = True
        break
    else:
        orange = False

print(orange)
