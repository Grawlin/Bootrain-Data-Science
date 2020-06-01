title = 'Exercise N°{}'

print(title.format(1), '\n')

in_temp = input('Please enter a temperature to convert, either Celcius or Fahrenheit (write C or F at the end): ')

scale = in_temp[len(in_temp)-1] #Determines the temperature scale

#Takes the number present in the variable in_temp
if ' ' not in in_temp:
    temp = int(in_temp[0:len(in_temp)-1])
else:
    temp = int(in_temp[0:in_temp.index(' ')])

if scale == 'C' or scale == 'c':
    #Temperaure in Fahrenheit
    print('The temperature in Fahrenheit is: {:.2f}'.format(temp*(9/5)+32), 'F \n')
else:
    #Temperaure in Celcius
    print('The temperature in Celcius is: {:.2f}'.format((temp-32)*(5/9)), 'C \n')

print(title.format(2), '\n')

years = int(input('Please enter the years you have been working for this company: '))
print('')
salary = int(input('Please enter your salary: '))
print('')

if years > 5:
    print('You will have a bouns of: $ {:.2f}'.format(0.05*salary), '\n')
else:
    print("You won't be receiving a bouns \n")

print(title.format(3), '\n')

person1 = input('Enter the name of the first person: ')
print('')
years1 = int(input('Enter the  years of that person: '))
print('')

person2 = input('Enter the name of the second person: ')
print('')
years2 = int(input('Enter the  years of that person: '))
print('')

person3 = input('Enter the name of the third person: ')
print('')
years3 = int(input('Enter the  years of that person: '))
print('')

youngest = min(years1, years2, years3)
oldest = max(years1, years2, years3)

if youngest == years1:
    print('The youngest among them is:', person1, '\n')
elif youngest == years2:
    print('The youngest among them is:', person2, '\n')
else:
    print('The youngest among them is:', person3, '\n')

if oldest == years1:
    print('The oldest among them is:', person1, '\n')
elif oldest == years2:
    print('The oldest among them is:', person2, '\n')
else:
    print('The oldest among them is:', person3, '\n')

print(title.format(4), '\n')

class_held = int(input('Please enter the number of classes held: '))
print('')
class_attend = int(input('Please enter the number of classes you have attendedd: '))
print('')

perc_class = (class_attend/class_held)

if perc_class >= 0.75:
    print('You can attend the exam \n')
else:
    print('You are not allowed to attend the exam \n')

print(title.format(5), '\n')

letter = input('Please enter a letter: ')
print('')

if letter == 'a' or letter =='e' or letter =='i' or letter =='o'or letter =='u':
    print('The letter you have entered is a vowel \n')
elif letter == 'y':
    print('The "y" is sometimes a vowel and sometimes a consonant \n')
else:
    print('The letter you have entered is a consonant \n')