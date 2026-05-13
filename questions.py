#WAP to ask the user to enter names of their 3 favourite movies and store them in a list

# movies = []
# mov1 = input("Enter your first favourite movie: ")
# mov2 = input("Enter your second favourite movie: ")
# mov3 = input("Enter your third favourite movie: ")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

#WAP to check if a list contains a palindrome of elements

a = [1, 2, 3, 2, 1]
b = a.reverse()

if a ==b :
    print("The list is a palindrome")
else:  
    print("The list is not a palindrome")

#-----------------CORRECT ANSWER-----------------

list = [1, 2, 3, 2, 1]
copy_list = list.copy()
copy_list.reverse()

if copy_list == list:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")

# WAP to count the number of students with the A grade in follow tuple

tup = ("C", "D", "A", "A", "B", "B", "A")
print(tup.count("A"))

list = ["C", "D", "A", "A", "B", "B", "A"]
list.sort()
print(list)