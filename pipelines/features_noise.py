import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
CURATED_DIR = BASE / "backend" / "data" / "curated"
FEATURE_DIR = BASE / "backend" / "data" / "features"
FEATURE_DIR.mkdir(exist_ok=True)

def noise_bucket(v):
    if v < 70:
        return "LOW"
    elif v < 150:
        return "MEDIUM"
    return "HIGH"

def main():
    csv_files = list(CURATED_DIR.glob("sound_temp_*.csv"))
    if not csv_files:
        print("No curated archive, execute daily_curate.py first")
        return

    for csv_path in csv_files:
        df = pd.read_csv(csv_path, parse_dates=["ts_iso"])
        df["noise_level"] = df["sound_raw"].apply(noise_bucket)
        df["hour"] = df["ts_iso"].dt.hour
        out = FEATURE_DIR / csv_path.name.replace("sound_temp_", "features_")
        df.to_csv(out, index=False)
        print(f"✅ Archivo de features creado: {out}")

if __name__ == "__main__":
    main()
