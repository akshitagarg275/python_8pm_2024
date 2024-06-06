# WAP to find the no of digits entered by the user
# 546 -> 3

# num = int(input("enter the number: "))
# count = 0

# while num > 0:
#     # rem = num % 10
#     count = count + 1
#     num = num // 10
# else:
#     print("No of digits: ", count)    

# TODO: WAP to add all the digits
# 546 -> 15

num = int(input("enter the number: "))
sum = 0

while num > 0:
    rem = num % 10
    sum = sum + rem
    num = num // 10
else:
    print("sum of digits: ", sum)   

# TODO: WAP to multiply the digits
