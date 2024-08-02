'''
Aim : to implement a student library system using object oriented programming where a student can borrow a book from the  list of books 

To do : create a separate library and a student class. program must be menu driven

'''

class Library:

    def __init__(self,bookslist):
        self.books = bookslist

    def display(self):
        print("Books in library are: ")
        for book in self.books:
            print(" * " +book)
    
    def borrow(self,bookname):
        if bookname in self.books:
            print(f"Book issued is {bookname}. return it within 30 days")
            self.books.remove(bookname)
            return True
        else:
            print("Book has been borrowed by other student")
            return False

    def returned(self,bookname):
        self.books.append(bookname)
        print(" Returned book ")


class Student:
    def request(self):
        self.book = input("Enter the name of the book you need ")
        return self.book
    
    def returned(self):
        self.book = input("Enter the name of the book you returned ")
        return self.book


if __name__ == "__studentLibrary__":
    central = Library(["Algorithms", "python","java","c","c++","R","Webdevelopment"])
    student = Student()
    central.display()

    while(True):
        welcome = '''*****Welcome to central library*****
        please choose an option :
        1. Listing a book
        2. Request a book 
        3. Return a book
        4. Exit the Library
    
        '''
        print(welcome)

        a = int(input("Enter a choice: "))
        if a == 1:
            central.display()
        elif a == 2:
            central.borrow(student.request())
        elif a == 3:
            central.returned(student.returned())
        elif a == 4:
            print("Thank you! visit again")
            exit()
        else:
            print("Invalid choice!")

