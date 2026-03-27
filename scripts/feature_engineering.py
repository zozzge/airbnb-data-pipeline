import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED_DIR = BASE_DIR / "data" / "processed"

CLEAN_FILE = PROCESSED_DIR / "airbnb_cleaned.csv"
FEATURED_FILE = PROCESSED_DIR / "airbnb_featured.csv"

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["price_category"] = np.select(
        [
            df["price"] < 100,
            (df["price"] >= 100) & (df["price"] < 200),
            df["price"] >= 200
        ],
        [
            "Cheap",
            "Medium",
            "Expensive"
        ],

        default = "Unknown" # hiçbir koşula girmeyen
    )

    df["is_active"] = df["reviews_per_month"] > 0
    df["price_per_review"] = df["price"] / (df["number_of_reviews"] + 1)

    return df

def main() -> None:
    df = pd.read_csv(CLEAN_FILE)

    df = add_features(df)

    df.to_csv(FEATURED_FILE, index=False)

    print("Feature engineering done")
    print(FEATURED_FILE)
    print(df[["price","number_of_reviews", "price_category", "is_active", "price_per_review"]].head())


if __name__ == "__main__":
    main()