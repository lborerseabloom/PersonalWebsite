// These variables will act as an in-memory cache.
// A "warm" function invocation can reuse the token from a previous run.
let accessToken = null;
let tokenExpiresAt = 0;

async function refreshAccessToken() {
    const {
        SPOTIFY_CLIENT_ID,
        SPOTIFY_CLIENT_SECRET,
        SPOTIFY_REFRESH_TOKEN
    } = process.env;

    // In Node.js, we use Buffer to create a Base64 string.
    const authHeader = Buffer.from(`${SPOTIFY_CLIENT_ID}:${SPOTIFY_CLIENT_SECRET}`).toString('base64');

    // To send 'application/x-www-form-urlencoded' data, we use URLSearchParams.
    const body = new URLSearchParams({
        grant_type: 'refresh_token',
        refresh_token: SPOTIFY_REFRESH_TOKEN,
    });

    const response = await fetch('https://accounts.spotify.com/api/token', {
        method: 'POST',
        headers: {
            'Authorization': `Basic ${authHeader}`,
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: body.toString(),
    });

    const data = await response.json();

    if (!response.ok) {
        throw new Error(`Failed to refresh token: ${JSON.stringify(data)}`);
    }

    accessToken = data.access_token;
    // Date.now() gives milliseconds, so divide by 1000 to get seconds like Python's time.time().
    // We subtract 60 seconds as a buffer to ensure the token is still valid.
    tokenExpiresAt = (Date.now() / 1000) + data.expires_in - 60;
}

async function getCurrentPlaying() {
    // Check if the token is missing or has expired.
    if (!accessToken || (Date.now() / 1000) >= tokenExpiresAt) {
        await refreshAccessToken();
    }

    const response = await fetch('https://api.spotify.com/v1/me/player/currently-playing', {
        headers: {
            'Authorization': `Bearer ${accessToken}`,
        },
    });

    // 204 No Content: Nothing is playing.
    if (response.status === 204) {
        return null;
    }
    
    // 401 Unauthorized: The token might have expired. Refresh and retry.
    if (response.status === 401) {
        await refreshAccessToken();
        return getCurrentPlaying(); // Retry the request
    }
    
    if (!response.ok) {
        throw new Error(`Spotify API error: ${response.statusText}`);
    }

    return response.json();
}

// This is the main function Netlify will run.
exports.handler = async function(event, context) {
    try {
        const data = await getCurrentPlaying();

        // If nothing is playing or the data is malformed.
        if (!data || !data.item) {
            return {
                statusCode: 200,
                body: JSON.stringify({ playing: false }),
            };
        }

        const item = data.item;
        const result = {
            playing: true,
            track: item.name,
            // .map().join() is the JavaScript equivalent of the Python list comprehension.
            artists: item.artists.map(a => a.name).join(', '),
            albumArt: item.album.images[0].url,
        };

        return {
            statusCode: 200,
            body: JSON.stringify(result),
        };

    } catch (e) {
        // Log the error for debugging in the Netlify function logs.
        console.error(e);
        return {
            statusCode: 500,
            body: JSON.stringify({ playing: false, error: e.toString() }),
        };
    }
};