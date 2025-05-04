while True:
    try:
        num = int(input("Enter a number: "))
    except KeyboardInterrupt:
        print("It is rude to KeyboardInterrupt a computer")
    except ValueError:
        print("Invalid input. Please enter a valid number, PLEASE!")
    else:
        print("You made the code work, DO YOU EXPECT A THANK YOU?")
    finally:
        print("One more loop is done, whether u crashed it or not")