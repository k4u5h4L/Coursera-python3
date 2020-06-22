
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']

l3 = zip(l1, l2)

opposites = list(filter(lambda res: len(res[0]) > 3 and len(res[1]) > 3, l3))
