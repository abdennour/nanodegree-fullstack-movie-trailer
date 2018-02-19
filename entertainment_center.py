#!/usr/bin/python
import fresh_tomatoes
import media

movies_list = [{
    'title': 'Hello ACloud Guru',
    'poster_image_url': 'http://via.placeholder.com/160x250.png',
    'storyline': 'Blah Blah Blah',
    'trailer_youtube_url': 'https://youtu.be/aRvVwG4wnRw',
    }]

# lambda converter of movie structure : From Dictionary structure to Movice Object

map_dict_to_object = lambda movie: media.Movie(title=movie['title'],
        poster_image_url=movie['poster_image_url'],
        storyline=movie['storyline'],
        trailer_youtube_url=movie['trailer_youtube_url'])

# Convert the whole list

movies = map(map_dict_to_object, movies_list)

# Generate HTML and Open Web Page

fresh_tomatoes.open_movies_page(movies)
