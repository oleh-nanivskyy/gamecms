import enum

from flask_sqlalchemy import SQLAlchemy

from app import app

db = SQLAlchemy(app)


class Roles(enum.Enum):
    regular = 1
    admin = 2


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.Enum(Roles), nullable=False)

    reviews = db.relationship('Reviews', backref='users', lazy=True)


class Companies(db.Model):
    company_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(2000))
    foundation_date = db.Column(db.DateTime, nullable=False)
    ceo = db.Column(db.String(60))
    
    games = db.relationship('Games', backref='companies', lazy=True)


class Games(db.Model):
    game_id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.company_id'), 
                           nullable=False)
    name = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(2000))
    release_date = db.Column(db.DateTime, nullable=False)

    reviews = db.relationship('Reviews', backref='games', lazy=True)
    screenshots = db.relationship('Screenshots', backref='games', lazy=True)


class Reviews(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'), 
                           nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), 
                           nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)
    edit_date = db.Column(db.DateTime)

class Screenshots(db.Model):
    screenshot_id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'), 
                           nullable=False)
    file_name = db.Column(db.String(256), nullable=False)
    thumbnail_name = db.Column(db.String(256), nullable=False)