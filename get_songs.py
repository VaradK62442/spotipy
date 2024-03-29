import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials


def get_artists():
    spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

    if len(sys.argv) > 1:
        name = ' '.join(sys.argv[1:])
    else:
        name = 'Freaky'

    results = spotify.search(q='track:'+name, type='track')
    items = results['tracks']['items']
    if len(items) > 0:
        for title in items:
            print(f"{title['name']}: {', '.join([n['name'] for n in title['artists']])}")


def main():
    get_artists()


if __name__ == "__main__":
    main()
