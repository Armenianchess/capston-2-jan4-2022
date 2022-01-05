"""SQLAlchemy models for Warbler."""

from datetime import datetime

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()


class Follows(db.Model):
    """Connection of a follower <-> followed_user."""

    __tablename__ = 'follows'

    user_being_followed_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete="cascade"),
        primary_key=True,
    )

    user_following_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete="cascade"),
        primary_key=True,
    )


class Likes(db.Model):
    """Mapping user likes to warbles."""

    __tablename__ = 'likes' 

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='cascade')
    )

    message_id = db.Column(
        db.Integer,
        db.ForeignKey('messages.id', ondelete='cascade')
    )



class User(db.Model):
    """User in the system."""

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    email = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    username = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    image_url = db.Column(
        db.Text,
        default="/static/images/default-pic.png",
    )

    header_image_url = db.Column(
        db.Text,
        default="data:image/jpeg;base64,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"
    )

    bio = db.Column(
        db.Text,
    )

    location = db.Column(
        db.Text,
    )

    password = db.Column(
        db.Text,
        nullable=False,
    )

    messages = db.relationship('Message')

    followers = db.relationship(
        "User",
        secondary="follows",
        primaryjoin=(Follows.user_being_followed_id == id),
        secondaryjoin=(Follows.user_following_id == id)
    )

    following = db.relationship(
        "User",
        secondary="follows",
        primaryjoin=(Follows.user_following_id == id),
        secondaryjoin=(Follows.user_being_followed_id == id)
    )

    likes = db.relationship(
        'Message',
        secondary="likes"
    )

    def __repr__(self):
        return f"<User #{self.id}: {self.username}, {self.email}>"

    def is_followed_by(self, other_user):
        """Is this user followed by `other_user`?"""

        found_user_list = [user for user in self.followers if user == other_user]
        return len(found_user_list) == 1

    def is_following(self, other_user):
        """Is this user following `other_use`?"""

        found_user_list = [user for user in self.following if user == other_user]
        return len(found_user_list) == 1

    @classmethod
    def signup(cls, username, email, password, image_url):
        """Sign up user.

        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            username=username,
            email=email,
            password=hashed_pwd,
            image_url=image_url,
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password`.

        This is a class method (call it on the class, not an individual user.)
        It searches for a user whose password hash matches this password
        and, if it finds such a user, returns that user object.

        If can't find matching user (or if password is wrong), returns False.
        """

        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user

        return False


class Message(db.Model):
    """An individual message ("warble")."""

    __tablename__ = 'messages'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    text = db.Column(
        db.String(140),
        nullable=False,
    )

    timestamp = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow(),
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
    )

    user = db.relationship('User')


class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
    )

    message_id = db.Column(
    db.Integer,
    db.ForeignKey('messages.id', ondelete='cascade')
    )

    comment = db.Column(
        db.String,
        nullable=False
    )

class Certificate(db.Model):

    __tablename__ = 'certificate'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
    )

    certificate_link = db.Column(
        db.String,
        nullable=False
    )

    certificate_name = db.Column(
        db.String,
        nullable=False
    )

    
class Subject(db.Model):

    __tablename__ = 'subject'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
    )

    subject_name = db.Column(
        db.String,
        nullable=False
    )

class SchoolName(db.Model):

    __tablename__ = 'school_name'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
    )

    school_name = db.Column(
        db.String,
        nullable=False
    )



class Rating(db.Model):

    __tablename__ = 'rating'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
    )

    rating = db.Column(
        db.Integer,
        nullable=False
    )


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)
