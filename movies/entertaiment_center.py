import media
import fresh_tomatoes

#Star Wars
sw1 = media.Movie("Star Wars 1", 
						"Anakin guachin", 
						"http://img.lum.dolimg.com/v1/images/Star-Wars-Phantom-Menace-I-Poster_3c1ff9eb.jpeg?region=15%2C9%2C651%2C979&width=480", 
						"https://www.youtube.com/watch?v=bD7bpG-zDJQ")

sw2 = media.Movie("Star Wars 2", 
						"Anakin pibito enojado", 
						"https://s-media-cache-ak0.pinimg.com/originals/d3/e3/1e/d3e31e5775d1aed0820b555da52d0677.jpg", 
						"https://www.youtube.com/watch?v=CO2OLQ2kiq8")

sw3 = media.Movie("Star Wars 3", 
						"Anakin se retoba y la pudre", 
						"http://cdn.traileraddict.com/content/20th-century-fox/starwars3.jpg", 
						"https://www.youtube.com/watch?v=5UnjrG_N8hU")

#print(star_wars.storyline)
#star_wars.show_trailer()

movies = [sw1, sw2, sw3]

fresh_tomatoes.open_movies_page(movies)