# info = {
#     "key": "value",
#     "name": "Sudin",
#     "learning": "Python",
#     "topics" : ["Python", "Django", "Flask"],
#     "age"  : 20,
#     12.99: 94.4
# }

# null_dict = {}

# print(null_dict)
# print(type(info))
# # print(info["name"])
# # print(info["topics"])

# # info["name"] = "Sudin Shrestha"
# # print(info["name"])

# # null_dict["name"] = "Sudin"

# # student = {
# #     "name": "Sudin",
# #     "Subjects" : {
# #         "CN" : 90,
# #         "OS" :80,
# #         }
# # }

# # print(student.keys())

info = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat" : "a small animal ",
}

print(info)

marks = {}

x = int(input("enter your C marks:"))
marks.update({"c": x})
y = int(input("enter your CN marks:"))
marks.update({"cn": y})

print(marks)