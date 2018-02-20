import fresh_tomatoes
import media

MOVIES_LIST = [{
    'id': 'KYz2wyBy3kc',
    'title': 'Toy Story',
    'storyline': 'Woody Memorable Moments.'
}, {
    'id': 'eu1jekOB7sw',
    'title': 'The Jungle',
    'storyline': 'Disney Movies For Kids | Movies For Kids | Animation Movies For Children'
}, {
    'id': 'F_QW5TI5cqA',
    'title': 'Caillou, LiVE!',
    'storyline': ' Fun for Kids | Videos for Toddlers | Full Episodes'
}, {
    'id': '3b2jrx2eMP8',
    'title': 'Disney Movies For Kids',
    'storyline': ' Movies For Kids - Animation Movies For Children'
}]

# lambda converter of movie structure: From Dictionary structure to Movie Object

map_dict_to_object = lambda movie: media.Movie(
    title=movie['title'],
    poster_image_url='https://i.ytimg.com/vi/{}/mqdefault.jpg'.format(
        movie['id']),
    storyline=movie['storyline'],
    trailer_youtube_url='https://youtu.be/{}'.format(movie['id'])
)

# Convert the whole list from list of dictionary to list of Movie instances

MOVIES = map(map_dict_to_object, MOVIES_LIST)

# Generate HTML and Open Web Page

fresh_tomatoes.open_movies_page(MOVIES)
