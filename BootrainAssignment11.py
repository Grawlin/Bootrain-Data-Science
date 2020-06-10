title = 'Exercise N°{}'

print(title.format(' 1 & 3'), '\n')

def homographic(x):
    try:
        return 1/x
    except Exception as e:
        print('"{}" error occurred!'.format(e), '\n')

def enter_value(value):
    try:
        value = int(value)
        print('')
        print("It's homoraphic value is:", homographic(value), '\n')
    except ValueError:
        print('')
        print('Please enter a numeric value', '\n')
        value = input('Please enter an integer: ')
        return enter_value(value)

num = input('Please enter an integer: ')
enter_value(num)

print(title.format(2), '\n')

#name = input('Please enter your name: ')
last_name = input('Please enter your last name: ')

try:
    print('Your full name is', name + ' ' + last_name)
except NameError:
    print('One of the names are missing')