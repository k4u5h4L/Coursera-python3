
countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']

b_countries = []

def validate(n):
    if n[0] == 'B':
        return 'Fruit: ' + n
    else:
        return False

b_countries = filter(validate, countries)

print(list(b_countries))