while True:
    try:
        with open ("D:/Industry/Projects/Sprints - Ai/Python-tasks/files/file.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found")
    