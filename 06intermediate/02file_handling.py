# File handling 
# to store the data or fetch the data
'''
text file -> .txt, .py, .html, .text
modes:
r -> read mode
w -> write mode
a -> append mode

binary file -> .pdf, .png, .jpeg, .mp3, .mp4
mode:

rb -> read mode
wb -> write mode
ab -> append mode

open(file_path , mode)

'''

# file = open("./01functions.py" , "r")
# file = open("../01basics/00hello.py", "r")
# print(file)
# print(type(file))
# print(file.read())
# print(file.readlines()[0])
# print(file.readline())
# print(file.readline())
# print(file.readline())

# for i in file:
#     print(i)

# TODO: skips the no of characters passed in the method
# file.seek(5)
# print(file.read(10))

# file.seek()

# file.close()




# TODO: write mode
# file = open("./copy.txt", "w")
# file.write("I am writing using python program")
# file.write("Another data")
# file.close()

# TODO: append mode
# file = open("./copy.txt", "a")
# file.write("Writing in append mode")
# file.writelines(["Line1 \n", "Line2 \n"])
# file.close()


# f1 = open("./01functions.py", "r")

# with open("./01functions.py", "r") as f1:
#     print(f1.read())

# print("Outside")

# with open("./01functions.py", "r") as f1, open("./function_copy.py", "w") as f2:
#     for data in f1:
#         f2.write(data)
    

# TODO: binary file

# with open("./sst.png", "rb") as f1:
    # print(f1.read())

with open("./sst.png", "rb") as f1, open("./copy.png", "wb") as f2:
    for data in f1:
        f2.write(data)