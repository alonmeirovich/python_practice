# name = "Alon"
# age = 666
# money = 10,000,000
#
# if age < 18:
#    print("YES")
# elif age > 18:
#    print("WOW! So Old!")
#
# print("DONE")


# name = "Alon"
# if name == "Alon":
#    print ("YES")
# else:
#    print ("NO")


# count = 4
#
# while count > 0:
#    print("Hello")
#    count = count -1
# print("Done")
#
# for count in range(4):
#    print("Hello")
# print("Done")


# user_1 = input("Please enter your name: ")
# user_2 = input("Please enter your name: ")
# user_3 = input("Please enter your name: ")
# user_4 = input("Please enter your name: ")


# def users(user_1, user_2, user_3, user_4):
#     for user in users:
#         return input("Please enter your name: ")


number_of_names = input("How many names do you have? ")
names = []
for count in range(int(number_of_names)):
    name = input("Please enter your name: ")
    names.append(name)

for name in names:
    print(name)

name
