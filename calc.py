print("Welcome to this calculator")
print("+,-,*,/")
c = input("Enter the operator")
if c == "+":
      x = input("Enter your first number")
      v = input("Enter your second number")
      print("The sum is", int(x) + int(v))
elif c == "-":
      x = input("Enter your first number")
      v = input("Enter your second number")
      print("The difference is", int(x) - int(v))
elif c == "*":
      x = input("Enter your first number")
      v = input("Enter your second number")
      print("The multiplication is", int(x) * int(v))
elif c == "/":
      x = input("Enter your first number")
      v = input("Enter your second number")
      print("The division is", int(x) / int(v))
else:
      print("Invalid operator")
