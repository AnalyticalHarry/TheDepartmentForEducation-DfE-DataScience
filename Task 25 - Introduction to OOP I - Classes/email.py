class Email:
    
    #Constructor to initialize variables
    def __init__(self, email_contents, from_address):
        self.email_contents = email_contents
        self.from_address = from_address
        self.is_spam = False
        self.has_been_read = False

    #creating a function marked_as_read
    def mark_as_read(self):
        #assigning email has been read to true
        self.has_been_read = True
    
    #creating a function is_spam
    def mark_as_spam(self):
        #assigning email is spam to True
        self.is_spam = True

        
#inbox to store all emails  
inbox = []

#defininf function add_email
#method to add email with message
def add_email(contents, email_address):
    email = Email(contents, email_address)
    inbox.append(email)
    
#defining function get_count
#method to count of emails in inbox    
def get_count():
    return len(inbox)

#defining function get_email
#returns the contents of an email list
def get_email(i):
    if 0 <= i <len(inbox):
        email = inbox[i]
        email.mark_as_read()
        print(email)
        return email
    else:
        print("Email doesn't exist")
        
#defining function get_unread_emails
#return a list of all the email that haven't been read
def get_unread_emails():
    unread_email_list = []
    for i in inbox:
        if not i.has_been_read:
            unread_email_list.append(i)
    return unread_email_list

#defining function get_spam_emails
#return a list of all the emails that have been marked as spam
def get_spam_emails():
    spam_list = []
    for i in inbox:
        if i.is_spam:
            spam_list.append(i)
            print(f"Spam emails: {i.email_contents}")
    return spam_list

#defining function add_spam
#method for indexing email as spam
def add_spam(i):
    messages = inbox[i]
    messages.mark_as_spam()
    print("Email added to spam")


#defining function delete
#deletes the mail from inbox
def delete():
    if len(inbox)>0:
        return inbox.pop()
    else:
        print("Could not delete email")
        
#previous mail
previous_emails = [
'Hello Invest into our bitcoin, bitcoinhero@yahoo.com',
'Hi How you doing? You have won 10million dollars, luckdip@yahoo.com',
"Hello Harry James here and would like to hear more about pervious movie, jamesbond007@gmail.com"
]

#creating for loop to interate inside previous mail
for i in previous_emails:
    #spliting contents and email address
    contents, email_address = i.split(',')
    #calling fucntion
    add_email(contents, email_address)
    
    
#An Email Simulation
#declaring user choice
user_choice = ""

#using while loop for user input
while user_choice != "quit":
    #asking user for input read/mark spam/send/quit
    user_choice = input("What would you like to do - read/mark spam/send/quit?: ")
    
    #reading mail
    if user_choice == "read":  
        #printing list of unread email
        print("Unread mail in inbox\n")
        #printing output with index and email
        for i, email in enumerate(previous_emails):
            print(f'{i + 1}. {email}')
        #asking for index number to read email
        numbers = int(input("\nEnter the index number of email to read: "))
        #calling function 
        get_email(numbers - 1)
        
    #mark spam
    elif user_choice == "mark spam": 
        #printing list of email in screen from inbox
        print("List of emails in box: \n")
        #printing output with index and email
        for i, email in enumerate(previous_emails):
            print(f'{i + 1}. {email}')
        #asking for index number to mark spam
        numbers = int(input("\nEnter the index number of email to mark spam: "))
        #calling function
        add_spam(numbers - 1)
        get_spam_emails()
    #send mail
    elif user_choice == "send": 
        #user will enter email address
        from_address = input("Enter your email address: ")
        #user will enter message
        email_contents = input("Enter your content: ")
        #calling fucntion 
        add_email(email_contents, from_address)
        print("Email sent successfully!")
    #quit
    elif user_choice == "quit": 
        #priting reesult "Goodbye"
        print("Goodbye")
        #incorrect input from user will print "Oops - incorrect input" on screen
    else:
        print("Oops - incorrect input")