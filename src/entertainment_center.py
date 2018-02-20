import os
import json
import fresh_tomatoes
import media


def map_dict_to_object(movie):
    """ converter of movie structure: From Dictionary to Movie Object"""
    return media.Movie(
        title=movie['title'],
        poster_image_url='https://i.ytimg.com/vi/{}/mqdefault.jpg'.format(
            movie['id']),
        storyline=movie['storyline'],
        trailer_youtube_url='https://youtu.be/{}'.format(movie[
            'id'])
    )


JSON_PATH = os.path.join(os.getcwd(), 'src', media.Movie.DATASOURCE)

with open(JSON_PATH) as movies_file:
    # Convert movies from string to list of dictionary
    MOVIES_DICT = json.loads(movies_file.read())

    # Convert from list of dictionary to list of Movie instances
    MOVIES = map(map_dict_to_object, MOVIES_DICT)

    # Generate HTML and Open Web Page
    fresh_tomatoes.open_movies_page(MOVIES)
