from models import Users, session


def show_profile(current_user):
    """passing in the current_user object
    display their profile"""

    print(f"--- {current_user.username} ---")
    print(f"Email: {current_user.email}")
    print(f"Password: {current_user.password}")
    print(f"Bio: {current_user.bio}")

def update_profile(current_user):
    show_profile(current_user)
    print("Make your changes, leave blank if you want to keep current value")
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")
    bio = input("bio: ")

    if username:
        current_user.username = username
    if password:
        current_user.password = password
    if email:
        current_user.email = email
    if bio:
        current_user.bio = bio

    session.commit()
    print("Here are your new changes:")
    show_profile(current_user)
    return current_user

def delete_user(current_user):
    choice = input("Type 'delete' to confirm you wish to delete your account: ")
    if choice == 'delete':
        session.delete(current_user)
        session.commit()
        print("Successfully deleted account.")
        return True
    else:
        return False
