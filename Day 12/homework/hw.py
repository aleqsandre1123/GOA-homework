
correct_password = "password123"

while True:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Correct password entered. Access granted.")
        break  
    else:
        print("Incorrect password. Try again.")
