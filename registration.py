from db import *

def registration():
    country_code = {
        "NGN": 234,
        "GHN": 233,
        "BEN": 229,
        "TOGO": 229
    }

    first_name = str(input("Enter your first name\n>> ")).upper()
    last_name = str(input("Enter your last name\n>> ")).upper()
    other_name = str(input("Enter your other name\n>> ")).upper()
    username = str(input("Enter your username\n>> "))
    email = str(input("Enter your email\n>> ")).lower()
    password1 = str(input("Enter your password\n>> "))
    password2 = str(input("Confirm the password\n>> "))
    c_code = str(input("Select your country code\n1. Nigera\n2. Ghana\n3. BENIN\n4. TOGO\n>> "))
    number = str(input("Enter your number \n>> "))
    if c_code == "1":
        cc = country_code["NGN"]
        phone_number = f'{cc}{number}' 
    elif c_code == "2":
        cc = country_code["GHN"]
        phone_number = f'{cc}{number}'
    elif c_code == "3":
        cc = country_code["BEN"]
        phone_number = f'{cc}{number}'
    elif c_code == "4":
        cc = country_code["TOGO"]
        phone_number = f'{cc}{number}'
    else:
        print("You are not allowed to open account with us from your counutry")
    address = str(input("Enter your address\n>> ")).upper()
    nin = int(input("Enter a valid NIN (NATIONAL IDENTITY NUMBER)\n>> "))
        
    if password1 == password2:
        print(create_user(
            first_name,
            last_name,
            other_name,
            username,
            email,
            password1,
            phone_number,
            number,
            address,
            nin
            ))
    return "User added"