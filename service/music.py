from typing import List, Any

from sqlalchemy import Table, RowMapping

from database.config import SessionLocal, metadata, engine


tracks = Table("tracks", metadata, autoload_with=engine)


def get_all_tracks() -> List[RowMapping[str, Any]]:
    with SessionLocal() as session:
        result = session.execute(tracks.select()).mappings().all()

        return list(result)
