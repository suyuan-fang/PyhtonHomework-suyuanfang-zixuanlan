#NAMES Suyuan Fang
#Unless otherwise noted, try solving these using class content and without searching online

#1
#Modify this code so that when i is 5 it doesn't print anything (including Finished!)
#and instead moves directly onto 6, while leaving it unchanged for other values of i
i = 0
while i < 10:
    if i == 5:
        i += 1
        continue
    if i < 5:
        print('Little')
    else:
        print('Big')
    print('Finished!')
    i += 1    
#2
#Write a for loop that prints this pattern:
#HINT: you can write a for-loop inside of a for-loop

#1
#1 2
#1 2 3
#1 2 3 4
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

#3
start_list = [[2, 3, 4], [6, 8, 9]]
#turn it into [1,    2,   3, 4   ]  
#NOTE:  The spacing is just to show which numbers are converted to which
#HINTS: There are three steps here: mapping, filtering, and flattening the nested lists
#       Try doing this in a for-loop, then try doing it in a list comprehension
#       You may need to check StackOverflow for how to flatten a nested list
new_list = []
for sublist in start_list:
    for item in sublist:
        # Check if the item is even
        if item % 2 == 0:
            # Transform the even number by dividing it by 2
            transformed_item = item // 2
            new_list.append(transformed_item)
print(new_list)

#4
import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
#turn it into {'Noah': datetime.datetime(1999, 2, 23),
#              'Sarah': datetime.datetime(2001, 9, 1),
#              'Zach': datetime.datetime(2005, 8, 8)}
#HINTS: The datetime library has a function that turns strings of the right format into dates
#       Again, start with a for-loop, but make a dictionary comprehension in the end
transformed_dict = {name.capitalize(): datetime.datetime.strptime(date_str, '%m/%d/%Y').date() 
                    for name, date_str in start_dict.items()}
print(transformed_dict)


