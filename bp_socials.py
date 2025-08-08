from models import Users, Posts, session


def like_post(current_user):
    all_posts = session.query(Posts).all()

    for post in all_posts:
        print(f"\n------------ Post {post.id} -------------")
        print(post.img)
        print(post.id)
        print(post.caption)
        print(post.location)
        print(post.created_at)

    choice = input("choose a post to like by Post id: ")
    post_to_like = session.get(Posts, choice) #Query the particuler post
    if post_to_like not in current_user.liked_posts:
        current_user.liked_posts.append(post_to_like) #Appending a post to this relationship attribute, creates a relationship from user to post
        session.commit()
        print(f"{current_user.username} Liked Post {post_to_like.id}")
    else:
        print("Failed to like post")



def unlike_post(current_user):
    liked_posts = current_user.liked_posts

    for post in liked_posts:
        print(f"\n------------ Post {post.id} -------------")
        print(post.img)
        print(post.id)
        print(post.caption)
        print(post.location)
        print(post.created_at)

    choice = input("choose a post to unlike by Post id: ")
    post_to_unlike = session.get(Posts, choice) #Query the particuler post
    if post_to_unlike in current_user.liked_posts:
        current_user.liked_posts.remove(post_to_unlike) #Removing this post from my users liked_posts list
        session.commit()
        print(f"{current_user.username} unliked Post {post_to_unlike.id}")
    else:
        print("Failed to unlike post")


def view_liked_posts(current_user):
    liked_posts = current_user.liked_posts

    print("\n----------- MY LIKED POSTS --------------")
    for post in liked_posts:
        print(f"\n------------ Post {post.id} -------------")
        print(post.img)
        print(post.id)
        print(post.caption)
        print(post.location)
        print(post.created_at)
