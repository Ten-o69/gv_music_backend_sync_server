from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from ten_utils.log import Logger

from common.constants import (
    DATABASE_URL,
)


logger = Logger(__name__, level=4)


if DATABASE_URL:
    engine = create_engine(DATABASE_URL, echo=False)
    SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    metadata = MetaData()

else:
    logger.critical("DATABASE_URL environment variable is not set")
