
# numbers = [10, 20, 30, 40, 50]

# total_sum = 0

# for n in numbers:
#     total_sum += n
#     # total_sum = total_sum + n     both valid
# print(total_sum)


# scores = [85, 42, 78, 90, 33, 61]


# for score in scores:
#     if score >= 60:
#         print("Passed:", score)


# user_names = ["Alice", "Bob", "Charlie", "David"]

# for name in user_names:
#     print("Hello", name)


# contacts = {
#     'Bamia': 'bamia@gmail.com',
#     'Butzu': 'butzu@gmail.com',
#     'Shai': 'shai@gmail.com',
# }
# contacts['Dani'] = 'dani@gmail.com'
# contacts['Mehanem'] = 'mehanem@gmail.com'
# contacts.pop('Dani')

# print(contacts)


users = [
    {"name": "Alice", "job": "Engineer"},
    {"name": "Bob", "job": "Designer"},
    {"name": "Charlie", "job": "Manager"}
]


# for user in users:
#     if user["job"] == "Engineer":
#         print("Job Title:", user["job"])


# for user in users:
#     if user["job"] == "Engineer":
#         print("Job Title:", user["job"])


# for user in users:
#     if user["job"] != "Manager":
#         print("Job title: ", user["job"])


products = [
    {"item": "Laptop", "price": 1000, "in_stock": True},
    {"item": "Mouse", "price": 25, "in_stock": False},
    {"item": "Monitor", "price": 300, "in_stock": True}
]


# for product in products:
#     print(product["price"])


# for product in products:
#     if product["price"] < 400:
#         print(product["item"])


# for product in products:
#     if product["in_stock"]:   # same as if     product["in_stock"] == True:
#         print(product["item"])


# for student in students:
#     if student["active"] and student["score"] > 80:
#         print(student["name"])


# for student in students:
#     if student["score"] > 90 or student["active"]:
#         print(student["name"])


# students = [
#     {"name": "Daria", "score": 85, "active": True},
#     {"name": "Ethan", "score": 92, "active": False},
#     {"name": "Fiona", "score": 78, "active": True}
# ]


# for student in students:
#     if student["active"]:
#         print(f"{student["name"]} has a score of {student["score"]}")


# students = [
#     {"name": "Daria Morgendorffer", "score": 85, "active": True},
#     {"name": "Ethan Hunt", "score": 92, "active": False},
#     {"name": "Fiona Gallagher", "score": 78, "active": True}
# ]


# for student in students:
#     if student["active"]:
#         print(f"hello! {student["name"].split()[0]}")


# users = [
#     {"email": "john@gmail.com", "active": True},
#     {"email": "sarah@yahoo.com", "active": False},
#     {"email": "mike@hotmail.com", "active": True}
# ]


# for user in users:
#     if user["active"]:
#         print(f"user {user['email'].split('@')[0]} is ready")
