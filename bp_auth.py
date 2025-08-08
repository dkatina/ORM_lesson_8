from models import Users, session #Need the Users model to create and search for users
#need the sesssion to add users to our db


def register_user(user_data):
    """ this fucntion will recieve a dictionary called user_data
    and will create a Users object from this data and store the object to the db
    user_data = {
        usernam: str,
        bio: str,
        email: str,
        password: str

    returns new_user object on success 
    returns none on failure
    }"""

    try:
        new_user = Users(**user_data) #unpacks the dictionary directly into the Class to create a model
        session.add(new_user)
        session.commit()
        print("User successfully created")
        return new_user
    except Exception as e:
        print("An erro occured while trying to create the user")
        print(e)
        return None
    

def login(user_credentials):
    """Takes in a dictionary user_credentials
    Searches for a user using given email
    evaluates if that user's password is the same as the password given
    if so returns the user object
    else returns invalid login

    user_credentials = {
    email: str,
    password: str}"""

    try:
        user = session.query(Users).where(Users.email==user_credentials['email']).first() #Trying to find a user with this email
        if user and user.password == user_credentials['password']:
            print(f'Successfully logged in {user.username}')
            return user
        else:
            print("Invalid email or password")
            return None
    except Exception as e:
        print("An error occured while trying to log you in.")
        print(e)
        return None




