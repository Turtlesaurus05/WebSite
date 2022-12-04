import streamlit as st


st.set_page_config(page_title="Projects", page_icon=":blue_heart:", layout="wide")


_right, mid = st.columns([1,1])
with _right:
    st.title("Welcome to my projects")
with mid:
    st.markdown("![Alt Text](https://media4.giphy.com/media/ukMiDlCmdv2og/giphy.gif?cid=ecf05e472grb5svh58vsuxxe6zx3ihaywkif7kzcd161rqr0&rid=giphy.gif&ct=g)")



with st.container():
    st.write("---")
    st.write("##")
    st.subheader("Random password generator")
    st.write(
        "Simply just enter how long you want the password to be and after that you enter how many passwords you would like!")
    st.write("https://github.com/Turtlesaurus05/Pythons/blob/master/Passgen.py")
    st.write("---")

    #Alexa texts
    st.subheader("Alexa 2.0")
    st.write("""

    We all know Alexa the expensive amazon ai. Well i made my own Alexa for absolutely free! Want it to play a song from youtube? No problem just say 'Alexa play Ariana grande'
    """)
    st.write("https://github.com/Turtlesaurus05/Pythons/blob/master/MyAlexa.py")



#Coming soon
    st.write("---")
    st.write("##")
    st.subheader(" Youtube song to mp3 file")
    st.write("Coming soon!")
    st.write("---")




