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






