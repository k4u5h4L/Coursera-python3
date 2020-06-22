
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

map_testing = []

def concat(n):
  return 'Fruit: ' + n

map_testing = map(concat, lst_check)

print(list(map_testing))