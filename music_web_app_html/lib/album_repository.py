from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.database_connection import DatabaseConnection

class AlbumRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all albums
    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums

    # Find a single album by their id
    def find(self, album_id):
        rows = self._connection.execute(
            'SELECT * from albums WHERE id = %s', [album_id])
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])

    # Create a new album
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, album):
        self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [
                                 album.title, album.release_year, album.artist_id])
        return None

    # Delete an album by their id
    def delete(self, album_id):
        self._connection.execute(
            'DELETE FROM albums WHERE id = %s', [album_id])
        return None

    # Update an existing album
    def update(self, album):
        self._connection.execute(
            'UPDATE albums SET title = %s, release_year = %s, artist_id = %s WHERE id = %s', [album.title, album.release_year, album.artist_id, album.id])
        return None
    
    def find_album_artist(self, album):
        artists = ArtistRepository(self._connection)
        artist = artists.find(album.artist_id)
        return artist.name
        