from wtforms import Form, StringField, SelectMultipleField, BooleanField, SubmitField, IntegerField, validators
import tmdbsimple as tmdb


g = tmdb.Genres().list()

class MovieForm(Form):
	# movie = StringField('Movie Title', [validators.Optional()])
	actors = StringField('Actor(s):', [validators.Optional()])
	keywords = StringField('Keywords:', [validators.Optional()])
	directors = StringField('Directors:', [validators.Optional()])
	year = IntegerField('Release Year:', [validators.Optional()])
	genres = SelectMultipleField('Genres:', [validators.Optional()], coerce=int, choices=[(i['id'], i['name']) for i in g['genres']])
	# language = SelectMultipleField('Language:', [validators.Optional()], choices=[(i['name'], i['id']) for i in g['genres']])
	submit = SubmitField('Submit')
