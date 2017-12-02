from flask import render_template, request, redirect, url_for
from . import controllers as controller
from .forms import *
from application import app
from application import CONFIG
from .models import *
import tmdbsimple as tmdb


d = tmdb.Discover()
s = tmdb.Search()

@app.route("/", methods = ["GET", "POST"])
def index():
	form = MovieForm(request.form)

	if request.method == 'POST' and form.validate():
		actors = form.actors.data.split(',')
		keywords = form.keywords.data.split(',')
		directors = form.directors.data.split(',')
		genres = form.genres.data
		year = form.year.data

		if (year == None):
			year = 0

		actorList = controller.getIds(actors, s.person)
		keywordList = controller.getIds(keywords, s.keyword)
		directorList = controller.getIds(directors, s.person)
		keywords = '|'.join(map(str, keywordList)) 
		actors = '|'.join(map(str, actorList))
		directors= '|'.join(map(str, directorList)) 
		genres= ','.join(map(str, genres)) 
		
		
		return redirect(url_for('search_results', page=1, genres=genres, keywords=keywords, actors=actors, year=year, directors=directors))
	return render_template('index.html', form=form)


@app.route('/search_results/<page>', methods = ["GET", "POST"])
def search_results(page):
	results = []

	discover = d.movie(page=page,with_genres=request.args['genres'],with_keywords=request.args['keywords'],with_cast=request.args['actors'],primary_release_year=request.args['year'],with_people=request.args['directors'])

	for movie in discover['results']:
		results.append(Movie(movie['id'], movie['title'],movie['poster_path'], movie['overview'], movie['release_date'], movie['original_language'],movie['genre_ids']))
	
	# from discover:
		# movie['id']
		# movie['title']
		# poster = "https://image.tmdb.org/t/p/original" + movie['poster_path']
	
	return render_template("search.html", discover=discover, results=results)




