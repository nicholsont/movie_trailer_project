import webbrowser

# Creates the movie class
class Movie():
    # Initializes the movie class
    def __init__(self, title, duration, rating, poster_image_url, trailer_url):
        self.title = title
        self.duration = duration
        self.rating = rating
        self.poster_image_url = poster_image_url
        self.trailer_url = trailer_url
    # Opens the movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_url)