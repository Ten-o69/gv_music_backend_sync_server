import os
from pathlib import Path

from dotenv import load_dotenv
from ten_utils.log import Logger


# base
ENV_MODE = os.getenv("ENV", "dev")
load_dotenv(f".env.{ENV_MODE}")
logger = Logger(__name__, level=4)

# path
DIR_DATA = os.getenv("DIR_DATA", None)
if DIR_DATA:
    DIR_DATA = Path(DIR_DATA)

else:
    logger.critical("DIR_DATA environment variable is not set")

DIR_MUSIC = DIR_DATA / "music"
DIR_MUSIC_COVER = DIR_DATA / "music_cover"

# database
DATABASE_URL = os.getenv("DATABASE_URL", None)
DATABASE_LOG: int | bool = int(os.getenv("DATABASE_LOG", 0))
if DATABASE_LOG == 0:
    DATABASE_LOG = False

elif DATABASE_LOG == 1:
    DATABASE_LOG = True

# log
LOG_LEVEL: int = int(os.getenv("LOG_LEVEL", 0))
