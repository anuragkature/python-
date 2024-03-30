 # Function to convert decimal to binary
def dec_to_binary(n):
    return bin(n)[2:]

# Function to convert decimal to octal
def dec_to_octal(n):
    return oct(n)[2:]

# Function to convert decimal to hexadecimal
def dec_to_hexadecimal(n):
    return hex(n)[2:]

num = int(input("Enter a decimal number: "))
print("Binary equivalent: ", dec_to_binary(num))
print("Octal equivalent: ", dec_to_octal(num))
print("Hexadecimal equivalent: ", dec_to_hexadecimal(num))