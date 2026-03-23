import streamlit as st
import pandas as pd

st.set_page_config(page_title="Packet Monitor", layout="wide")

st.title("🛰️ Network Packet Monitor")

# Dummy data (replace with API call)
data = pd.DataFrame([
    {"src": "192.168.1.5", "dst": "8.8.8.8", "proto": "TCP", "length": 60},
    {"src": "192.168.1.10", "dst": "1.1.1.1", "proto": "UDP", "length": 120}
])

st.dataframe(data)

# Filters
protocol = st.selectbox("Filter by Protocol", ["ALL", "TCP", "UDP"])
if protocol != "ALL":
    data = data[data["proto"] == protocol]

st.write("Filtered Traffic")
st.dataframe(data)
