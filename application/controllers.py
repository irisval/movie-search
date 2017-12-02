from application import app
from application import CONFIG
import tmdbsimple as tmdb
tmdb.API_KEY = CONFIG['TMDB_KEY']
from . forms import *


def getIds(paramList, param):
	ids = []
	for field in paramList:
		if (len(field) > 0):
			for x in param(query=field)['results']:
				ids.append(x['id'])
	return ids

