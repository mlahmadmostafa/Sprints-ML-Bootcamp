class calculator:
    def __init__(self): # Not necessary
        pass 
    def add(self,x,y): # to add
        return x+y
    def sub(self,x,y): # to subtract
        return x-y
    def mul(self,x,y): # to multiply
        return x*y
    def div(self,x,y): # to divide
        return x/y
# With variable
x, y = 5, 3
add = x+y
sub = x-y
mul = x*y
div = x/y

print("Addition variable      ", add)
print("Subtraction variable   ", sub)
print("Multiplication variable", mul)
print("Division variable      ", div)

# With class
c = calculator()

print("Addition      ", c.add(x,y))
print("Subtraction   ", c.sub(x,y))
print("Multiplication", c.mul(x,y))
print("Division      ", c.div(x,y))

# User input
while True:
    try: # to handle x, y type error
        user_input_x = int(input("type x: "))
        user_input_y = int(input("type y: "))
        user_input_op = input("type operator: ")
    except ValueError:
        print("Invalid input")
        continue
    if user_input_op not in ["+","-","*","/"]: # to handle invalid operator
        print("Invalid operator")
        continue
    if user_input_op == "+":
        print(c.add(user_input_x, user_input_y))
    elif user_input_op == "-":
        print(c.sub(user_input_x, user_input_y))
    elif user_input_op == "*":
        print(c.mul(user_input_x, user_input_y))
    elif user_input_op == "/":
        print(c.div(user_input_x, user_input_y))

