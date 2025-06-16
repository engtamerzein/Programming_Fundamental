
# num_1_input = "55.256"  # input("please enter the first number: ")
# nums_1 = num_1_input.split(".")
# nums_1 = ["55", "256"]

# # print(55 + 0.25)
# # print(256 / 100)
# # print(10**3)

# if len(nums_1) == 2 and nums_1[0].isdigit() and nums_1[1].isdigit():
#     num_1 = int(nums_1[0])
#     num_2 = int(nums_1[1])

#     len_num_2 = len(nums_1[1])  # 2

#     final_num = num_1 + (num_2 / 10**len_num_2)
#     # print(final_num)

# print(nums_1)

# num = 5.5
# print(type(num))

# quit()

OPERATIONS = ["+", "-", "*", "/"]

num_1_input = input("please enter the first number: ")  # a
num_2_input = input("please enter the second number: ") # 20
operation = input("please enter the operation (+, -, * , /): ") # a

# num = "-56"
# if num[0] == "-" and num[1:].isdigit():
#     num = int(num[1:]) * -1


if operation not in OPERATIONS:
    print("please try again")
    quit()


if num_1_input[0] == "-" and num_1_input[1:].isdigit() or num_1_input.isdigit():
    num_1 = int(num_1_input)
elif len(num_1_input) == 2 and num_1_input[0].isdigit() and num_1_input[1].isdigit():
    num_1 = float(num_1_input)
elif num_1_input[0] == "-" and len(num_1_input) == 2 and num_1_input[0].isdigit() and num_1_input[1].isdigit():
    num_float = num_1_input[1:]
    num_float_part_1 = int(num_1_input[0])
    num_float_part_2 = int(num_1_input[1])
    len_part_2 = len(num_1_input[1])
    num_1 = num_float_part_1 + (num_float_part_2 / 10**len_part_2)
    num_1 = num_1 *-1
else:
    print("please try again")
    quit()

if num_2_input[0] == "-" and num_2_input[1:].isdigit():
    num_1 = int(num_2_input) * -1
elif num_2_input.isdigit():
    num_1 = int(num_2_input)
elif len(num_2_input) == 2 and num_2_input[0].isdigit() and num_2_input[1].isdigit():
    num_2 = float(num_2_input)
elif num_2_input[0] == "-" and len(num_2_input) == 2 and num_2_input[0].isdigit() and num_2_input[1].isdigit():
    num_float = num_2_input[1:]
    num_float_part_1 = int(num_2_input[0])
    num_float_part_2 = int(num_2_input[1])
    len_part_2 = len(num_2_input[1])
    num_1 = num_float_part_1 + (num_float_part_2 / 10**len_part_2)
    num_1 = num_1 *-1
    # num_2_input = 00
    # operation = "/"
elif int(num_2_input) == 0 and operation == "/":
    print("please try again")
    quit()
else:
    print("please try again")
    quit()
# operation logic