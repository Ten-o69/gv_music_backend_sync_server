import time

from ten_utils.log import Logger

from common.constants import ENV_MODE
from sync.database import sync_db_table_tracks


logger = Logger(__name__)


def run_sync_db(delay: int) -> None:
    """
    Runs a synchronization loop that updates the local file system
    to reflect the current state of the database.

    This function repeatedly calls `sync_db_table_tracks()` every `delay` seconds.
    It is designed to be used in both development and production environments.

    Args:
        delay (int): The number of seconds to wait between each synchronization.

    Example:
        >>> run_sync_db(delay=10)
    """
    while True:
        logger.info("Start synchronization of track paths...")
        sync_db_table_tracks()
        logger.info("Finish synchronization of track paths!")
        logger.info("--------------------------------------------", additional_info=False)

        time.sleep(delay)


def run_sync() -> None:
    """
    Entry point function to start the synchronization service.

    Chooses the synchronization strategy based on the current environment mode.
    - In "dev" mode: synchronizes every 10 seconds.
    - In "prod" mode: synchronizes every 60 seconds.
    - Otherwise: logs a critical error about missing or incorrect ENV config.

    Raises:
        None

    Example:
        >>> run_sync()
    """
    logger.debug(f"The mode of operation is set: {ENV_MODE}")
    logger.info("Synchronisation server started!")

    if ENV_MODE == "dev":
        # In development mode, synchronize every 10 seconds
        run_sync_db(delay=10)

    elif ENV_MODE == "prod":
        # In production mode, synchronize every 60 seconds
        run_sync_db(delay=60)

    else:
        # Critical error: no valid environment mode specified
        logger.critical("ENV environment variable is not set")


if __name__ == "__main__":
    try:
        run_sync()

    except KeyboardInterrupt:
        # Gracefully handle Ctrl+C interruption
        pass
