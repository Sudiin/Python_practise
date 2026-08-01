# # # list = [1, 2, 3, 4, 5, 6]

# # # for num in list:
# # #     print(num)

# # # vegies = ["tomato", "potato", "onion", "carrot", 12, 3]
# # # for num in vegies:
# # #     print(num)

# # tup = ( 1, 2, 3 , 4)

# # for el in tup:
# #     print(el)


# st = "SUDIN SHRESTHA"

# for num in st:
#     print(num)

# else:
#     print("Finsid")


# str = "SUDIN SHRESTHA"
# for num in str:
#     if num == "S":
#         print("FOUND")
#         break
# else:
#     print("NOT FOUND")



# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for x in list:
#     print(x)

# num = int(input("Enter the number you want to search: "))
# idx = 0
# for x in list:
#     if x == num:
#         print("Number found at index:", idx)
#         break
#     print("Finding")
#     idx += 1
# else:
#     print("Number not found")

num = int(input("Enter the number you want the factorial of: "))
fact = 1
i = 0
for i in range(1, num+1):
    fact = fact * i

print(fact)