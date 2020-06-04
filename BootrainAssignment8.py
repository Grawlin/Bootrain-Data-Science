title = 'Exercise N°{}'

print(title.format(1), '\n')

num = int(input('Please enter a number to multiply: '))
print('')

for i in range(1,11):
    print(num, 'x', i, '=', num * i)
print('')

print(title.format(2), '\n')

for i in range(1,21):
    if i%2 == 0:
        print(i**3)
    else:
        print(i**2)
print('')

print(title.format(3), '\n')

word = input('Please enter a word: ')

for i in range(1,len(word)+1):
    print(word[len(word)-i], end='')
print('\n')

print(title.format(4), '\n')

for i in range(1, 201):
    if i%2 != 0:
        print(i, end=' ')
    else:
        print(i)
print('')

print(title.format(5), '\n')

def count(sequence, item):
    c = 0 #Define counter at 0
    for i in range(len(sequence)):
        if sequence[i] == item:
            c +=1
    print('The item appears', c, 'times')

count(list([1, 2, 2, 3]), 2) #Example
print('')

print(title.format(6), '\n') #REVISAR

def digit_sum(n):
    c = 0
    for i in range(len(str(n))):
        c += int(str(n)[i])
    if c < 10:
        return c
    else:
        return digit_sum(c)

num = input('Please enter a number: ')
print('')

print("The sum of all that number's digits are:", digit_sum(num), '\n')

print(title.format(7), '\n')

num1 = int(input('Please enter a number: '))
num2 = int(input('Please enter another number: '))
print('')

r = 1 #Set a starting value fo the remainder
lrg = max(num1, num2)
lwr = min(num1, num2)

while r != 0:
    r = lrg % lwr
    lrg = lwr
    lwr = r
    if lrg % lwr == 0:
        break

print('The greatest common divisor (GCD) is:', r, '\n')

print(title.format(8), '\n')

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
print('\n')

print(title.format(9), '\n')

a = 1
b = 1
print(a, end= ' ')
print(b, end= ' ')

for i in range(1, 51):
    c = a + b
    print(c, end=' ')
    a = b
    b = c
print('\n')