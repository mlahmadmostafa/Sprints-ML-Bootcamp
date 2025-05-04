for x in range(100): # For loop to 100
    # if elifs is used to avoid printing empty lines, as it can be done with printing only Fizz and Buzz with end = ''
    if x%3==0 and x%5==0: # If the number is divisible by both 3 and 5
        print("For x = ", x, "FizzBuzz")
    elif x%3==0: # If the number is divisible by 3
        print("For x = ", x, "Fizz")
    elif x%5==0: # If the number is divisible by 5
        print("For x = ", x, "Buzz")