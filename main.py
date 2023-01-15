import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials
cid = '6b0fcacdc9e24abaa5f8da3144748059'
secret = ''
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

playlistLink1 = input("Enter the first playlist link: ")
playlist_URI1 = playlistLink1.split("/")[-1].split("?")[0]

results = sp.playlist(playlist_URI1)
results = results + sp.playlist(playlist_URI1)
json.dumps(results, indent=4)

songTitle1 = []
songArtist1 = []

for item in results['tracks']['items']:
    songTitle1.append(item['track']['name'])
    songArtist1.append(item['track']['artists'][0]['name'])
print(len(songTitle1))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

playlistLink2 = input("Enter the second playlist link: ")
playlist_URI2 = playlistLink2.split("/")[-1].split("?")[0]

results = sp.playlist(playlist_URI2)
json.dumps(results, indent=4)

songTitle2 = []
songArtist2 = []

for item in results['tracks']['items']:
    songTitle2.append(item['track']['name'])
    songArtist2.append(item['track']['artists'][0]['name'])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


print("Songs in common: ")

if len(songTitle1) <= len(songTitle2):
    for x in range(len(songTitle1)):
        print(songTitle1[x])
        for y in range(len(songTitle2)):
            if songTitle1[x] == songTitle2[y] and songArtist1[x] == songArtist2[y]:
                print(songTitle1[x] + " - " + songArtist1[x])
elif len(songTitle1) > len(songTitle2):
    for x in range(len(songTitle2)):
        for y in range(len(songTitle1)):
            if songTitle1[y] == songTitle2[x] and songArtist1[y] == songArtist2[x]:
                print(songTitle1[y] + " - " + songArtist1[y])
