from datetime import datetime
from extensions import db
import bcrypt


class Users(db.Model):
	__tablename__ = "Users"


	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String(30), unique=True, nullable=False)
	email = db.Column(db.String(130), unique=True, nullable=False)
	about_me = db.Column(db.Text)
	password_hash = db.Column(db.String(200), nullable=False)
	avatar = db.Column(db.String(255), nullable=False)
	phone = db.Column(db.String(13))
	last_acess = db.Column(db.DateTime, default=datetime.utcnow)
	registration_date = db.Column(db.DateTime, default=datetime.utcnow)
	count_logins = db.Column(db.Integer)
	device_ip_register = db.Column(db.String(15), nullable=False)
	posts = db.relationship('Kindness', backref='author', lazy='dynamic')


	def __init__(self, username, email, pass_hash, avatar):
		self.username = username
		self.email = email
		self.password_hash = pass_hash
		self.avatar = avatar
	

	def save(self):
		db.session.add(self)
		db.session.commit()
	

	def encrypt_pass(self, password):
		return bcrypt.hashpw(password, bcrypt.gensalt(9))


	def check_pass(self, password, pass_hash):
		return bcrypt.checkpw(password, pass_hash)


	def __repr__(self):
		return '<User {}>'.format(self.username)
	

	def to_json(self):
		return {
			"idUser": self.id,
			"username": self.username,
			"email": self.email,
			"about_me": self.about_me,
			"avatar": self.avatar,
			"phone": self.phone,
			"posts": self.posts,
			"lastAcess": self.last_acess
		}


kindness_tags_association = db.Table('Kindness_Tags', 
	db.Column('id_kindness', db.Integer, db.ForeignKey('Kindness.id_kindness')),
	db.Column('id_tag', db.Integer, db.ForeignKey('Tags.id'))
)


class Kindness(db.Model):
	__tablename__ = "Kindness"

	id_kindness = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.String(50))
	body = db.Column(db.Text)
	latitude = db.Column(db.Float)
	longitude = db.Column(db.Float)
	post_date = db.Column(db.DateTime, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
	tags = db.relationship("Tags", secondary=kindness_tags_association)


	def __repr__(self):
		return '<Kindness {}>'.format(self.title)
	

	def save(self):
		db.session.add(self)
		db.session.commit()


	def get_all(self):
		return self.query.all()
	

	def get_post_by_id(self):
		return self.query.filter_by_id(id=self.id_kindness).first()

		
	def to_json(self):
		return {
			"idPost": self.id_kindness,
			"title": self.title,
			"body": self.body,
			"latitude": self.latitude,
			"longitude": self.longitude,
			"postDate": self.post_date,
			"userId": self.user_id,
			"tagId": self.tag_id
		}


class Tags(db.Model):
	__tablename__ = "Tags"


	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	description = db.Column(db.String(20), nullable=False, unique=True)
	marker = db.Column(db.String(100), nullable=False, unique=True)
	#Visao de alto nivel para simplicar consultas ao DB. Esse campo
	#nao e adicionado ao banco.
	posts = db.relationship('Post', backref='post', lazy='dynamic')

	def __repr__(self):
		return '<Tags {}>'.format(self.description)
	

	def get_all(self):
		return self.query.all()

	
	def to_json(self):
		return {
			"idTag": self.id,
			"description": self.description,
			"marker": self.marker
		}


class Likes(db.Model):
	__tablename__ = "Likes"


	id_like = db.Column(db.Integer, primary_key=True, autoincrement=True)
	date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
	id_user = db.Column(db.Integer, db.ForeignKey('Users.id'))
	id_kindness = db.Column(db.Integer, db.ForeignKey('Kindness.id_kindness'))


class Kindness_Files(db.Model):
	__tablename__ = "Kindness_Files"


	id_kindness_file = db.Column(db.Integer, primary_key=True, autoincrement=True)
	file_extension = db.Column(db.String(6), nullable=False)
	file_size = db.Column(db.Float, nullable=False)
	#depois olhar como vai ser guardado esse caminho para diminuir ou aumentar
	#o tamanho da coluna.
	file_path = db.Column(db.String(200), nullable=False)
	date_upload = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
	id_kindness = db.Column(db.Integer, db.ForeignKey('Kindness.id_kindness'))


	def save_file(self):
		pass


class Tokens_Reset_Password(db.Model):
	__tablename__ = "Tokens_Reset_Password"


	id_token = db.Column(db.Integer, primary_key=True, autoincrement=True)
	token = db.Column(db.String(200), unique=True, nullable=False)
	send_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
	id_user = db.Column(db.Integer, db.ForeignKey('Users.id'))


	def generate_token(self):
		pass