# f = open('demo.txt', "r")

# data3 = f.read()
# print(data3)

# data = f.readline()
# data1 = f.readline()

# print(data)
# print(data1)

# print(type(data))

# f.close()



# f = open("demo.txt","r+")


# f.write("abc")

# data = f.read()

# print(data)

# f.close

# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt", "w") as f:
#     f.write("new data")
#     print(data)


# deleting a  file

# import os
# os.remove("demo.txt")

# with open("demo.txt", "w") as f:
#     f.write("Hi everyone\n")
#     f.write("we are learning File I/O\n")
#     f.write("using python\n")


# with open("demo.txt", "r+") as f:
#     data = f.read()

# new = data.replace ("python", "Java")
# print(new)

# with open("demo.txt", "w") as f:
#     f.write(new)

with open("demo.txt", "r") as f:
    data = f.read()
    if(data.find("learning") != -1):
        print("Found")
    else:
        print("not found")