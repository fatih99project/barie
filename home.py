import streamlit as st

st.set_page_config(
    page_title="Portfolio | FATIHULBARIE",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("SELAMAT DATANG DI PORTFOLIO SAYA 👨‍🎓")

st.sidebar.success("SILAHKAN PILIH MENU DI ATAS")

import streamlit as st

col1, col2 = st.columns(2)

with col1:
   st.header("About Me")
   st.image("me.jpg", width= 290)

with col2:
   st.header("Data Diri")
   st.subheader("NAMA : FATIHUL BARRI ALMAHMUDI ")
   st.caption("NIM : 0402201176")
   st.write(
            """
            - Tempat Tanggal Lahir : Brebes 20 Februari 1999
            - Alamat               : Tanjung Tanjung Brebes
            - Hobi                 : tidur
            - Cita-cita            : sukses [sukses dalam tidurnya :D] 
            - Status               : BERNAFAS
            """
        )

st.header("*Call Me If You Want*")

st.link_button("Go to contact", "http://localhost:8501/contact")
