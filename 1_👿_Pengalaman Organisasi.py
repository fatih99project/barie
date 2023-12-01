import streamlit as st

st.set_page_config(
    page_title="Pengalaman Organisasi| FATIHULBARIE",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("Pengalaman Organisasi")
st.write("Beberapa Organisasi Yang Saya Ikuti; ")

st.container()
col1, = st.columns(1)
with col1:
    st.subheader("IPNU")


st.container()
st.write("---")
col1, = st.columns(1)
with col1:
   
    st.image("IPNU.png", width= 190)


st.container()
st.write("---")
col1, = st.columns(1)
with col1:
    st.write("*Menjabat Sebagai Ketua*")
