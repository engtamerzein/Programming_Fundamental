# review the variables
# number -> integer -> int
# decemail number -> float
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
# fiurst_letter = first_item[0]

# difference between function, method and variable
# # keyword if, for, while, int, str
# if statement
# input_grade.isdigit()
# and, or

# 70 -> good, 50 -> pass
input_grade = input("please enter your grade: ")
if input_grade.isdigit():
    grade = int(input_grade)
    # print(grade >= 50)
    if grade >= 70:
        print("you grade is passed")
    elif grade >= 50:
        print("you are good")
    else:
        print("you are failed")

    print("-" * 20)
else:
    print("please enter a valid number")


# is_study_math = False
# is_study_history = True
# can_play = is_study_math or is_study_history
# print(can_play)

# exercise: 1
# if the temprture between 20 and 25 print the weather is good, else print the weather is bad
# input_number = 10
# result = input_number>= 20 and input_number <= 25
# print(result)

# exercise: 2
# make the game of head or tail
import random

user_guess = input("Guess 'Head' or 'Tail': ").lower()

# Validate user input
if user_guess in ["head", "tail"]:

    # Define the possible outcomes of a coin flip
    outcomes = ["Head", "Tail"]

    # Randomly choose one outcome from the list
    result = random.choice(outcomes)

    # Print the result of the coin flip
    print(f"The coin landed on: {result}")

    # Compare user's guess with the actual result
    # Convert the result to lowercase for case-insensitive comparison
    if user_guess == result.lower():
        print("Congratulations! You guessed correctly!")
    else:
        print("Sorry, you guessed incorrectly. Better luck next time!")

    print("Thanks for playing!")
else:
    print("Invalid guess. Please enter 'Head' or 'Tail'.")
