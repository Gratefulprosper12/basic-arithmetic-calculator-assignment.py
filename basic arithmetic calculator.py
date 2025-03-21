# asking the user to inputtwo numbers
num1 = float(input("enter your first number: "))
num2= float(input("enter your second number: "))
# asking the user to input a mathametical operation
operation = input("Enter the operation from (+, -, *, /, **, %, //,): ")
# perform the operation based on the users input
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == '**':
    result = num1**num2
    print(f"{num1} ** {num2} = {result}")

elif operation == '*':
     result = num1*num2
     print(f"{num1}*{num2} = {result}")

elif operation == '//':
     result = num1//num2
     print(f"{num1}//{num2} = {result}")

elif operation == '%':
     result = num1%num2
     print(f"{num1}%{num2} = {result}")

elif operation == '/':
 if num2 !=0:
     result = num1/num2
     print(f"{num1}/{num2} = {result}")
 else: 
     print("error: division by zero is not allowed.")

else:
      print("invalid operation: please enter one of +, -, *, /, **, %, //.")
