import re
first_name = input("please enter your first name: ")
last_name = input("please enter your last name: ")
email = input("please input a valid email address")
password = input("please enter your password: ")

# Task 1: input length validatior
# First name
if len(first_name) <= 2:
    print("please enter a valid first name with at least 3 characters")
else:
    print(first_name)
#Last name
if len(last_name) <= 2:
    print("please enter a valid last name with at least 3 characters")
else: 
    print(last_name)

# Task 2: password complexity checker
def check_password(passowrd):
    # length
    if len(password) < 8:
        print("password must be at least 8 characters long")
        return False
    # Upper Case
    if not re.search(r'[A-Z]', password):
        print("password must contain at least one uppercase letter")
        return False
    # Lower Case
    if not re.search(r'[a-z]', password):
        print("Password must contain at least one lowercase letter.")
        return False
    # Number
    if not re.search(r'\d', password):
        print("Password must contain at least one number.")
        return False
    return True

# Task 3: Email Formatter
def standardize_email(email):
    email = email.lower()
    email = re.sub(r'\s+','',email)
    return email

standard_email = standardize_email(email)

print(standard_email)

if check_password(password):
    print("Password meets complexity requirements.")
else:
    print("Password does not meet complexity requirements.")