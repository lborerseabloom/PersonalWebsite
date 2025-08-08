import os
import time
import base64
import requests

access_token = None
token_expires_at = 0

def refresh_access_token():
    global access_token, token_expires_at

    CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']
    CLIENT_SECRET = os.environ['SPOTIFY_CLIENT_SECRET']
    REFRESH_TOKEN = os.environ['SPOTIFY_REFRESH_TOKEN']

    auth_header = f"{CLIENT_ID}:{CLIENT_SECRET}".encode('utf-8')
    base64_auth = base64.b64encode(auth_header).decode('utf-8')

    response = requests.post(
        'https://accounts.spotify.com/api/token',
        headers={
            'Authorization': f'Basic {base64_auth}',
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data={
            'grant_type': 'refresh_token',
            'refresh_token': REFRESH_TOKEN
        }
    )

    data = response.json()
    if response.status_code != 200:
        raise Exception(f"Failed to refresh token: {data}")

    access_token = data['access_token']
    token_expires_at = time.time() + data['expires_in']

def get_current_playing():
    global access_token
    if not access_token or time.time() >= token_expires_at:
        refresh_access_token()

    response = requests.get(
        'https://api.spotify.com/v1/me/player/currently-playing',
        headers={'Authorization': f'Bearer {access_token}'}
    )

    if response.status_code == 204:
        return None
    elif response.status_code == 401:
        refresh_access_token()
        return get_current_playing()

    return response.json()

def handler(event, context):
    try:
        data = get_current_playing()
        if not data or 'item' not in data:
            return {
                "statusCode": 200,
                "body": '{"playing": false}'
            }

        item = data['item']
        result = {
            'playing': True,
            'track': item['name'],
            'artists': ', '.join([a['name'] for a in item['artists']]),
            'albumArt': item['album']['images'][0]['url']
        }
        import json
        return {
            "statusCode": 200,
            "body": json.dumps(result)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": '{"playing": false, "error": "%s"}' % str(e)
        }
