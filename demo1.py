import streamlit as st
st.set_page_config(page_icon="😊",page_title="Dinesh portfolio",layout="centered")
st.title(body="Dinesh Eswar Reddy",anchor=False)
st.image("https://cdn.glitch.global/09c35baf-7f38-4267-9f8b-68d545980c8d/dinesh.jpeg?v=1721138782764",width=100)

st.subheader("Full stack Developer| ML | DS ",anchor=False)
with st.container(border=True):
    st.info("My name is Dinesh, and I am currently studying B.Tech 3rd year in Computer Science and Engineering (CSE). I have a strong passion for technology and programming, and I enjoy learning about new developments in the field. My interests include data science, full-stack development, and exploring new technologies. In my spare time, I like to work on personal projects and improve my skills.")
st.subheader("SKILLS")
col1,col2,col3,col4=st.columns(4)
with col1:
   with st.expander(label="languages",expanded=False):
    st.info("C, C++, JAVA, PYTHON, HTML, CSS, JAVASCRIPT")
with col2:
    with st.expander(label="databases",expanded=False):
        st.info("MYSQL, NOSQL, MONGODB, ORACLE, PHP")