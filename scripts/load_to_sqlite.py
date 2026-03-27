import sqlite3
import pandas as pd 
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
FEATURED_FILE = BASE_DIR / "data" / "processed" / "airbnb_featured.csv"
DB_PATH = BASE_DIR / "database" / "nyc.db"


def load_to_sqlite() -> None:
    df = pd.read_csv(FEATURED_FILE)
    
    conn = sqlite3.connect(DB_PATH)
    try:
        df.to_sql("airbnb_listings", conn, if_exists="replace", index=False)
    finally:
        conn.close()

def main() -> None:
    load_to_sqlite()
    print("Data loaded into SQLite database:")
    print(DB_PATH)


if __name__ == "__main__":
    main()