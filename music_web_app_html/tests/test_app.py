from playwright.sync_api import Page, expect

# """
# We can get an emoji from the /emoji page
# """
# def test_get_emoji(page, test_web_address): # Note new parameters
#     # We load a virtual browser and navigate to the /emoji page
#     page.goto(f"http://{test_web_address}/emoji")

#     # We look at the <strong> tag
#     strong_tag = page.locator("strong")

#     # We assert that it has the text ":)"
#     expect(strong_tag).to_have_text(":)")

# # Tests for your routes go here
"""
When I call GET /albums 
All albums are returned 
"""
def test_get_albums(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums")

    div_items = page.locator("p")

    text = ["Title: DoolittleReleased: 1989",
    "Title: Surfer RosaReleased: 1988",
    "Title: WaterlooReleased: 1974",
    "Title: Super TrouperReleased: 1980",
    "Title: BossanovaReleased: 1990",
    "Title: LoverReleased: 2019",
    "Title: FolkloreReleased: 2020",
    "Title: I Put a Spell on YouReleased: 1965",
    "Title: BaltimoreReleased: 1978",
    "Title: Here Comes the SunReleased: 1971",
    "Title: Fodder on My WingsReleased: 1982",
    "Title: Ring RingReleased: 1973",
    "Title: VoyageReleased: 2022"]
    
    expect(div_items).to_have_text(text)

    
"""
When I call GET /albums/<int:id> with an album.id
That album is returned
"""


"""
When I call 
"""



"""
When I call POST /albums with album info
That album is now in the list returned by GET /albums
"""
# def test_post_albums(db_connection, web_client):
#     db_connection.seed("seeds/music_library.sql")
#     post_response = web_client.post("/albums", data =
#     {
#         'title': 'Little Girl Blue',
#         'release_year': '1959',
#         'artist_id': 4
#     })
#     assert post_response.status_code == 200
#     assert post_response.data.decode("utf-8") == ""

#     get_response = web_client.get("/albums")
#     assert get_response.status_code == 200
#     assert get_response.data.decode("utf-8") == "Album(1, Doolittle, 1989, 1), Album(2, Little Girl Blue, 1959, 4)"








# def test_get_books(db_connection, page, test_web_address):
#     # We seed our database with the book store seed file
#     db_connection.seed("seeds/book_store.sql")

#     # We load a virtual browser and navigate to the /books page
#     page.goto(f"http://{test_web_address}/books")

#     # We look at all the <li> tags
#     list_items = page.locator("li")

#     # We assert that it has the books in it
#     expect(list_items).to_have_text([
#         "Invisible Cities by Italo Calvino",
#         "The Man Who Was Thursday by GK Chesterton",
#         "Bluets by Maggie Nelson",
#         "No Place on Earth by Christa Wolf",
#         "Nevada by Imogen Binnie",
#     ])


# """
# We can retrieve a single book
# """
# def test_get_book(db_connection, page, test_web_address):
#     db_connection.seed("seeds/book_store.sql")

#     # We visit the books page
#     page.goto(f"http://{test_web_address}/books")

#     # Click the link with the text 'Bluets by Maggie Nelson'
#     page.click("text=Bluets by Maggie Nelson")

#     # The virtual browser acts just like a normal browser and goes to the next
#     # page without us having to tell it to.

#     # Then we look for specific test classes that we have put into the HTML
#     # as targets for our tests to look for. This one is called `t-title`.
#     # You can see it in `templates/books/show.html`
#     title_element = page.locator(".t-title")
#     expect(title_element).to_have_text("Title: Bluets")

#     # We do the same for the author name
#     author_element = page.locator(".t-author-name")
#     expect(author_element).to_have_text("Author: Maggie Nelson")