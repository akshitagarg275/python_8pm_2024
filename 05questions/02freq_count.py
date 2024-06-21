# frequecy counter
# 'we are learning python'

sentence = 'we are learning python'
freq = {}

for char in sentence:
    # char has occured for the first time
    if freq.get(char) == None:
        freq[char] = 1
    else:
        freq[char] += 1

else:
    print(freq)

# WAP: to count the words 
# WAP : to consider the uppercase and lowercase letter as one
# Please python 
# {'p' : 2}