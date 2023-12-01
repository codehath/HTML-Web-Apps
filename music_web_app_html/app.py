import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

@app.route('/goodbye', methods = ['GET'])
def get_goodbye():
    return render_template('goodbye.html', message='Bye!')

# GET /albums
# Returns a list of albums
# Try it:
#   ; curl http://localhost:5001/albums
@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums/index.html', albums=albums)

# GET /albums/<id>
# Returns a single album
# Try it:
#   ; curl http://localhost:5001/albums/1

@app.route('/albums/<int:id>', methods=['GET'])
def get_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id)
    artist = repository.find_album_artist(album)
    return render_template('albums/show.html', album=album, artist=artist)


# POST /albums
# Creates a new album
# Try it:
#   ; curl -X POST -d "title=Dave&author_name=Caden%20Lovelace" http://localhost:5001/albums
@app.route('/albums', methods=['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(None, request.form['title'], request.form['release_year'], request.form['artist_id'])
    album = repository.create(album)
    return "Album added successfully"


# DELETE /albums/<id>
# Deletes a album
# Try it:
#   ; curl -X DELETE http://localhost:5001/albums/1
@app.route('/albums/<int:id>', methods=['DELETE'])
def delete_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    repository.delete(id)
    return "Album deleted successfully"

@app.route('/artists', methods = ['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template('artists/index.html', artists=artists)

@app.route('/artists', methods = ['POST'])
def create_artist():
    if ('name' not in request.form) or ('genre' not in request.form):
        response = make_response("Bad Request - Please provide a name and genre!")
        response.status_code = 400
        print("if path")
        print(request.form['name'], request.form['genre'])
        return response

    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(None, request.form['name'], request.form['genre'])
    repository.create(artist)
    return "Artists added successfully"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
