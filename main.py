import time

from ten_utils.log import Logger

from common.constants import (
    ENV_MODE,
)
from sync.database import sync_db_table_tracks


logger = Logger(__name__, level=0)


def run_sync() -> None:
    """
    Функция для запуска синхронизации.
    Используется и нужна для точки входа программы.
    :return: None
    """
    logger.debug(f"The mode of operation is set: {ENV_MODE}")
    logger.info("Synchronisation server started!")


    if ENV_MODE == "dev":
        """
        При запуске в режиме разработки, 
        скрипт синхронизации запускается каждые 10 сек
        """
        while True:
            logger.info("Start synchronization of track paths...")
            sync_db_table_tracks()
            logger.info("Finish synchronization of track paths!")
            print("--------------------------------------------")

            time.sleep(10)

    elif ENV_MODE == "prod":
        """
        При запуске в режиме продакшена,
        скрипт синхронизации запускается с помощью cron
        внутри docker образа
        """
        logger.info("Start synchronization of track paths...")
        sync_db_table_tracks()
        logger.info("Finish synchronization of track paths!")
        print("--------------------------------------------")

    else:
        logger.critical("ENV environment variable is not set")


if __name__ == "__main__":
    try:
        run_sync()

    except KeyboardInterrupt:
        pass
