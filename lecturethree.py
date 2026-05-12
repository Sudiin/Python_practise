marks = [94.4, 87.5, 44.3, 78.9, 56.7]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))


student = ["Sudin", 20, "Kathmandu"]
print(student)
student[0] = "Nasudin"
print(student)

str = "Hellow"
print(str[0])

top = [85, 95, 76, 63, 48] 
print(top[1:-1])

list = [ "banana", "apple", "grape", "orange"]
# list.append(4)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)

list.reverse()
print(list)

list.insert(2, 'litchi')
print(list)

list = [1, 3, 5, 9]
list.remove(3)
print(list)
list.pop(2)
print(list)