from media import Movie
import fresh_tomatoes
import os

def get_movies():
	'''Return a list of Movie objects'''
	# read data from dataset
	path = os.path.dirname(os.path.realpath(__file__))
	movie_file = open(path + '/movies.txt', 'r')
	# create a list to store movie objects with their own information
	movies = []
	for row in movie_file:
		# get each movie's information
		content = row.split('"')[1::2]
		# create a Movie object for the corresponding movie
		movie = Movie(content[0],content[1],content[2],content[3])
		# add created Movie object into the list
		movies.append(movie)
	movie_file.close()
	return movies

if __name__ == '__main__':
	# get a list of movies
	movies = get_movies()
	# render the webpage of trailers with the list of movies
	fresh_tomatoes.open_movies_page(movies)