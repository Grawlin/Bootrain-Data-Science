title = 'Exercise N°{}'

print(title.format(1))
print('')

capital = 1000
dg = 12 #Daily growth
period = 7

#gr = #final growth rate

result = capital * (1 + dg/100) ** period

print(result)

print('-' * 20)
print(title.format(2))
print('')

print('"When we buy bitcoin with {} USD at the beginning of the week, \
we would earn {:.2f} USD \nat the end of the week, with an average gain of {}%."'.format(capital, result - capital, dg))
print('')

print('-' * 20)
print(title.format(3))
print('')

tf = input('Enter the temperature in Fahrenheit: ') #Temperature in Fahrenheit
tc = (5/9) * (int(tf) - 32) #Temperature in Celcius

print('Temperature (C): {:.2f}'.format(tc))

print('-' * 20)
print(title.format(4))
print('')

num = input('Enter a 3 digit number: ')
add = int(num[0]) + int(num[1]) + int(num[2])

print('The sum of digits in the number is:', add)

print('-' * 20)
print(title.format(5))
print('')

c1 = input('First side  length: ')
c2 = input('Second side  length: ')

hyp = (int(c1) ** 2 + int(c2) ** 2) ** 0.5

print('The length of the hypotenuse is {:.2f}'.format(hyp))
print('')