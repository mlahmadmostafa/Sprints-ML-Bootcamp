class Record:
    def __init__(self):
        self.record = {}

    def add(self, name, age, grade):
        self.record[name] = {"age": age, "grade": grade}
        print("Record added successfully")

    def get(self, name):
        return self.record[name]
    def update(self,name, age = None, grade = None):
        if age == None and grade == None:
            print("Please provide age and/or grade")
            return
        if age == None:
            self.record[name]["grade"] = grade
            print("Record age updated successfully")
            return
        if grade == None:
            self.record[name]["age"] = age
            print("Record grade updated successfully")
            return
        self.record[name]["age"] = age
        self.record[name]["grade"] = grade
        print("Record age and grade updated successfully")
        return
    
c = Record()
c.add("Ahmad", 10, 90)
c.add("Rofida", 20, 80)


print("Rofida's record:", c.get("Rofida"))
c.update("Rofida", 25)
print("Rofida's record after updating age:", c.get("Rofida"))
c.update("Rofida", 25, 75)
print("Rofida's record after updating age and grade:",c.get("Rofida"))