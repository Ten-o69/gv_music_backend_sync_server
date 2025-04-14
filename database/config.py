from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from common.constants import (
    DATABASE_URL,
    DATABASE_LOG,
)


engine = create_engine(DATABASE_URL, echo=DATABASE_LOG)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
metadata = MetaData()
