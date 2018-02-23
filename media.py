import webbrowser


class Movie():
    """ A move website to show your favorite movies"""

    def __init__(self, movie_title,
                 movie_storyline, poster_image, trailer_youtube):
        """This constructor creates an instance of the object
        Movie using 4 input parameters

        :param movie_title: string
        :param movie_storyline: string
        :param poster_image: string
        :param trailer_youtube: string
        """

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Function which opens the webbrowser and
         plays the trailer using the url"""
        webbrowser.open(self.trailer_youtube_url)
