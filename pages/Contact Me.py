import streamlit as st

st.header(":mailbox: Get in touch with me !")

contact_form = """
<form action="https://formsubmit.co/turtlesaurus05@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="your name" required>
     <input type="hidden" name="_autoresponse" value="Hello, I will response to you as soon as i can!">
     <input type="email" name="email" placeholder="Your Email Address" required>
     <textarea name="message" placeholder="Type your message/Problem"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)

local_css("style.css")
