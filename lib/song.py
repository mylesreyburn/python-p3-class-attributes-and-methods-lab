class Song:
    
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre) -> None:
        self.increase_song_count()
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_artist(artist)
        self.add_genre(genre)

    @classmethod
    def increase_song_count(cls):
        cls.count += 1
        
    @classmethod
    def add_artist(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
            cls.artist_count[artist] = 0
        cls.artist_count[artist] += 1

    @classmethod
    def add_genre(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
            cls.genre_count[genre] = 0
        cls.genre_count[genre] += 1