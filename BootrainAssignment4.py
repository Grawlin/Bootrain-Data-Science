title = 'Exercise N°{}'

print(title.format(1), '\n')

my_list = [34, 56, 76, 45, 2, 12, 67, 98, 37, 54, 66]

min_list = my_list.copy()

min_1 = min(my_list) #Save de lowest number
min_list.pop(min_list.index(min(min_list))) #Removes the lowest number from the copy of the original list

min_2 = min(min_list) #Save the lowest number from the new list

sum_min = min_1 + min_2

max_list = my_list.copy()

max_1 = max(my_list) #Save de highest number
max_list.pop(max_list.index(max(max_list))) #Removes the highest number from the copy of the original list

max_2 = max(max_list) #Save the highest number from the new list

sum_max = max_1 + max_2

print(my_list,'\n')
print('Sum two lowest numbers from list:', sum_min, '\n')
print('Sum two highest numbers from list:', sum_max, '\n')

print(title.format(2), '\n')

names = ["David", "Michael", "John", "James", "Greg", "Mark", "William", "Richard", "Thomas", "Steven", 
        "Mary", "Susan", "Maria", "Karen", "Lisa", "Linda", "Donna", "Patricia", "Debra"]

scores = [99, 87, 78, 86, 68, 94, 76, 97, 56, 98, 76, 87, 79, 90, 73, 93, 82, 69, 97, 98]

name = input('Enter your name: ')
print('')

print(name)
print('Your score is:', scores[names.index(name)], '\n')

print(title.format(3), '\n')

print('The maximum score is:', max(scores))
print('The amount of people that obtained that score is:', scores.count(max(scores)), '\n')

print(title.format(4), '\n')

months = ["January", "February", "March", "April", "May", "June", 
"July", "August", "September", "October", "November", "December"]

n_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

months_days = [months, n_days]

print(title.format(5), '\n')

#month_winter = [months_days[0][11], *months_days[0][0:2]]
#days_winter = [months_days[1][11], *months_days[1][0:2]]

summer = [months_days[0][5:8] , months_days[1][5:8]]
fall   = [months_days[0][8:11], months_days[1][8:11]]
winter = [[months_days[0][11], *months_days[0][0:2]], [months_days[1][11], *months_days[1][0:2]]]
spring = [months_days[0][2:5], months_days[1][2:5]]

print(title.format(6), '\n')

print('Summer lasts', summer[1][0] + summer[1][1] + summer[1][2], 'days')