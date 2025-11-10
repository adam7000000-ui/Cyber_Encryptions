def login():
    correct_username = "cyber1234"
    correct_password = "7946"

    print("=== Welcome to the Login System ===")

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == correct_username and password == correct_password:
        print("Login successful. Welcome, Cyber!")
        return True
    else:
        print("Incorrect username or password. Access denied.")
    return False