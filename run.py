#!/usr/bin/env python3.6
from user import User
from credential import Credential

def create_user(user_name,password):
    """
    Function to create a new users
    """
    new_user= User(user_name,password)
    return new_user

def save_user(user):
    """
    Function to save contact
    """
    user.save_user()



def check_existing_users(user_name):
    """
    Functionto to check if an user exists using the user _name
    """
    return User.user_exist(user_name)

def add_credential(account_type,user_name,password):
    """
    Function to add credential
    """
    new_credential=Credential(account_type,user_name,password)
    return new_credential

def save_credentials(credential):
    """
    Function to save credentials
    """
    credential.save_credential()

def display_credentials():
    """
    Function that returns all the saved contacts
    """
    return Credential.display_credentials()

def main():
    print("To access the password locker account please input your user name")
    user_name=input()
    print("Enter your password")
    password=input()
    print("Welcome,Please use these short codes to navigate: ac - add credentials, dc - display credentials, ex - exit the application")
    short_code = input().lower()
    if short_code == 'ac':
        print("Add credentials")
        print("-"*10)
        print("Account type...")
        account_type=input()
        print("User name")
        user_name=input()
        print("Password")
        password=input()

        save_credentials(add_credential(account_type,user_name,password))
        print('\n')
        print(f"Credentials for {account_type} added")
        print('\n')
    elif short_code == 'dc':
        if display_credentials():
            print("Here is a list of your credentials")
            print('\n')

            for contact in display_credentials():
                print(f"{credential.account_type}..{credential.user_name} ..{credential.password}")
                print('\n')
            else:
                print('\n')
                print("You don't have credentials saved yet")
            # elif short_code =='fc':

        elif short_code == 'ex':
            print("Exiting the password locker")
            # break
        # else:
        #     print("Please use the short codes provided")




if __name__ == '__main__':

    main()
