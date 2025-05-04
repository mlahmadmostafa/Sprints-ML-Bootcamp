def OR(a, b):
    return a + b - AND(a,b)
def AND(a, b):
    return a * b
def XOR(a, b):
    return int(AND(OR(a, b), not AND(a, b)))
print("Numbers must be of equal length")
x = input("Enter the first digit binary number: ")
y = input("Enter the second digit binary number: ")
assert len(x) == len(y), "Numbers must be of equal length"
for i in range(len(x)):
    print(OR(int(x[i]),int(y[i])), end = "")
print()
for i in range(len(x)):
    print(AND(int(x[i]),int(y[i])), end = "")
print()
for i in range(len(x)):
    print(XOR(int(x[i]),int(y[i])), end = "")