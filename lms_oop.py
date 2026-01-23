# Book Class
class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        self._available=True
    
    def _is_available(self):
         return self._available
# Member Class  
class Member:
    def __init__(self,member_id,name):
        self.member_id=member_id
        self.name=name
        self.borrowed_books=[]

# Library Class
class Library:
    def __init__(self):
        self.books={}
        self.members={}
    
    def add_book(self):
        isbn=input("Enter ISBN : ")
        if isbn in self.books:
            print("This Book already exists.")
            return
        
        title=input("Enter Book name : ")
        author=input("Enter author name : ")

        book=Book(title,author,isbn)
        self.books[isbn]=book      #At that particular isbn put the book details
        print("Book Added successfully!")

    def add_member(self):
        member_id=input("Enter member id : ")
        if member_id in self.members:
            print("Member with this ID already exists.")
            return
        name=input("Enter member name : ")

        member=Member(member_id,name)
        self.members[member_id]=member
        print("Member Added Successfully!")

    def view_member(self):
        if not self.members:
            print("No member registered yet")
            return
        for member_id, member in self.members.items():
            print(f"Member_id : {member_id} | Member_name : {member.name} | Borrowed books : {member.borrowed_books}")

    def view_books(self):
        if not self.books:
            print("No Books available")
            return
        for isbn,book in self.books.items():
            if book._available:
                status="Available"
            else:
                status="Borrowed"
            print(f"Title : {book.title} | Author : {book.author} | ISBN : {isbn} | {status}")
    
    def borrow_book(self):
        isbn=input("Enter ISBN : ")
        member_id=input("Enter member ID : ")

        if isbn not in self.books and member_id not in self.members:
            print("Invalid member id or ISBN ")
            return
        member=self.members[member_id]
        book=self.books[isbn]

        if not book._is_available():
            print("Already Borrowed")
            return
        else:
            book._available= False
            member.borrowed_books.append(isbn)
            print("Book Borrowed Successfully!")

    def return_book(self):
        isbn=input("Enter book ISBN : ")
        memebr_id=input("Enter member id : ")

        if isbn not in self.books and memebr_id not in self.members:
            print("This Book wasn't borrowed by this member.")
            return 
        
        member=self.members[memebr_id]
        book=self.books[isbn]

        book._available=True
        member.borrowed_books.remove(isbn)
        print("Book Returned Successfully!")
# A menu to display
    def  menu(self):
        """
            Displays the main menu of the Library Management System
            and handles user interaction based on selected options.
        """
        while True:
            print("########## Library Management System ##########")
            print("1. Add new Member : ")
            print("2. Add new Book : ")
            print("3. Borrow Book : ")
            print("4. Return Book : ")
            print("5. View Members : ")
            print("6. View Books : ")
            print("7. Exit : ")
            
            choice =int(input("Enter Your choice : "))
            match choice:
                case 1:
                    self.add_member()
                case 2:   
                    self.add_book()
                case 3:
                    self.borrow_book()
                case 4:   
                    self.return_book()
                case 5:
                    self.view_member()
                case 6:
                    self.view_books()
                case 7:
                    print("Exiting System...")
                    break
                case _:
                    print("Invalid Input ")
            # if choice==1:
            #     self.add_member()
            # elif choice==2:
            #     self.add_book()
            # elif choice==3:
            #     self.borrow_book()
            # elif choice==4:
            #     self.return_book()
            # elif choice==5:
            #     self.view_member()
            # elif choice==6:
            #     self.view_books()
            # elif choice==7:
            #     print("Exiting System...")
            #     break
            # else:
            #     print("Invalid Input ")


# Library object calling menu function
library_obj=Library()
library_obj.menu()
help(Library.menu)
# print(Library.menu.__doc__)