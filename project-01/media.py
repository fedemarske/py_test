class Movie(object):
	"""docstring for Movie"""

	#INIT
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, wiki_url):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.wiki_url = wiki_url