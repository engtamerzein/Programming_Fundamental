# review the variables
# number -> integer -> int
# decimal number -> float
# text => string -> str-> text + text, text[0], text[-1], text[2:3], len(text), text.upper(), text.lower()
# escape character -> \n, \", \\
# list = list['text', num] -> list[0] -> len(list) -> list.append("") -> list.insert(1, "") -> list.pop()
# text = number -> number as text -> num = int(text)
# number = text -> error -> text = str(num)
# type(text) -> str

# exercise of full_name.splite(" ")
# full_name = "tamer ali sami"
# names = full_name.split(" ")
# print(names)
# first_name = names[0][0].upper() + names[0][1:]
# print(first_name)
# first_item = names[0]
# first_letter = first_item[0]

# difference between function, method and variable
# # keyword if, for, while, int, str
# if statement
# input_grade.isdigit()
# and, or

# grade = 80
# good = grade >= 70
# passed = grade >= 50
# if grade >= 70:
#     print("you are good")
# elif grade >= 50:
#     print("you are pass")
# else:
#     print("your are fail")

# exercise: 1
# grade >= 80 -> your grade is A
# grade >= 70 -> your grade is B
# grade >= 60 -> your grade is C
# grade >= 50 -> your grade is D
# grade < 50 -> you fail

# input_grade = input("please enter your grade: ")
# if input_grade.isdigit():
#     grade = int(input_grade)
#     if grade >= 70:
#         print("you grade is passed")
#     elif grade >= 50:
#         print("you are good")
#     else:
#         print("you are failed")

#     print("-" * 20)
# else:
#     print("please enter a valid number")


# is_study_math = False
# is_study_history = True
# can_play = is_study_math or is_study_history
# print(can_play)

# exercise: 2
# if the temprture between 20 and 25 print the weather is good, else print the weather is bad
# input_number = 10
# result = input_number>= 20 and input_number <= 25
# print(result)

