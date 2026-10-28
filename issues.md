# Issues Found: music_catalog.py

Name: Maniish Rajendran | SRN: PES2UG24CS265

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| SQL injection (Bandit B608, Medium) | Security | 10 | INSERT query built with `%` string formatting, so a title like `x'); DROP TABLE songs;--` alters the query | Use a parameterized query: `VALUES (?, ?, ?)` with a tuple of values |
| Unsafe pickle deserialization (Bandit B301, Medium) | Security | 33 | `pickle.loads` on a blob can execute arbitrary code if the data is untrusted | Replace pickle with `json.dumps` / `json.loads` |
| Pickle import (Bandit B403, Low) | Security | 1 | Importing pickle flags a security risk | Removed the import by switching to `json` |
| Insecure random (Bandit B311, Low) | Security | 17 | `random.choice` is not cryptographically secure | Use `secrets.choice` |
| Mutable default argument (Pylint W0102) | Bug | 9 | `playlist=[]` is created once and shared across calls, so songs leak between playlists | Default to `None` and create a new list inside the function |
| Bare except (Pylint W0702, Flake8 E722) | Bug | 39 | `except:` hides every error, including KeyboardInterrupt | Catch `sqlite3.Error` only |
| SUM returns None on empty table | Bug | 38 | `SUM()` returns `None` when there are no rows, so `total_plays` could return `None` instead of a number | Added `or 0` |
| Function names not snake_case (Pylint C0103) | Style | 9, 15, 28, 32, 36 | `addSong`, `shufflePick`, `savePlaylist`, `loadPlaylist`, `totalPlays` | Renamed to `add_song`, `shuffle_pick`, `save_playlist`, `load_playlist`, `total_plays` |
| Missing docstrings (Pylint C0114, C0116) | Style | 1, 9, 15, 20, 28, 32, 36, 43 | No module or function docstrings | Added a docstring to the module and every function |
| Lines too long (Flake8 E501, Pylint C0301) | Style | 6, 10, 21, 49 | Lines exceed 79 characters | Wrapped lines across multiple lines |
| Ambiguous variable name (Flake8 E741) | Style | 47 | Variable named `l` looks like `1` | Renamed to `loaded` (and `pl` to `playlist`) |
| Multiple statements on one line (Flake8 E701, Pylint C0321) | Style | 48 | `if ...: print(...)` on one line | Put the `print` on its own indented line |
| Unnecessary else after return (Pylint R1705) | Style | 24 | `else` after `return` in `popularity` | Removed the `else` and de-indented |
| main() runs on import (design) | Bug | 52 | `main()` is called at module level, so importing the file runs the demo | Wrapped in `if __name__ == "__main__":` |
| Module-level constant naming (Pylint C0103) | Style | 5 | `conn` is a module-level constant-like global | Renamed to `CONN` |

## Results

| Tool | Before | After |
|------|--------|-------|
| Pylint | 4.57/10 | 10.00/10 |
| Bandit | 4 issues (2 Medium, 2 Low) | No issues identified |
| Flake8 | 7 warnings | 0 warnings |
