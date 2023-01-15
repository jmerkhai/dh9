import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials
cid = '6b0fcacdc9e24abaa5f8da3144748059'
secret = '82e1ec90361c474ab40349ea922b5958'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

playlistLink1 = input("Enter the first playlist link: ")
playlist_URI1 = playlistLink1.split("/")[-1].split("?")[0]

playlistData = sp.playlist(playlist_URI1)
json.dumps(playlistData, indent=4)

songTitle1 = []
songArtist1 = []

for item in playlistData['tracks']['items']:
    songTitle1.append(item['track']['name'])
    songArtist1.append(item['track']['artists'][0]['name'])

print(songTitle1)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

playlistLink2 = input("Enter the second playlist link: ")
playlist_URI2 = playlistLink2.split("/")[-1].split("?")[0]

playlistData = sp.playlist(playlist_URI2)
json.dumps(playlistData, indent=4)

songTitle2 = []
songArtist2 = []

for item in playlistData['tracks']['items']:
    songTitle2.append(item['track']['name'])
    songArtist2.append(item['track']['artists'][0]['name'])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
print("Songs in common: ")

if len(songTitle1) < len(songTitle2):
    for x in range(len(songTitle1)):
        if songTitle1[x] == songTitle2[x] and songArtist1[x] == songArtist2[x]:
            print(songTitle1[x] + " - " + songArtist1[x])
else:
    for x in range(len(songTitle2)):
        if songTitle1[x] == songTitle2[x] and songArtist1[x] == songArtist2[x]:
            print(songTitle1[x] + " - " + songArtist1[x])
