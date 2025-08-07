from sqlalchemy import Column, Float, create_engine, Integer, String, ForeignKey, DateTime, Table, null
from sqlalchemy.orm import relationship, Mapped, mapped_column, declarative_base, sessionmaker
from datetime import datetime

Base = declarative_base()

engine = create_engine('sqlite:///socials.db')

following = Table(
    'following',
    Base.metadata,
    Column('follower_id', Integer, ForeignKey('users.id')),
    Column('followed_id', Integer, ForeignKey('users.id'))
)

likes = Table(
    'likes',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('post_id', Integer, ForeignKey('posts.id'))
)


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(80), nullable=False, unique=True)
    bio: Mapped[str] = mapped_column(String(500), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    email: Mapped[str] = mapped_column(String(360), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(100), nullable=False)

    posts: Mapped[list['Posts']] = relationship('Posts', back_populates='user')
    liked_post: Mapped[list['Posts']] = relationship('Posts', secondary=likes, back_populates='liked_by')
                                                    
                                                    
                                                    
    following: Mapped[list['Users']] = relationship(
        'Users', 
        secondary="following", 
        primaryjoin="Users.id==following.c.follower_id",
        secondaryjoin="Users.id==following.c.followed_id",
        backref='followed_by')
    


class Posts(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True) #auto increment
    img: Mapped[str] = mapped_column(String(250), nullable=False)
    caption: Mapped[str] = mapped_column(String(225), nullable=True)
    location: Mapped[float] = mapped_column(Float, nullable=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False) #FK's need the table name they are pointing to, and the field
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    user: Mapped['Users'] = relationship('Users', back_populates='posts')
    liked_by: Mapped[list['Users']] = relationship('Users', secondary=likes )

#Build db
Base.metadata.create_all(bind=engine)


#==================================================== Creating Data =====================================================

#create database session
Session = sessionmaker(engine) #Creates a Session class
session = Session() #Creating an instance of the Session class

#Creating a new_user and adding them to the db
# new_user = Users(username='dylank', bio='Just a guy', email='dk@email.com', password='123')
# session.add(new_user) #Adds it to the session
# session.commit()

#Creating a new_post for the user in my db.
# new_post = Posts(img='https://i1.sndcdn.com/artworks-LiehzC8qIN6z1pFa-iGq9Fg-t1080x1080.jpg', caption='Just a chill guy', user_id=1)
# session.add(new_post)
# session.commit()

new_users = [
    Users(username= 'joeyv', bio = 'hi', email ='jv@email.com', password ='123'),
    Users(username='arnett', bio='Just a chill guy navigating the code jungle. Former chef, future engineer.', email='arnett@example.com', password='s3cr3t'),
    Users(username= 'niknak', bio = 'helo', email ='niknak@email.com', password ='abc123'),
    Users(username='Leo duley',bio='Lab rat', email='leoduley@email.com', password = '1234567' ),
    Users(username='Mashal_Mathers', bio='The real slim Shady', email='eminem@shady.com', password='password123'),
    Users(username="thuchain", bio="hello world", email="thu@email.com", password="2222"),
    Users(username ="gotcurds", bio = "cheese is life nuff said", email = "nachocheese@queso.brie", password= "nicetrybigguy"),
    Users(username= 'Daniel_O', bio= 'software development is cool', email= 'danieltravels033@gmail.com', password='123acb'),
    Users(username='sharogers', bio='hello', email='sharogers@email.com', password='1234'),
    Users(username='Spuck', bio= 'Wassup', email='spuck@email.com', password='8692' ),
    Users(username='RayKay', bio='guy in OK', email='rayk@email.com', password='4567'),
    Users(username='chrisrod', bio='Hello', email='crodriguezaerc@gmail.com', password='12345')

]



