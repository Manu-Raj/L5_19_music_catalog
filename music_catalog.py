"""Music catalog and playlist manager."""
import json
import secrets
import sqlite3

CONN = sqlite3.connect(":memory:")
CONN.execute(
    "CREATE TABLE songs "
    "(id INTEGER PRIMARY KEY, title TEXT, artist TEXT, plays INTEGER)"
)


def add_song(title, artist, plays=0, playlist=None):
    """Insert a song into the catalog and append its title to the playlist."""
    if playlist is None:
        playlist = []
    CONN.execute(
        "INSERT INTO songs (title, artist, plays) VALUES (?, ?, ?)",
        (title, artist, plays),
    )
    playlist.append(title)
    return playlist


def shuffle_pick():
    """Return the id of a randomly chosen song."""
    ids = [r[0] for r in CONN.execute("SELECT id FROM songs")]
    return secrets.choice(ids)


def popularity(title):
    """Classify a song as popular, niche or unknown by its play count."""
    row = CONN.execute(
        "SELECT plays FROM songs WHERE title = ?", (title,)
    ).fetchone()
    if row is None:
        return "unknown"
    return "popular" if row[0] > 100 else "niche"


def save_playlist(playlist):
    """Serialize a playlist to bytes (JSON, safe to load)."""
    return json.dumps(playlist).encode("utf-8")


def load_playlist(blob):
    """Deserialize a playlist from bytes produced by save_playlist."""
    return json.loads(blob.decode("utf-8"))


def total_plays():
    """Return the total number of plays across all songs."""
    try:
        return CONN.execute("SELECT SUM(plays) FROM songs").fetchone()[0] or 0
    except sqlite3.Error:
        return 0


def main():
    """Run a short demonstration."""
    playlist = add_song("Aurora", "Nila", 250)
    add_song("Monsoon", "Kavya", 40, playlist)
    blob = save_playlist(playlist)
    loaded = load_playlist(blob)
    if len(loaded) > 1:
        print("multi-song playlist")
    print(
        popularity("Aurora"),
        popularity("Monsoon"),
        shuffle_pick(),
        total_plays(),
    )


if __name__ == "__main__":
    main()
