from pandas import DataFrame as df
class Book:
    # This is a constructor
    def __init__(self, title, author, pages):
        self.title = title # an attribute
        self.author = author
        self.pages = pages
    def describe(self): # A method
        # Sorry had to use df to print the table, It looked awful not organized.
        print(df([['Title', 'Author', 'Pages'],
                  [self.title,self.author,self.pages]]))
        
book1 = Book("The Alchemist", "Paulo Coelho", 208)
book1.describe()