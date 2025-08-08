from flask_migrate import current
from models import session
from bp_auth import register_user, login
from bp_users import show_profile, update_profile, delete_user





def welcome_menu():
    current_user = None
    while True:
        print("""
--------- Welcome to Finstagram --------
        1.) Login
        2.) Register
""")
        choice = input("select (1 or 2) or quit: ")
        if choice == '1':
            email= input("Email: ")
            password= input("Password: ")
            user_credentials = {
                "email": email,
                "password": password
            }
            user = login(user_credentials)
            if user:
                current_user = user
                return current_user

        elif choice == '2':
            username = input("Username: ")
            email = input("Email: ")
            password = input("Password: ")
            bio = input("option bio: ")
            user_data = {
                'username': username,
                'email': email,
                'password': password,
                'bio': bio
            }
            new_user = register_user(user_data)
            if new_user:
                current_user = new_user #automatically "logging them in" setting our current user to the new_users
                return current_user

        elif choice == 'quit':
            return
        else:
            print("Invalid response please try again.")

def user_menu(current_user):
    while True:
        print("""
    1.) View Profile
    2.) Update Profile
    3.) Delete Profile
    4.) Back""")
        choice = input("choose 1-3: ")
        if choice == '1':
            show_profile(current_user)
        elif choice == '2':
            current_user = update_profile(current_user)
        elif choice == '3':
            is_deleted = delete_user(current_user)
            if is_deleted:
                current_user = None
                main() #Recursivly calling my main function to restart the program from the begining
        elif choice == '4':
            return
        else:
            print("Invalid Selection.")

def posts_menu(current_user):
    while True:
        print("""
1.) View all of my Posts
2.) Create Post
3.) Update Post
4.) Delete Post
5.) Back""")
        choice = input("choose 1-5: ")
        if choice == '1':
            #View all of my posts
            pass
        elif choice == '2':
            #Create a post
            pass
        elif choice == '3':
            #Update a post
            pass
        elif choice == '4':
            #Delete a post
            pass
        elif choice == '5':
            return
        else:
            print("Invalid Selection.")



def main():
    
    current_user = welcome_menu()
    
    if current_user:
        while True:
            print("""
        --------- Finstagram --------
        1.) Manage Profile
        2.) My Posts
        3.) Social Features
        """)
            choice = input("choose 1-3: ")
            if choice == '1':
                user_menu(current_user)
            elif choice == '2':
                #show Posts menu
                pass
            elif choice == '3':
                #show Social Menu
                pass
            else:
                print("Invalid Selection.")
    

main()
    
