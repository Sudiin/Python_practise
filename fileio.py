# f = open('demo.txt', "r")

# data3 = f.read()
# print(data3)

# data = f.readline()
# data1 = f.readline()

# print(data)
# print(data1)

# print(type(data))

# f.close()



f = open("demo.txt","r+")


f.write("abc")

data = f.read()

print(data)

f.close
