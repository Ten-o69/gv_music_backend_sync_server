from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from ten_utils.log import Logger

from common.constants import (
    DATABASE_URL,
    DATABASE_LOG,
    LOG_LEVEL,
)


logger = Logger(__name__, level=LOG_LEVEL)


if DATABASE_URL:
    engine = create_engine(DATABASE_URL, echo=DATABASE_LOG)
    SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    metadata = MetaData()

else:
    logger.critical("DATABASE_URL environment variable is not set")
