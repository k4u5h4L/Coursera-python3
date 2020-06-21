
athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt',
                                                                       'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]

t = []
other = []

for i in athletes:
    for j in i:
        if 't' in j:
            t.append(j)
        else:
            other.append(j)

print(t)
