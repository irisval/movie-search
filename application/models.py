class Movie(object):
	def __init__(self, id, title, poster_path, overview, release_date, original_language, genre_ids):
		self.id = id
		self.title = title
		self.poster_path = poster_path
		self.bio = overview
		self.original_language = original_language
		self.release_date = release_date
		self.genre_ids = genre_ids

	def __repr__(self):
		return "%s: %d" % (self.title, self.id)

	# @property
	# def email(self):
	# 	return self.id + "d"

# id
# title

