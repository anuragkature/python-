# To check greater number
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num1 < num2:
   print(f"{num2} is greater than {num1}.")
else:
    print("Both numbers are equal.")
# To check number even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# To swap two number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Before swapping: num1 =", num1, "and num2 =", num2)
num1, num2 = num2, num1
print("After swapping: num1 =", num1, "and num2 =", num2)