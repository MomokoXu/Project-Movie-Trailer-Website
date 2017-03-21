import webbrowser

class Movie():
	''' This class provides a way to store movie related information
	
	Attributes:
		title (str): movie title
		storyline (str): summery of the movie
		poster_image_url (str): movie poster url
		trailer_youtube_url (str): movie trailer youtube url
	'''
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_url):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_url

	def show_trailer(self):
		'''show trailer with given url'''
		webbrowser.open(self.trailer_youtube_url)

	def show_poster(self):
		'''show poster image'''
		webbrowser.open(self.poster_image_url)
