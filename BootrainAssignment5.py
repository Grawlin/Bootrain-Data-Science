title = 'Exercise N°{}'

print(title.format(1), '\n')

days = {1:'Sunday', 2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday', 7:'Saturday'}

day1 = input('Insert the number from a day of the week (1-7, Sunday to Saturday): ')
day2 = input('Insert a different number from a day of the week (1-7, Sunday to Saturday): ')
print('')

days.pop(int(day1))
days.pop(int(day2))

print(days.values(), '\n')

print(title.format(2), '\n')

personnel = {
    'John':{
        'age':25,
        'sex':'Male'
    },
    'Lisa':{
        'age':28,
        'sex':'Female'
    },
    'Linda':{
        'age':32,
        'sex':'Female'
    },
    'Michael':{
        'age':41,
        'sex':'Male'
    }
}

print(personnel.items(), '\n')

print(title.format(3), '\n')

personnel = {
    'John':{
        'age':25,
        'sex':'Male'
    },
    'Lisa':{
        'age':28,
        'sex':'Female'
    },
    'Linda':{
        'age':32,
        'sex':'Female',
        'child':{
            'Susan':{
                'age':6,
                'sex':'Female'
            }
        }
    },
    'Michael':{
        'age':41,
        'sex':'Male',
        'child':{
            'Karen':{
                'age':12,
                'sex':'Female'
            },
            'Greg':{
                'age':7,
                'sex':'Male'
            }
        }
    }
}

print(personnel.items(), '\n')

print(title.format(4), '\n')

print(list(personnel['Michael']['child']))