book_list = []
choise_list = ("1","2","3","4","5")

def list():
    print("fdgn") 
def search():
    print("123")
def register():
    print("567")
def delete():
    print("1020")

while True:
    imput1 = ""
    while not imput1 in choise_list:
        imput1 = input("choose one : ")

    if imput1 == "1":
        list()
    elif imput1 == "2":
        search()
    elif imput1 == "3":
        register()
    elif imput1 == "4":
        delete()
    elif imput1 == "5":
        break
