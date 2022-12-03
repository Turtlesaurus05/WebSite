import streamlit as st

st.set_page_config(
    page_title="Multipage",
    page_icon=":house:"
)

st.title("Welcome! :wave: ")


with st.container():
    st.subheader("About me   ")
    st.write("I am a software developer student from Finland! ")
    st.write("Currently i am on my second year of my studies. ")
    st.write(" The languages that i am the best at are probaply Python, html and C#")
    st.write("In my free time i like to practice my python skills to be a pythong pro :sunglasses:")
    st.write("---")

