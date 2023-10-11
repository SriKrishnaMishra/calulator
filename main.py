num1 = float(input("enter the num1:"))
num2 = float(input("enter the num2:"))

operator = input("enter an operator (+ - * / ):")

if operator == "+":
 print(num1 + num2)
elif operator == "-":
  print(num1 - num2)
elif operator == "*":
  print(num1 * num2)
elif operator == "/":
 print(num1 / num2)
else:
  print("invalid operator")



