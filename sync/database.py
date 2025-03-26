from pathlib import Path
import os

from service.music import (
    get_all_tracks,
)
from common.helpers import (
    CustomDict,
)
from common.constants import (
    DIR_DATA,
    DIR_MUSIC,
    DIR_MUSIC_COVER,
)


def sync_db_table_tracks():
    track_list = get_all_tracks()
    paths_to_tracks = []
    paths_to_track_covers = []
    paths_to_local_tracks = Path(DIR_MUSIC).glob('*.mp3')
    paths_to_local_track_covers = Path(DIR_MUSIC_COVER).glob('*.jpg')

    for track in track_list:
        track = CustomDict(dict(track))
        paths_to_tracks.append(DIR_DATA / track.path)
        paths_to_track_covers.append(DIR_DATA / track.cover_path)

    for local_path_to_track in paths_to_local_tracks:
        if local_path_to_track not in paths_to_tracks:
            os.remove(local_path_to_track)

    for local_path_to_track_cover in paths_to_local_track_covers:
        if local_path_to_track_cover not in paths_to_track_covers:
            os.remove(local_path_to_track_cover)
