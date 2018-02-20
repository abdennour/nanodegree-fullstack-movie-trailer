import webbrowser

# __doc__
# __name__
# __module__
class Movie(object): # pylint: disable=too-few-public-methods 
    """ Model for movies instances """
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """ Open the movie trailer in the browser"""
        webbrowser.open(self.trailer_youtube_url)
