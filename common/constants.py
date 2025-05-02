import os
from pathlib import Path

from ten_utils.log import LoggerConfig
from ten_utils.env_loader import EnvLoader


# env
ENV_MODE = os.getenv("ENV", "dev")

if ENV_MODE == "dev":
    env_loader = EnvLoader(f".env.{ENV_MODE}")

elif ENV_MODE == "prod":
    env_loader = EnvLoader(getenv_mode=True)

else:
    raise ValueError("Incorrect value of the environment variable ENV_MODE")

# path
DIR_DATA = env_loader.load("DIR_DATA", Path)
DIR_MUSIC = DIR_DATA / "music"
DIR_MUSIC_COVER = DIR_DATA / "music_cover"

# database
DATABASE_URL = env_loader.load("DATABASE_URL", str)
DATABASE_LOG: bool = env_loader.load("DATABASE_LOG", bool)

# log
LoggerConfig().set_default_level_log(
    env_loader.load("LOG_LEVEL", int)
)  # setting the default logging level value
