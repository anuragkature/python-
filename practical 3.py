# To check nth term of the Fibonacci sequence
n = int(input("Enter the value of n: "))
a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a + b

# To check inputs prime or not
num = int(input("Enter a number to check if it is prime: "))
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        print(f"{num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")