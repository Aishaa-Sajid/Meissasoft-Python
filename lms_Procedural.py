books={}
members={}

# isbn  989-001-1-001-001
# Add book function
def add_book():
    isbn=input("Enter ISBN : ")

    if isbn in books:
        print("This ISBN already exists")
        return
    title=input("Enter book title : ")
    author=input("Enter author name : ")

    books[isbn]={
        "title":title,
        "author":author,
        "availability":True
    }
    print("Book Added Successfully!")

# Add Member function
def add_member():
    member_id=input("Enter Member id : ")

    if member_id in members:
        print("This member id already exists.")
        return
    name=input("Enter Member name : ")

    members[member_id]={
        "name":name,
        "borrowed_books":[]
    }
    print("Member Added Successfully!")

# View members
def view_member():
    if not members:
        print("No Member Registered yet.")
        return
    
    for member_id,member in members.items():
        print(f"Name : {member["name"]} | Member_id : {member_id} \n Borrowed books : {member["borrowed_books"]}")

# View Books
def view_books():
    if not books:
        print("No Books available!")
        return 
    
    for isbn,book in books.items():
        if book["availability"]:
            status="Available"
        else:
            status="Borrowed"
        print(f"Title : {book["title"]} | Author : {book["author"]} | ISBN : {isbn} | {status}")

# Borrow books
def borrow_books():
    member_id=input("Enter member id : ")
    isbn=input("Enter ISBN : ")

    if member_id not in members or isbn not in books:
        print("Invalid book or member_id")
        return
    
    member=None
    book=None

    member=members[member_id]
    book=books[isbn]

    if book["availability"]==False :
        print("Book already borrowed.")
        return
    
    book["availability"]=False
    member["borrowed_books"].append(isbn)
    print("Book Borrowed successfully!")
    return

# return books
def return_books():
    member_id=input("Enter Member ID : ")
    isbn=input("Enter ISBN : ")

    if member_id not in members or isbn not in books:
        print("Invalid data ")
        return
    
    member=members[member_id]
    book=books[isbn]

    book["availability"]=True
    member["borrowed_books"].remove(isbn)
    print("Book Returned Successfully!")
    return
# Menu
def menu():
    while True:
        print("############## Library Management System ##############")
        print("1. Add new Books")
        print("2. Register new Member ")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Members ")
        print("6. View Books ")
        print("7. Exit ")

        choice=input("Enter your choice : ")
        if choice=="1":
            add_book()
        elif choice=="2":
            add_member()
        elif choice=="3":
            borrow_books()
        elif choice=="4":
            return_books()
        elif choice=="5":
            view_member()
        elif choice=="6":
            view_books()
        elif choice=="7":
            print("Exiting System")
            break

        else:
            print("Invalid Choice")

menu()
