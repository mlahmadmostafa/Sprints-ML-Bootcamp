class AgeError(Exception):
    def __init__(self, message):
        super().__init__(message)

while True:
    age = int(input("Enter your age: "))
    if age > 120:
        raise AgeError("Are you sure you're that old!")