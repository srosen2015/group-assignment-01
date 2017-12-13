
import os
from flask import Flask, session, render_template, request, flash, redirect, url_for, jsonify
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
    year = db.Column(db.Integer)
    genre = db.Column(db.String(64))
    description = db.Column(db.String(256))
    actors = db.relationship('Actor', backref='movie', cascade="delete")

class Actor(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer, primary_key=True)
    actor_name = db.Column(db.String(256))
    age = db.Column(db.Integer)
    role = db.Column(db.String(64))
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movies')
def show_all_movies():
    movies = Movie.query.all()
    return render_template('movies-all.html', movies = movies)

@app.route('/movie/add', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'GET':
        return render_template('movie-add.html')
    if request.method == 'POST':
        # get data from the form
        title = request.form['title']
        year = request.form['year']
        genre = request.form['genre']
        description = request.form['description']
        # insert the data into the database
        movie = Movie(title=title, year=year, genre=genre, description=description)
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('show_all_movies'))

@app.route('/movie/edit/<int:id>', methods=['GET', 'POST'])
def edit_movie(id):
    movie = Movie.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('movie-edit.html', movie=movie)
    if request.method == 'POST':
        # update data based on the form data
        movie.title = request.form['title']
        movie.year = request.form['year']
        movie.genre = request.form['genre']
        movie.description = request.form['description']
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_movies'))

@app.route('/movie/delete/<int:id>', methods=['GET', 'POST'])
def delete_movie(id):
    movie = Movie.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('movie-delete.html', movie=movie)
    if request.method == 'POST':
        db.session.delete(movie)
        db.session.commit()
        return redirect(url_for('show_all_movies'))


@app.route('/api/movie/<int:id>', methods=['DELETE'])
def delete_ajax_movie(id):
    movie = Movie.query.get_or_404(id)
    db.session.delete(movie)
    db.session.commit()
    return jsonify({"id": str(movie.id), "name": movie.title})

@app.route('/actors')
def show_all_actors():
    actors = Actor.query.all()
    return render_template('actor-all.html', actors=actors)

@app.route('/actor-directory/add', methods=['GET', 'POST'])
def add_actors():
    if request.method == 'GET':
        movies = Movie.query.all()
        return render_template('actor-add.html', movies=movies)
    if request.method == 'POST':
        actor_name = request.form['name']
        age = request.form['age']
        role = request.form['role']
        movie_title = request.form['movie']
        movie = Movie.query.filter_by(title=movie_title).first()
        actor = Actor(actor_name=actor_name, age=age, movie=movie, role=role)
        db.session.add(actor)
        db.session.commit()
        return redirect(url_for('show_all_actors'))

@app.route('/actor-directory/edit/<int:id>', methods=['GET', 'POST'])
def edit_actor(id):
    actor = Actor.query.filter_by(id=id).first()
    if request.method == 'GET':
        movies = Movie.query.all()
        return render_template('actor-edit.html', actor=actor, movies=movies)
    if request.method == 'POST':
        actor.actor_name = request.form['name']
        actor.age = request.form['age']
        actor.role = request.form['role']
        movie_title = request.form['movie']
        movie = Movie.query.filter_by(title=movie_title).first()
        actor.movie = movie
        db.session.commit()
        return redirect(url_for('show_all_actors'))

@app.route('/actor-directory/delete/<int:id>', methods=['GET', 'POST'])
def delete_actor(id):
    actor = Actor.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('actor-delete.html', actor=actor)
    if request.method == 'POST':
        db.session.delete(actor)
        db.session.commit()
        return redirect(url_for('show_all_actors'))
    
    
   @app.route('/api/actor/<int:id>', methods=['DELETE'])
def delete_ajax_actor(id):
    actor =Actor.query.get_or_404(id)
    db.session.delete(actor)
    db.session.commit()
    return jsonify({"id": str(actor.id), "name": actor.actor_name})


@app.route('/members')
def members_page():
    return render_template('members.html')


if __name__ == '__main__':
    app.run(debug=True)
