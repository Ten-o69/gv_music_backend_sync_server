from pathlib import Path
import os

from ten_utils.log import Logger

from service.music import get_all_tracks
from common.helpers import CustomDict
from common.constants import (
    DIR_DATA,
    DIR_MUSIC,
    DIR_MUSIC_COVER
)


logger = Logger(__name__)


def sync_db_table_tracks() -> None:
    """
    Synchronizes the local file system with music track data from the database.

    This function compares the list of music tracks and their cover images
    stored in the database with the actual files in the local file system.
    Any files that are not present in the database are removed from the file system.

    Workflow:
    1. Fetches all track records from the database.
    2. Gathers current `.mp3` and `.jpg` files from the music directory.
    3. Compares database paths with actual files on disk.
    4. Deletes unused music and artwork files from the local directories.

    Logging messages are emitted at every major step for tracking the process.

    Raises:
        OSError: If a file cannot be deleted due to permission issues or similar.

    Example:
        >>> sync_db_table_tracks()
    """
    logger.info("Retrieving data from the database...")
    track_list = get_all_tracks()
    logger.info("Data retrieval from the db is complete!")

    logger.info("Retrieving data from the file system...")
    paths_to_tracks = []
    paths_to_track_covers = []

    # Get all .mp3 and .jpg file paths
    paths_to_local_tracks = Path(DIR_MUSIC).glob('*.mp3')
    paths_to_local_track_covers = Path(DIR_MUSIC_COVER).glob('*.jpg')
    logger.info("Retrieving data from the file system is complete!")

    logger.debug("Convert relative paths from the database "
                 "to full paths in the file system...")

    # Convert track rows to full filesystem paths
    for track in track_list:
        track = CustomDict(dict(track))
        paths_to_tracks.append(DIR_DATA / track.path)

        if track.cover_path is not None:
            paths_to_track_covers.append(DIR_DATA / track.cover_path)

    logger.info("Synchronising paths to music tracks...")
    # Delete orphaned track files
    for local_path_to_track in paths_to_local_tracks:
        if local_path_to_track not in paths_to_tracks:
            os.remove(local_path_to_track)
    logger.info("Synchronisation of music track paths is complete!!!")

    logger.info("Synchronising paths to music track artwork...")
    # Delete orphaned artwork files
    for local_path_to_track_cover in paths_to_local_track_covers:
        if local_path_to_track_cover not in paths_to_track_covers:
            os.remove(local_path_to_track_cover)
    logger.info("Synchronisation of music track artwork paths is complete!!!")
