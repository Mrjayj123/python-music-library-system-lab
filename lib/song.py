class Song:
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artists_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Trigger class methods automatically upon creation   
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)   
        
    @classmethod
    def add_song_to_count(cls):        
        cls.count += 1
        
    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.add(genre)
        
    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.add(artist)
        
    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1
        
    @classmethod
    def add_to_artists_count(cls, artist):
        cls.artists_count[artist] = cls.artists_count.get(artist, 0) + 1


if __name__ == "__main__":
  
    S1 = Song("Halo", "Beyonce", "Pop")
    print(Song.count) 