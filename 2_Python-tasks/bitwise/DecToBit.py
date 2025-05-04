# Firsst Method
dec = int(input("Enter a decimal number: "))
print(f"Method 1: {dec:08b}")

# Second Method
bin_ = ""
def decToBin(dec):
    if dec == 0:
            return '0'
    bin = ""
    while dec > 0:
        bin = str(dec%2) + bin
        dec //=2
    return bin
        

print("Method 2:", decToBin(dec))

# Third Method
print("Method 3:", bin(dec))