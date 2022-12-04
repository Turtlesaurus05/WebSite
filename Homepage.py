import streamlit as st
bottom_image = "https://images.vexels.com/media/users/3/246391/isolated/preview/73f72c0a6b0a9d4c1629b720e77a4dbe-western-welcome-sign.png"
st.set_page_config(
    page_title="Multipage",
    page_icon=":house:"
)

st.image(bottom_image, width=500)


with st.container():
    st.subheader("About me   ")
    st.write("I am a software developer student from Finland! ")
    st.write("Currently i am on my second year of my studies. ")
    st.write(" The languages that i am the best at are probaply Python, html and C#")
    st.write("In my free time i like to practice my python skills to be a pythong pro :sunglasses:")
    st.write("---")
