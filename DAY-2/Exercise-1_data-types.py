'''Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8'''

two_digit_number = input("Type a two digit number:")
converted = str(two_digit_number)
sumnum = int(converted[0]) + int(converted[1])
print('\n', sumnum)
