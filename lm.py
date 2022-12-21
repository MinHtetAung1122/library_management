books = ["programming","data_scientist","analyst","dataE"]
cmd_list = ("list","search","register","delete","quit")

def list():
    if books == 0:
        print("there is no book")
    else:
        print("list of books")
        for book in books:
            print(f"({books.index(book) + 1 }) {book}")

def search():
    search_keywords = input("make a search : ")
    for book in books:
        if search_keywords in book:
            print(f"({books.index(book) + 1 } )  {book}")

def register():
    
    while True:
        
        new_book = input("add a book : ")
        if new_book in books:
            print("this book is already saved")
        else:
            books.append(new_book)
            if new_book == "quit":
                books.pop()
                break

def delete():
    book_num = int(input("book num u  want to del : "))
    sure = input(f"r u sure del to this {books[book_num - 1 ]} : (Y or N) : ").lower()

    if sure == "y":
        books.pop(book_num - 1)

while True:

    cmd = ""
    while not cmd in cmd_list :
        cmd = input("choose one : ")

    if cmd == "list":
        list()
    elif cmd =="search":
        search()
    elif cmd == "register":
        register()
    elif cmd == "delete":
        delete()
    elif cmd == "quit":
        break
