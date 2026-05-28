

ones = {1:"one",
2:"two",
3:"three",
4:"four",
5:"five",
6:"six",
7:"seven",
8:"eight",
9:"nine"}

teens = {10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
tens = {20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}
output = ""
choice = input("pick a number 3 digit.\n>")
digit_count = len(choice)

if int(choice[0]) in ones and digit_count == 3:
    output += ones[int(choice[0])] + " hundred "
    choice = choice[1:]

if int(choice) in teens and digit_count == 3:
    output += " and " + teens[int(choice)]

elif int(choice) >= 20:
    num = int(choice)

    tens_digit = (num // 10) * 10
    ones_digit = num % 10

    output += " and " + tens[tens_digit]

    if ones_digit != 0:
        output += " " + ones[ones_digit]



print(output)







