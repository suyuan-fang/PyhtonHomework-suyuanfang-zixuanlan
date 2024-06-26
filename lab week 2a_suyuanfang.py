#NAME:Suyuan Fang 
#Id:suyuanfang

#### fix the following errors!
#### do not use any web-based resources to figure them out

#1
x = 10
y = 20
print(x + y)

#2
my_list = [40, 50, 60, 70, 80, 100, 200, 400]
my_list_len = len(my_list)
print(my_list[my_list_len-1])

#3
my_string = 'hello world'
print(my_string.upper())

#4
z = ['a', 'b', 'c']
z += 'd'
print(z)

#5 run all these lines at once. why does the x not display 10, 
#followed by the 200?  Fix it so it does.
x = 10
print(x)
y = 20
print(x * y)

#6
color = 'My favorite color is {}, what is yours?'.format("blue")
print(color)

#7
color = 'My favorite color is {}, what is yours?'.format("yellow")
print(color)

#8
color = f'My favorite color is {"red"}, what is yours?'
print(color)

#### answer the following questions by adding lines, but without changing the code given

#9 make the entries in this list unique
schools = ['harris', 'booth', 'crown', 'harris', 'harris']
schools = list(set(schools))
print(schools)

#10 change the 'dog' entry to 'cat'
animals = tuple(['bird', 'horse', 'dog', 'fish'])
animals = list(animals)
animals[2] = 'cat'
animals = tuple(animals)
print(animals)

#11 separate the words in this string into entries in a list, with only lower-case
#letters, e.g. ['i', 'love', 'how', ...
my_sent = 'All that snow we had this winter sure was fun!'
words_separate = my_sent.lower().split()
print(words_separate)
