import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="ESP32 Sound (Live)", page_icon="🔊", layout="wide")
st.title("🔊 ESP32 Sound – Live Dashboard")
st_autorefresh(interval=8000, key="live-refresh")

BASE = Path(__file__).resolve().parents[1]
DATA_DIR = BASE / "backend" / "data"
RAW_CSV = DATA_DIR / "sensor_data.csv"

st.sidebar.header("Debug")
st.sidebar.write("BASE:", BASE)
st.sidebar.write("RAW_CSV:", RAW_CSV)


if not RAW_CSV.exists():
    st.warning("Data does not exist. ESP32 should be sending and backend running..")
    st.stop()

df = pd.read_csv(RAW_CSV)

if df.empty:
    st.info("El archivo existe pero no tiene datos.")
    st.stop()

df["ts_iso"] = pd.to_datetime(df["ts_iso"], errors="coerce")
df = df.dropna(subset=["ts_iso"])
df = df.sort_values("ts_iso")

def to_noise_level(v):
    if v < 800:
        return "LOW"
    elif v < 2000:
        return "MEDIUM"
    return "HIGH"

df["noise_level"] = df["sound_raw"].apply(to_noise_level)

col1, col2, col3 = st.columns(3)
col1.metric("Total Lectures", len(df))
col2.metric("Last sound_raw", int(df["sound_raw"].iloc[-1]))
col3.metric("Last update", datetime.now().strftime("%H:%M:%S"))

st.subheader("Last Lectures")
st.dataframe(df.tail(30), use_container_width=True)

c1, c2 = st.columns(2)

with c1:
    st.subheader("Sound vs Time (live)")
    st.line_chart(df.set_index("ts_iso")["sound_raw"])

with c2:
    st.subheader("Level of noise")
    st.bar_chart(df["noise_level"].value_counts())

st.caption("Updates automatically every 8 seg, if esp32 is reading and Flask app is running.")