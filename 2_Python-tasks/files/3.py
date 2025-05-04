with open ("D:/Industry/Projects/Sprints - Ai/Python-tasks/files/file.txt", "r") as f:
        data = f.read()
print(data)
data += "Hello Universe"
with open ("D:/Industry/Projects/Sprints - Ai/Python-tasks/files/file.txt", "w") as f:
    f.write(data)    
print(data)