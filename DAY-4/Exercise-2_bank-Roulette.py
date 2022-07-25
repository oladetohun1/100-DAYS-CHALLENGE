'''
Instructions
You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

When you run the code, just use a random number as the seed. e.g. 67346 It doesn't matter what you chose, it's only for our testing code to check your work.
'''


import random
# íº¨ Don't change the code below í±‡
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# íº¨ Don't change the code above print(names,"\n")
#Write yourode below this line í±‡
num_items = len(names)
choice = random.randint(0, num_items - 1)

person = names[choice]

print(person + " is going to buy the meal today!")
