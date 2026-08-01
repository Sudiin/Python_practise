# i = 1
# while i <= 10000 :
#     print("Hello", i)
#     i += 1
# print(i)

# num = 1
# while num <= 5 :
#     print(num, " : ", num)
#     num += 1


# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# i = 100
# while i >= 1:
#     print(i)
#     i =- 1

# n = int(input("Enter the number you want the table of: "))
# i = 0

# while i<= 12:
#     print(n, "X", i, "=", n*i)
#     i += 1

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# i = 0
# while i < len(a):
#     print(a[i])
#     i+=1

# a = (1, 4, 9 , 16, 25, 36, 49, 64, 81, 100)

# i = 0
# num = int(input("Enter the number you want to search: "))

# while i <len(a): 
#     if a[i] == num:
#         print("Number found at index: ", i)
#         break
#     else:
#         print("Finding")
#     i += 1
# else :
#     print("Number not found")

i = 1

while i <= 10:
    if(i%2) == 0:
        i+=1
        continue
    print(i)
    i+=1


num = int(input("Enter the number you want to add upto: "))
i = 0
sum = 1
while i <= num:
    sum += i
    i += 1
print(sum)
