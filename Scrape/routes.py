from flask import render_template, request, url_for, redirect
from Scrape.scrape import genereWise
from Scrape import app


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/genre")
def search():
    genre_name = request.args.get('genre')
    print(genre_name)
    return redirect(url_for("home", genre=genre_name))


@app.route("/genre_name=/<genre>")
def home(genre):
    movies = genereWise(genre)
    movies=[x for x in movies.split("%%")]
    return render_template('diplay_movie.html',a=movies[0],b=movies[1],c=movies[2],d=movies[3],e=movies[4])
