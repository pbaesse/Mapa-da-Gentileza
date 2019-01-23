import datetime
from extensions import db
from flask_login import UserMixin
from dynaconf import settings
from flask import send_from_directory


class Users(UserMixin, db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(130), unique=True, nullable=False)
    about_me = db.Column(db.Text)
    status = db.Column(db.String(20))
    password_hash = db.Column(db.String(200), nullable=False)
    avatar = db.Column(db.String(255))
    phone = db.Column(db.String(13))
    last_access = db.Column(db.DateTime, default=datetime.datetime.now)
    registration_date = db.Column(db.DateTime, default=datetime.datetime.now)
    count_logins = db.Column(db.Integer)
    count_logins_failed = db.Column(db.Integer)
    date_last_login_failed = db.Column(db.DateTime, default=datetime.datetime.now)
    genre = db.Column(db.String(10), nullable=False)
    date_birth = db.Column(db.DateTime, nullable=False)
    confirmed = db.Column(db.Boolean, default=False)
    date_last_change_pass = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)
    device_ip_register = db.Column(db.String(15), nullable=False)
    posts = db.relationship('Kindness', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def to_json(self):
        return {
            "idUser": self.id,
            "username": self.username,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "genre": self.genre,
            "status": self.status,
            "dateBirth": self.date_birth,
            "email": self.email,
            "aboutMe": self.about_me,
            "avatar": self.avatar,
            "phone": self.phone,
            "lastAcess": self.last_access,
        }


kindness_tags_association = db.Table('Kindness_Tags',
                                     db.Column('id_kindness', db.Integer, db.ForeignKey(
                                         'Kindness.id_kindness'), primary_key=True),
                                     db.Column('id_tag', db.Integer, db.ForeignKey(
                                         'Tags.id'), primary_key=True)
                                     )


class Kindness(db.Model):
    __tablename__ = "Kindness"

    id_kindness = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    identifier = db.Column(db.String(40), unique=True, nullable=False)
    body = db.Column(db.Text, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    post_date = db.Column(db.DateTime, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    unnamed = db.Column(db.Boolean, default=False)
    files = db.relationship('Kindness_Files', backref='file', lazy=True)
    tags = db.relationship('Tags', secondary=kindness_tags_association,
                           lazy='subquery', backref=db.backref('kindness', lazy=True))

    def __repr__(self):
        return '<Kindness {}>'.format(self.title)

    def to_json(self):
        return {
            "idPost": self.identifier,
            "title": self.title,
            "body": self.body,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "postDate": self.post_date,
            "userId": self.user_id
        }


class Tags(db.Model):
    __tablename__ = "Tags"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(20), nullable=False, unique=True)
    path_file_marker = db.Column(db.String(100), nullable=False, unique=True)
    file_name_marker = db.Column(db.String(30), nullable=False, unique=True)
    # Visao de alto nivel para simplicar consultas ao DB. Esse campo
    # nao e adicionado ao banco.
    #posts = db.relationship('Kindness', backref='post', lazy='dynamic')

    def __repr__(self):
        return '<Tags {}>'.format(self.description)

    def get_all(self):
        return self.query.all()

    def to_json(self):
        return {
            "idTag": self.id,
            "description": self.description,
            "pathMarker": self.path_file_marker,
            "fileName": self.file_name_marker
        }


class Likes(db.Model):
    __tablename__ = "Likes"

    id_like = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('Users.id'))
    id_kindness = db.Column(db.Integer, db.ForeignKey('Kindness.id_kindness'))

    def to_json(self):
        return {
            "idLike": self.id_like,
            "dateLike": self.date,
            "idUser": self.id_user,
            "idKindness": self.id_kindness
        }


class Kindness_Files(db.Model):
    __tablename__ = "Kindness_Files"

    id_kindness_file = db.Column(
        db.Integer, primary_key=True, autoincrement=True)
    file_extension = db.Column(db.String(6), nullable=False)
    size = db.Column(db.LargeBinary())
    file_path = db.Column(db.String(70), nullable=False)
    date_upload = db.Column(
        db.DateTime, default=datetime.datetime.now, nullable=False)
    id_kindness = db.Column(db.Integer, db.ForeignKey('Kindness.id_kindness'))


class Tokens(db.Model):
    __tablename__ = "Tokens"

    id_token = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(200), unique=True, nullable=False)
    send_date = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)
    was_used = db.Column(db.Boolean, default=False)
    type_token = db.Column(db.String(15), nullable=False)
    is_valid = db.Column(db.Boolean, default=True, nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('Users.id'))
