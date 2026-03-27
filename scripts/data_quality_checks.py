import sqlite3
import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "nyc.db"


def run_quality_checks() -> None:
    conn = sqlite3.connect(DB_PATH)

    try:
        row_count = pd.read_sql(
            "SELECT COUNT(*) AS cnt FROM airbnb_listings;", conn
        ).iloc[0]["cnt"]

        if row_count == 0:
            raise ValueError("airbnb_listings table is empty")

        negative_prices = pd.read_sql(
            "SELECT COUNT(*) AS cnt FROM airbnb_listings WHERE price < 0;", conn
        ).iloc[0]["cnt"]

        if negative_prices > 0:
            raise ValueError("Negatif price found")

        invalid_nights = pd.read_sql(
            "SELECT COUNT(*) AS cnt FROM airbnb_listings WHERE minimum_nights < 1;", conn
        ).iloc[0]["cnt"]

        if invalid_nights > 0:
            raise ValueError("Found an entry with minimum_nights < 1 ")

        print("Passed the quality checks")

    finally:
        conn.close()


def main() -> None:
    run_quality_checks()


if __name__ == "__main__":
    main()