class library:
    def __init__(self, listofbooks):
        self.books = listofbooks

        
    def displayAvailabaleBooks(self):
        print("Books present in the library")
        for book in self.books:
            print(" *" + book)
    def borrowBook(self, bookName):
            if bookName in self.books:
                print(f"you have been issued {bookName}. Please keep it safe and return it within 30 days ")
                self.books.remove(bookName)
                return True
            else:
                print("Sorry, THis book is either not available or has  already b issued to someon else. Please wait  the book is returned")
                return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it! Have a great day ahead")

class student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book
    def retunBook(self):
        self.book = input("Enter the name of the book you want to return/Add: ")
        return self.book



if __name__ == "__main__":
    centrallibrary = library(["algorithms", "Django", "clrs", "python Notes", "Networking", "os", "flask", "Html", "Css", "java", "flutter"])
    student = student()
    # centrallibrary.displayAvailabaleBooks()
    while (True):
        WelcomeMsg = '''
        =====Welcome To Central Library=====
        please choose an option 
        1. List all the book
        2. Request a book
        3. Add/Return a book
        4. Exit the library'''
        print(WelcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centrallibrary.displayAvailabaleBooks()
        elif a == 2:
            centrallibrary.borrowBook(student.requestBook())
        elif a == 3:
            centrallibrary.returnBook(student.retunBook(), student.user_return_book())
        elif a == 4:
            print("Thanks for choosing central library. Have a great day ahead...")
            exit()
        else:
            print("Invalid Choice!")


    