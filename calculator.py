def calculator(first_num, operator, second_num):
    
    if operator == "+":
        return first_num + second_num
    elif operator == "-":
        return first_num - second_num
    
    elif operator == "*":
        return first_num * second_num
    
    elif operator == "/":
        if second_num == 0:
            return "Not define"
        else:
            return first_num / second_num


total = calculator(first_num = int(input("Enter first number: ")),operator = input("Enter the operator: ") ,second_num = int(input("Enter second number: ")))
print(f"The total is {total}")


# def calculator(first_num, operator, second_num):
#     if operator == "+":
#         return first_num + second_num
#     elif operator == "-":
#         return first_num - second_num
#     elif operator == "*":
#         return first_num * second_num
#     elif operator == "/":
#         if second_num == 0:
#             return "Division by zero is not allowed"
#         return first_num / second_num
#     else:
#         return "Invalid operator"

# try:
#     first_num = int(input("Enter first number: "))
#     operator = input("Enter the operator: ")
#     second_num = int(input("Enter second number: "))
#     total = calculator(first_num, operator, second_num)
#     print("Result:", total)
# except ValueError:
#     print("Invalid input. Please enter valid numbers.")
