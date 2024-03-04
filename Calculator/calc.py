def calculate(num1, num2, operator):
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      print("Error: Division by zero")
      return None
    else:
      return num1 / num2
  else:
    print("Error: Invalid operator")
    return None

while True:
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, or /): ")
    break
  except ValueError:
    print("Invalid input. Please enter numbers only.")

result = calculate(num1, num2, operator)
if result is not None:
  print("The result is:", result)
