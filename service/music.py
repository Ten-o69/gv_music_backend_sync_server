from typing import List, Any

from sqlalchemy import Table, RowMapping

from database.config import SessionLocal, metadata, engine


# Define the table object using SQLAlchemy's reflection
tracks = Table("tracks", metadata, autoload_with=engine)


def get_all_tracks() -> List[RowMapping[str, Any]]:
    """
    Retrieve all records from the 'tracks' table.

    This function opens a new SQLAlchemy session using `SessionLocal`,
    performs a `SELECT *` query on the `tracks` table, and returns
    the result as a list of dictionary-like `RowMapping` objects.

    Each `RowMapping` behaves like a dictionary, allowing access to
    column values by key (e.g., `row["column_name"]`).

    Returns:
        List[RowMapping[str, Any]]:
            A list of mappings, where each mapping represents a row
            from the `tracks` table with column names as keys and
            their corresponding values.

    Example:
        >>> rows = get_all_tracks()
        >>> for row in rows:
        ...     print(row["title"], row["duration"])
    """
    with SessionLocal() as session:
        result = session.execute(tracks.select()).mappings().all()

        return list(result)
