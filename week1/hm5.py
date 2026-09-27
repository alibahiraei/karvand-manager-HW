my_book={}
while True:
    menu=input("enter work you\nadd\nsearch\nshow\nexit\n: ")
    if menu=="add":
        book=input("enter name boook: ")
        ather=input("enter name ather: ")
        my_book[book]=ather
    if menu=="search":
        my_search=input("enter name book: ")
        if my_search in my_book:
            print(f"ather is: {my_book[my_search]}")
        else:
            print("not found")
    if menu=="show":
        for i , j in my_book.items():
            print(f"name book: {i}  name ather:{j}")
    if menu=="exit":
        break