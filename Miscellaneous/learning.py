password = ''

while password != 'Python123':
    password = input("Enter your password: ")
    if password == "Python123":
        print("You are logged in!")
    else:
        print("Sorry, try again")