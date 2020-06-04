title = 'Exercise N°{}'

print(title.format(1), '\n')

def is_prime(n):
    if n == 1 or n == 2:
        return True
    else:    
        for i in range(2, n):
            if n % i == 0:
                return False
            else:
                return True

num = 0

num = int(input('Please enter an integer: '))
print('')

if is_prime(num):
    print('The number entered is a PRIME number', '\n')
else:
    print('The number entered is NOT A PRIME number', '\n')

print(title.format(2), '\n')

def unique_list(list1):
    new_list = []
    new_list.append(list1[0])
    for i in range(0, len(list1)):
        n_repeats = 0 #Variable to ensure there are no duplicates in the new list
        for j in range(0, len(new_list)):
            if list1[i] == new_list[j]:
                n_repeats += 1 #Controls duplication
        if n_repeats == 0:
            new_list.append(list1[i])
    return new_list


print('The unique list of [1,2,2,3,3,4,4] is:', unique_list([1,2,2,3,3,4,4]), '\n')

print(title.format(3), '\n')

birthday = input('Please enter your birthday (d/m/yyyy): ')
birthday = birthday.replace(' ', '')

def age(birthday):
    """
    You need to use the following format for a date in this function: d/m/yyyy
    """
    import datetime
    birthday = datetime.datetime.strptime(birthday, '%d/%m/%Y')
    today = datetime.date.today()
    old = today.year - birthday.year
    if birthday.month >= today.month and birthday.day >= today.day:
        old -= 1
    return old

print('You are {} years old'.format(age(birthday)), '\n')

print(title.format(4), '\n')

num = int(input('Please enter an integer: '))

def factorail(n):
    fact = 1
    if n ==  0:
        return fact
    else:
        for i in range(1, n+1):
            fact = fact * i
        return fact

print('{} factorial is {}'.format(num, factorail(num)), '\n')

print(title.format(5), '\n')

def perfect(n):
    sum_fact = 1 #The factors are added in this variable
    for i in range(2, n):
        if n % i == 0:
            sum_fact += i
    if sum_fact == n:
        return True
    else:
        return False

for i in range(1, 1001):
    if perfect(i):
        print(i)
print('')

print(title.format(6), '\n')

def pascal(n):
    prev_list = [1]
    new_list = []
    print(prev_list)
    i = 1
    while i < n:
        for j in range(i+1):
            if j == 0 or j == i:
                new_list.append(1)
            else:
                new_list.append(prev_list[j-1]+prev_list[j])
        i += 1
        prev_list = new_list
        print(new_list)
        new_list = []
    for k in range(n+1):
        if k == 0 or k == n:
            new_list.append(1)
        else:
            new_list.append(prev_list[k-1]+prev_list[k])
    return new_list

num = int(input('Please enter the power of binomial function you are looking for: '))
print(pascal(num), '\n')