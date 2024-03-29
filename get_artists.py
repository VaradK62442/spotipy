import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials


def get_artists():
    spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

    if len(sys.argv) > 1:
        name = ' '.join(sys.argv[1:])
    else:
        name = 'Dominic Fike'

    results = spotify.search(q='artist:'+name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        for artist in items:
            print(f"{artist['name']}")


def main():
    get_artists()


if __name__ == "__main__":
    main()
