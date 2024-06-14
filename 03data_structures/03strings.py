# strings -> '' , " " , ''' '''

'''
immutable
indexing is available
order is fixed 
iterable
'''

s = 'we are learning python'
# print(s)
# print(type(s))
# print(len(s))

# TODO: iterable
# for i in s:
#     # print(i)
#     print(i, end ="")

# TODO: immutable
# s[0] = 'W'
# print(s)

#TODO: indexing
s = 'we are learning python'
# print(s[0])
# print(s[-1])

# TODO: slicing 
# print(s[1:10])
# print(s[: : 2])
# print(s[-14 : ])

s = 'we are learning python'

# print(s.capitalize())
# print(s.lower())
# print(s.upper())

# print(s.center(50, '*'))
# print(s.count('e'))
# print(s.count('e', 3))
# print(s.count('ar'))

# print(s.endswith("on"))
# print(s.startswith("we"))

# print(s.find("we"))
# print(s.find("We"))   #-1

# print(s.index('We'))

# TODO: concatenation
# print(5 + 3)
# print('5' + '3')

# TODO: format

n1 = 5
n2 = 3
ans = n1 + n2

#  5 + 3 = 8

# print(str(n1) + ' + ' + str(n2) + ' = ' + str(ans))

# print("{0} + {1} = {2} ".format(n1, n2, ans))

# print("{1} + {0} = {2} ".format(n1, n2, ans))


# TODO: f-strings
# print(f"{n1} + {n2} = {ans}")

# TODO: raw strings

'''
escape sequences: 
\\ : \
\' : '
\b : backspace
\a : alert
\n : new line
'''

# p = r"C:\\imp\new_folder\backup\and"
# print(p)

# s = "122324as  "
# s = 'False'
s ="   "

# print(s.isnumeric())
# print(s.isalnum())
# print(s.isidentifier())

# print(s.islower())
# print(s.isspace())

# TODO: strip : reducing extra white spaces
p = "      p@ssword    "
# print(p.lstrip())
# print(p.rstrip())
# print(p.strip())


# TODO: replace
s = "we are learning python"
# print("Before: ",s)
# s = s.replace('a', '@')
# s = s.replace('a', '@', 1)
# print("After: ", s)

# TODO: split
s = "we are learning python"
# print(s.split())
# print(s.split('e'))
# print(s.split(" ",2))


# TODO: join
fname = "john"
lname = "doe"

userName = ".".join([fname, lname])
print(userName)

companyName = "abc.com"

email = "@".join([userName, companyName])
print(email)


