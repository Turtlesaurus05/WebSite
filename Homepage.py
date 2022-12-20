import streamlit as st
bottom_image = "https://png.pngtree.com/png-vector/20220922/ourmid/pngtree-retro-style-welcome-text-element-png-image_238439.png"
st.set_page_config(
    page_title="My app",
    page_icon=":house:"
)

st.image(bottom_image, width=600)


with st.container():
    st.subheader("About me   ")
    st.write("I am a software developer student from Finland! ")
    st.write("Currently i am on my second year of my studies. ")
    st.write(" The languages that i am the best at are probaply Python and C#")
    st.write("In my free time i like to practice my python skills to be a python pro :sunglasses:")
    st.write("---")
