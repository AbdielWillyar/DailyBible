import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

url = "https://docs.google.com/spreadsheets/d/1b1nzezQIXNXC3WUTsuPCrL4jRskfeZItCDuzYqV5f2M/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, ttl=5)

st.markdown("<h1 style='text-align: center; color: #4A659D;'>Daily Bible Devotions - BMW Church</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border:1px solid #FF4B4B'>", unsafe_allow_html=True)

data['Tanggal'] = pd.to_datetime(data['Tanggal'])

#pilih tanggal
tanggal = st.date_input("Pilih Tanggal Renungan", datetime.today())
selected_data = data[data['Tanggal'] == pd.to_datetime(tanggal)]

if not selected_data.empty:
    st.markdown("Renungan: " + selected_data.iloc[0]['Tanggal'].strftime("%d %B %Y"))
    st.markdown(f"""
        <div style='padding: 20px; background-color: #f9f9f9; border-radius: 10px color: black;'>
            {selected_data.iloc[0]['Konten']}
        </div>
    """, unsafe_allow_html=True)
else:
    st.title("No data available for this date")

# Footer
st.markdown("<footer style='text-align: center; padding: 10px; position: fixed; left: 0; bottom: 0; width: 100%; background-color: #f0f2f6; color: black;'>"
            "<p>© 2024 by Ps. Steven Y. Goni - BMW Church.</p></footer>", 
            unsafe_allow_html=True)
