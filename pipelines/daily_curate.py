import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
RAW_CSV = BASE / "backend" / "data" / "sensor_data.csv"
CURATED_DIR = BASE / "backend" / "data" / "curated"
CURATED_DIR.mkdir(exist_ok=True)

def main():
    if not RAW_CSV.exists():
        print("No sensor_data.csv, execute backend.")
        return

    df = pd.read_csv(RAW_CSV)
    df["ts_iso"] = pd.to_datetime(df["ts_iso"], errors="coerce")
    df = df.dropna(subset=["sound_raw"])
    df = df.sort_values("ts_iso")
    df["sound_raw"] = df["sound_raw"].astype(int)

    for day, group in df.groupby(df["ts_iso"].dt.date):
        out = CURATED_DIR / f"sound_temp_{day}.csv"
        group.to_csv(out, index=False)
        print(f"Curate archive: {out}")

if __name__ == "__main__":
    main()