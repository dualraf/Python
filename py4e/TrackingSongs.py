import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import xml.etree.ElementTree as ET
import pandas as pd

CLIENT_ID = '0af87a23861d49af9c6993d02914379b'
CLIENT_SECRET = "1f91261b6d2d482480af2ac29e078a45"
PLAYLIST_LINK = "https://open.spotify.com/playlist/5sdy5E6Eehi1dkt0iS2P7Z?si=df34cd04a4874429"

CLIENT_CREDENTIALS_MANAGER = SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET
)
SP = spotipy.Spotify(client_credentials_manager=CLIENT_CREDENTIALS_MANAGER)


def get_playlist_uri(playlist_link):
    return playlist_link.split("/")[-1].split("?")[0]

def get_playlist_tracks(username,playlist_id):
    results = SP.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:
        results = SP.next(results)
        tracks.extend(results['items'])
    return tracks

playlist_uri = get_playlist_uri(PLAYLIST_LINK)
the_stuff=get_playlist_tracks(CLIENT_ID,playlist_uri)
songs=list()
for track in the_stuff:
    artists=[]
    for artist in track['track']['artists']:
        artists=artist['name']
    new = ({'Name': track['track']['name'], 'Artist': artists})
    songs.append(new)

spotify=pd.DataFrame(songs)
fname="Meh.xml"
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
stuff=list()
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    genre = lookup(entry,'Genre')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    new=({'Name':name,'Artist':artist})
    if name is None or artist is None or genre is None or album is None :
        continue
    stuff.append(new)
apple_music=pd.DataFrame(stuff)

#merging
for song in spotify['Name']:
    song=song.strip()
for song in apple_music['Name']:
    song=song.strip()

spotify=spotify.sort_values('Name')
print(spotify)