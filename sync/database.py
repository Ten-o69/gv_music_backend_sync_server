from pathlib import Path
import os

from ten_utils.log import Logger

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


logger = Logger(__name__, level=0)


def sync_db_table_tracks():
    logger.info("Retrieving data from the database...")
    track_list = get_all_tracks()
    logger.info("Data retrieval from the db is complete!")

    logger.info("Retrieving data from the file system...")
    paths_to_tracks = []
    paths_to_track_covers = []
    paths_to_local_tracks = Path(DIR_MUSIC).glob('*.mp3')
    paths_to_local_track_covers = Path(DIR_MUSIC_COVER).glob('*.jpg')
    logger.info("Retrieving data from the file system is complete!")

    logger.debug("Convert relative paths "
                 "from the database to full paths in the file system...")
    for track in track_list:
        track = CustomDict(dict(track))
        paths_to_tracks.append(DIR_DATA / track.path)
        paths_to_track_covers.append(DIR_DATA / track.cover_path)

    logger.info("Synchronising paths to music tracks...")
    for local_path_to_track in paths_to_local_tracks:
        if local_path_to_track not in paths_to_tracks:
            os.remove(local_path_to_track)
    logger.info("Synchronisation of music track paths is complete!!!")

    logger.info("Synchronising paths to music track artwork...")
    for local_path_to_track_cover in paths_to_local_track_covers:
        if local_path_to_track_cover not in paths_to_track_covers:
            os.remove(local_path_to_track_cover)
    logger.info("Synchronisation of music track artwork paths is complete!!!")
