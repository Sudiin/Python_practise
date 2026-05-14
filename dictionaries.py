# info = {
#     "key": "value",
#     "name": "Sudin Shrestha",
#     "age": 20,
#     "is_adult": True,
#     "subjects": ["Math", "Science", "Social"],
#     "topics": ("Dictionaries", "lists"),
# }

# print(info)
# print(info["name"])
# info["name"] = "Sudiin"
# info["Surname"] = "Shrestha"
# print(info["name"]) 

# null_dict = {}
# null_dict["name"] = "Sudin"



student = {
    "name" : "Simrika",
    "subject" : {
        "Math" : 90,
        "Science" : 80,
        "Social" : 85
    }
}

print(student["subject"])
print(student["subject"]["Math"])

pairs = list(student.keys())
print(pairs[0])
print(list(student["subject"].keys()))
print((student.values()))
print(student.items())

print(student.get("name"))
print(student["name"])
student.update({"city": "Kathmandu"})

new_dict = {"Country":"Nepal", "Language" : "Nepali"}
student.update(new_dict)