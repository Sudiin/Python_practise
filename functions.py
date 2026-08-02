#function definition
def sum(a, b): #paramteres
    return a + b

print(sum(5, 7)) #function call

def print_Hello():
    print("Hello Wold!!")

print_Hello()
print_Hello()
print_Hello()

#averge of 3 numebrs
def average(a, b, c):
    print((a+b+c)/3)
    return (a+b+c)/3

average(1,2,3)


#waf to print the length of a list
nums = [1, 2, 3, 4, 5]
alphabet = ["a", "b", "c" ,"d"]

def print_list(list):
    print(len(list))

print_list(nums)
print_list(alphabet)

#waf to print the elemnts of a list in a signle line

# nums1 = [1, 2, 3 , 45 ]

# def print_online(list):
#     print(list)

# print_online(nums1)

# def print_line(list):
#     for item in list:
#         print (item, end = " ")

# print_line()


# #waf to find the factorial of n.

def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

fact(5)


def currency(a):
    return a * 150

print("the amount after converting to US dollar is ", currency(20))

#waf to take input to check odd or even

num = int(input("Enter the number you wanna check: "))
def check_oddeven(num):
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd")

check_oddeven(num)