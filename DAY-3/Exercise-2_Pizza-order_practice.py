'''
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small Pizza: $15

Medium Pizza: $20

Large Pizza: $25

Pepperoni for Small Pizza: +$2

Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: + $1
'''

print("Welcome to python Pizza Deliveries!")
option1 = input("What size pizza do you want? S, M, or L ")
option2 = input("Do you want pepperoni? Y or N ")
option3 = input("Do you want extra cheese? Y or N ")
bill = 0
if option1 == "S":
    bill += 15
    if option2 == "Y":
        bill += 2
elif option1 == "M":
    bill += 20
    if option2 == "Y":
        bill += 3
else:
    bill += 25
    if option2 == "Y":
        bill += 3
if option3 == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")
