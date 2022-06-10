from .myspotifyapi import SpotifyAPI
from .schemas import SearchSchema
from fastapi import FastAPI
app = FastAPI()


# Log in with your Spotify account. Click on 'Create an app'.  
# After creation, you get client_id and  client_secret.

client_id = "xxxxxxxxxxxx"
client_secret = "xxxxxxxxx"

spotify = SpotifyAPI(client_id, client_secret)

@app.get("/get-albums/{ids}")
def get_albums(ids:str):
    try:
        response = spotify.get_albums(ids)
    except Exception as e:
        return {"message":str(e)}
    return response

@app.get("/get-albums")
def get_several_albums():
    try:
        response = spotify.get_several_albums()
    except Exception as e:
        return {"message":str(e)}
    return response

@app.get("/get-albums-track")
def get_albums_track():
    try:
        response = spotify.get_albums_track()
    except Exception as e:
        return {"message":str(e)}
    return response

@app.delete("/remove-albums/")
def remove_albums(ids:str):
    try:
        response = spotify.remove_albums(ids)
    except Exception as e:
        return {"message":str(e)}
    return response

@app.get("/get-new-releases")
def get_new_releases():
    try:
        response = spotify.get_new_releases()
    except Exception as e:
        return {"message":str(e)}
    return response

@app.post("/search")
def search(doc:SearchSchema):
    query_string = {doc.search_type.value:doc.query}
    try:
        response = spotify.search(query_string, doc.search_type)
    except Exception as e:
        return {"message":str(e)}
    return response


