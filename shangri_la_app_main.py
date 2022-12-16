#################################################
## Spotipy Quickstart from ReadTheDocs 
## https://pypi.org/project/spotipy/
#################################################

## Parses top tracks from an Artist and outputs the data into Python Shell terminal

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="2d654f4b2613491fa490239c10426f0a",
                                                           client_secret="f876b42b91a24ecf89418a5cefea0a09"))

number_of_tracks = 10

results = sp.search(q='Journey', limit=number_of_tracks)

## for loop has been condensed and 'track', 'audio', and 'cover art' have been included into the idx for loop
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
