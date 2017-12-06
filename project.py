
import os
from flask import Flask, session, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '3028876288'

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    description = db.Column(db.Text)

class Course(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer, primary_key=True)
    actor_name = db.Column(db.String(256))
    age = db.Column(db.Integer)
     = db.Column(db.Text)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movies')
def get_all_movies():
    movies =[
    'The Lion King',
    'Mulan',
    'Moana',
    'Frozen',
    'Cinderella'
    ]
    return render_template('movies.html', movies = movies)

@app.route('/members')
def members_page():
    return render_template('members.html')


if __name__ == '__main__':
    app.run(debug=True)
