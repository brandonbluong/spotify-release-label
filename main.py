import json
import requests
from requests.auth import HTTPBasicAuth

SPOTIFY_GET_PROFILE_URL = "https://api.spotify.com/v1/me"
# Access token expires after one hour
ACCESS_TOKEN = "BQAqMD1uAzwcEeFtTD9TYllRYYJc9haSKiDw4H8rG8Zyc_AWu2XyPpFe2jfRr0iNz2dhGSjyy1lHa3A2sFG4rSzYvluhbjYCOOEnq6ljP4D6NJvoXquRwNMYAVxaEXgmJK512VaX9iLJN3VqsJ2ThwCtnGHY350s4q_Av-n147LjKxr0BJ20xxjsJsvg5zg"


def get_profile():
    response = requests.get(
        SPOTIFY_GET_PROFILE_URL, headers={"Authorization": f"Bearer {ACCESS_TOKEN}"}
    )
    json_resp = response.json()
    return json.dumps(json_resp, indent=4)


def main():
    profile = get_profile()
    print(profile)


if __name__ == "__main__":
    main()
