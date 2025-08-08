from models import Posts, session


def show_my_posts(current_user):
    posts_list = current_user.posts

    for post in posts_list:
        print(f"\n------------ Post {post.id} -------------")
        print(post.img)
        print(post.id)
        print(post.caption)
        print(post.location)
        print(post.created_at)


def create_post(current_user):

    img = input("Img URL: ")
    caption = input("Caption: ")
    location = input("Location: ")

    new_post = Posts(img=img, caption=caption, location=location, user_id=current_user.id) #Creating new Posts object
    session.add(new_post)
    session.commit()
    print("Post successfully created")


def update_post(current_user):
    show_my_posts(current_user) #Shows my posts as a menu to choose from

    choice = int(input("Select a post by Post Id: ")) #Converting the id to an int
    post_to_update = session.query(Posts).where(Posts.id == choice).first()

    if post_to_update and post_to_update.user_id == current_user.id:
        print(f"\n------------ Post {post_to_update.id} -------------")
        print(post_to_update.img)
        print(post_to_update.id)
        print(post_to_update.caption)
        print(post_to_update.location)
        print(post_to_update.created_at)
        print("Make your changes, and leave any values you wish to keep blank.")
        img = input("Img URL: ")
        caption = input("Caption: ")
        location = input("Location: ")
        if img: #Checking to see if they gave us a value for img
            post_to_update.img = img #if so update the post's img value
        if caption:
            post_to_update.caption = caption
        if location:
            post_to_update.location = location

        session.commit() #Need to make sure you commit your db.
        print(f"\n------------ Post {post_to_update.id} Updates -------------")
        print(post_to_update.img)
        print(post_to_update.id)
        print(post_to_update.caption)
        print(post_to_update.location)
        print(post_to_update.created_at)
    else:
        print("Invalid Choice")

def delete_post(current_user):
    show_my_posts(current_user) #Shows my posts as a menu to choose from

    choice = int(input("Select a post by Post Id: ")) #Converting the id to an int
    post_to_delete = session.query(Posts).where(Posts.id == choice).first()

    if post_to_delete and post_to_delete.user_id == current_user.id:
        session.delete(post_to_delete)
        session.commit()
        print(f'Successfully deleted post {choice}')
    else:
        print("Invalid choice.")



