import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_FILE = BASE_DIR / "data" / "raw" / "AB_NYC_2019.csv"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
CLEAN_FILE = PROCESSED_DIR / "airbnb_cleaned.csv"

def clean_airbnb_data(df:pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["name"] = df["name"].fillna("Unknown")
    df["host_name"] = df["host_name"].fillna("Unknown")
    df["reviews_per_month"] = df["reviews_per_month"].fillna(0)

    df["last_review"] = pd.to_datetime(df["last_review"], errors="coerce")

    df = df.drop_duplicates()

    df = df[df["price"] >= 0]
    df = df[df["minimum_nights"] <=1]

    return df

def main() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(RAW_FILE)
    df_clean = clean_airbnb_data(df)
    df_clean.to_csv(CLEAN_FILE, index=False)

    print("Cleaned file created:")
    print(CLEAN_FILE)
    print(f"Row count: {len(df_clean)}")


if __name__ == "__main__":
    main()



