from flask_migrate import current
from models import session, Users
from bp_auth import register_user, login
from bp_users import show_profile, update_profile, delete_user
from bp_posts import delete_post, show_my_posts, create_post, update_post
from bp_socials import like_post, unlike_post, view_liked_posts





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
            show_my_posts(current_user)
        elif choice == '2':
            create_post(current_user)
        elif choice == '3':
            update_post(current_user)
        elif choice == '4':
            delete_post(current_user)
        elif choice == '5':
            return
        else:
            print("Invalid Selection.")

def social_menu(current_user):
    while True:
        print("""
1.) Like Post
2.) Unlike Post
3.) View Liked Posts
4.) Follow User
5.) Unfollow User
""")
        choice = input("choose 1-6: ")
        if choice == '1':
            like_post(current_user)
        if choice == '2':
            unlike_post(current_user)
        if choice == '3':
            view_liked_posts(current_user)
        if choice == '4':
            pass
        if choice == '5':
            pass
        if choice == '6':
            pass



def main():
    
    # current_user = welcome_menu() Not going to log in everytime I want to test

    current_user = session.get(Users, 1) #Make the 1st user my current user skipping the loggin process
    
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
                posts_menu(current_user)
            elif choice == '3':
                social_menu(current_user)
            else:
                print("Invalid Selection.")
    

main()
    
