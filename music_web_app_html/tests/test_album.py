from lib.album import Album

"""
Album constructs with an id, title, release_year, artist_id
"""
def test_album_constructs():
    album = Album(1, "Test Album", 1980, 2)
    assert album.id == 1
    assert album.title == "Test Album"
    assert album.release_year == 1980
    assert album.artist_id == 2

"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    album = Album(1, "Test Album", 1980, 2)
    assert str(album) == "Album(1, Test Album, 1980, 2)"

"""
We can compare two identical albums
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album(1, "Test Album", 1980, 2)
    album2 = Album(1, "Test Album", 1980, 2)
    assert album1 == album2
