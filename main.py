import json
import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import urlencode

ENDPOINT = "https://api.spotify.com/v1/me/following"
# Access token expires after one hour
ACCESS_TOKEN = "BQCTADw7cH-d3uOwA1efqN1grjOpjq_wJopKA7YlR4WoahoTeKsEi8qGNERH8nSpLjEDDF5YScbB6skCZWQTTP00oD_s9UpgEN033S2epawL3YXTSywZEWRdmQrclPgOzc_Y1SW7yXb7f5n34HHgBlztTsjbGfIQtZibU57s0Q760FGqE5ZSkic"


def get_followed_artists(last_artist_id=None):
    # create lookup_url
    if last_artist_id:
        query_params = {"type": "artist", "after": f"{last_artist_id}", "limit": "50"}
    else:
        query_params = {"type": "artist", "limit": "50"}

    lookup_url = f"{ENDPOINT}?{urlencode(query_params)}"

    # pass lookup_url into requests
    response = requests.get(
        lookup_url, headers={"Authorization": f"Bearer {ACCESS_TOKEN}"}
    )
    return response.json()


def add_artist_page(query, total_artists=list()):

    # query['artists'].keys() -> ['items', 'next', 'total', 'cursors', 'limit', 'href']
    page = query["artists"]["items"]  # data
    page_artist = [artist["name"] for artist in page]
    total_artists.extend(page_artist)

    next_artist_id = query["artists"]["cursors"].get("after", None)

    if next_artist_id:
        next_query = get_followed_artists(next_artist_id)
        add_artist_page(next_query, total_artists)

    return total_artists


def main():

    response = get_followed_artists()
    total_artists = sorted(add_artist_page(response))
    print(total_artists)


if __name__ == "__main__":
    main()
