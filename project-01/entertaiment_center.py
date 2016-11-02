import media
import fresh_tomatoes

#instance the 3 movies with their respective data
sw1 = media.Movie(	"Star Wars 1", 
					"Two Jedi Knights escape a hostile blockade to find allies and "
					"come across a young boy who may bring balance to the Force.", 
					"http://img.lum.dolimg.com/v1/images/Star-Wars-Phantom-Menace-I-Poster_3c1ff9eb.jpeg?region=15%2C9%2C651%2C979&width=480", 
					"https://www.youtube.com/watch?v=bD7bpG-zDJQ",
					"https://es.wikipedia.org/wiki/Star_Wars:_Episode_I_-_The_Phantom_Menace")

sw2 = media.Movie(	"Star Wars 2", 
					"Ten years after initially meeting, Anakin Skywalker shares a "
					"forbidden romance with Padme, while Obi-Wan "
					"investigates an assassination attempt on the Senator.", 
					"https://s-media-cache-ak0.pinimg.com/originals/d3/e3/1e/d3e31e5775d1aed0820b555da52d0677.jpg", 
					"https://www.youtube.com/watch?v=CO2OLQ2kiq8",
					"https://es.wikipedia.org/wiki/Star_Wars:_Episode_II_-_Attack_of_the_Clones")

sw3 = media.Movie(	"Star Wars 3", 
					"During the near end of the clone wars, Darth Sidious has "
					"revealed himself and is ready to execute the last part"
					" of his plan to rule the Galaxy.", 
					"http://cdn.traileraddict.com/content/20th-century-fox/starwars3.jpg", 
					"https://www.youtube.com/watch?v=5UnjrG_N8hU",
					"https://es.wikipedia.org/wiki/Star_Wars:_Episode_III_-_Revenge_of_the_Sith")

#create an array and add the movies to it
movies = [sw1, sw2, sw3]

#function that will render and open the website
fresh_tomatoes.open_movies_page(movies)