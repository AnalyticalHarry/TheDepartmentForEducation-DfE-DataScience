#importing Libraries
import sqlite3 as sql
#defining book store 
def book_store():
    # Connect to the database or create it if it doesn't exist
    db = sql.connect('bookstore.db')
    cursor = db.cursor()
    
    # Create the table with an auto-incrementing primary key
    cursor.execute('''CREATE TABLE IF NOT EXISTS bookstore (ID INTEGER PRIMARY KEY, Title TEXT, Author TEXT, QTY INTEGER)''')
    
    # Set the starting value of the auto-incrementing primary key
    # Check if the table was created
    cursor.execute("SELECT name from sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    if ('bookstore',) in tables:
        print("Table 'bookstore' created successfully.")
    else:
        print("Error creating table 'bookstore'.") 
        
    while True:
        #printing result on screen
        print('''
                add    - Add book
                update - Update book
                delete - Delete book
                search - Search book
                read   - Read all information in table
                exit   - Exit
             ''')
        #Reopen the connection to the database
        cursor = db.cursor()
        user_input = str(input().lower())
        
        #user input add
        if user_input == 'add':
            #book title
            title = input("Enter book title: ")
            #author title
            author = input("Enter book author: ")
            #quantity
            qty = int(input("Enter book quantity: "))
            #executing sql command
            cursor.execute("INSERT INTO bookstore(Title, Author, QTY) VALUES (?,?,?)", (title, author, qty))
            db.commit()
            #printing on screen
            print("Book added to the bookstore.")
        #user input update
        elif user_input == 'update':
            #old title of book to update
            title = input("Enter book title to update: ")
            #new title of book
            new_title = input("Enter new book title: ")
            #new author of book
            new_author = input("Enter new book author: ")
            #new qyantity 
            new_qty = int(input("Enter new book quantity: "))
            #executing sql command
            cursor.execute("UPDATE bookstore SET Title=?, Author=?, QTY=? WHERE Title=?", (new_title, new_author, new_qty, title))
            db.commit()
            #pirinting result
            print("Book updated in the bookstore.")
        #user input delete
        elif user_input == 'delete':
            #title of book
            title = input("Enter book title to delete: ")
            #quantity of book
            qty = int(input("Enter book Qty"))
            #executing sql command
            cursor.execute("DELETE FROM bookstore WHERE Title=? AND QTY=?", (title, qty))
            db.commit()
            print("Book deleted from the bookstore.")
    
        #user input search
        elif user_input == 'search':
            #title of book to search
            title = input("Enter book title to search: ")
            #executing sql command
            cursor.execute("SELECT * FROM bookstore WHERE Title=?", (title,))
            book = cursor.fetchone()
            #printing result on screen if book match
            if book:
                print("Title: ", book[1])
                print("Author: ", book[2])
                print("Quantity: ", book[3])
            #printing result on screen if book do not match
            else:
                print("Book not found in the bookstore.")
        #user input read or print all book on screen
        elif user_input == 'read':
            books = cursor.fetchall()
            #executing sql command
            cursor.execute('''SELECT id, Title, Author, Qty FROM bookstore''')
            #printing result on screen
            print('Printing Tables from database')
            result = cursor.fetchall()
            #for loop for iterating into data table and print them on screen
            for row in result:
                print(row)
        #user input exit
        elif user_input == 'exit':
            print("Exiting program.")
            #break while loop
            break
        #print if input key is wrong
        else:
            print("Invalid input. Try again.")
        
    #closing database    
    db.close()       

book_store()