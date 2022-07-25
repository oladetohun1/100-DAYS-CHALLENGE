'''
You are going to write a program that will mark a spot with an X.

In the starting code, you will find a variable called map.

This map contains a nested list. When map is printed this is what the nested list looks like:

    ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']

    In the starting code, we have used new lines (\n) to format the three rows into a square, like this:

    ['⬜️', '⬜️', '⬜️']

    ['⬜️', '⬜️', '⬜️']

    ['⬜️', '⬜️', '⬜️']

    This is to try and simulate the coordinates on a real map.
First, your program must take the user input and convert it to a usable format.

Next, you need to use it to update your nested list with an "x".

Example Input 1
column 2, row 3 would be entered as:

    23
'''
# ��� Don't change the code below ���
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
#print(map)
position = input("Where do you want to put the treasure? ")
# ��� Don't change the code above ���

#Write your code below this row ���
row = int(position[0])
column = int(position[1])
map[column - 1][row - 1] = 'x'




#Write your code above this row ���

# ��� Don't change the code below ���
print(f"{row1}\n{row2}\n{row3}")
