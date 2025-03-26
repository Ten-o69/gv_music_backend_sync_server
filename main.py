import time

from ten_utils.log import Logger

from common.constants import (
    ENV_MODE,
)
from service.music import get_all_music


logger = Logger(__name__, level=4)


def run_sync():
    if ENV_MODE == "dev":
        while True:
            time.sleep(10)
            pass

    elif ENV_MODE == "prod":
        pass

    else:
        logger.critical("ENV environment variable is not set")


if __name__ == "__main__":
    try:
        run_sync()

    except KeyboardInterrupt:
        pass
