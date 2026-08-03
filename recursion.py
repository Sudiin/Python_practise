# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
#     print("END")

# show(3)


def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n*fact(n-1)

print(fact(5))


def sum(n):
    if(n == 0):
        return 0
    else:
        return n + sum(n-1)

print(sum(4))

def prlist(lst, idx=0):
    if(idx == len(lst)):
        return
    print(lst[idx])
    prlist(lst, idx + 1)

fruits = ["mango", "apple", "litchi", "bannaana"]
prlist(fruits)


#===============================


a = [1, 2, 3, 10, 15, 11]

def find_max(lst, idx):
    if(idx == idx - 1):
        return
    elif lst[idx] > lst[idx + 1]:
        print(lst[idx])

find_max(a, 0)