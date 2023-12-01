import streamlit as st

st.set_page_config(
    page_title="Riwayat Sekolah | FATIHULBARIE",
    page_icon="👨‍🎓",
    layout="wide"
)
st.title("BEBERAPA JENJANG PENDIDIKAN YANG SAYA LALUI SELAMA MASA HIDUP")

st.container()
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.subheader("SDN TANJUNG 02")
   
with col2:
    st.subheader("SMPN TANJUNG 01")
    
with col3:
    st.subheader("SMK 01 KERSANA")
   
with col4:
    st.subheader("UNU Rombel AL Bukhori")

with st.container():
        col1, col2, col3, col4, = st.columns(4)
        with col1:
            st.caption("*Alamat : Jl. Cemara - Tanjung - Brebes*")
        with col2:
            st.caption("*Alamat : Jl. Cemara - Tanjung - Brebes*")
        with col3:
            st.caption("*Alamat : Jl. jagapura - Kersana - Brebes*")
        with col4:
            st.caption("*Alamat : Gedung BLKK Pesantren Al Bukhori, Jl. Cemara Gg. At Taubah Rt. 07 Rw. 03, Sengon - Tanjung - Brebes*")
   
