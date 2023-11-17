from pathlib import Path
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import streamlit_authenticator as stauth

st.set_page_config(page_title="My First website",page_icon=":slightly_smiling_face:",layout="wide")    



def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/snowflake.css")

animation_symbol = "❄"

st.markdown(f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
     """,
    unsafe_allow_html=True
    )



def load_lottieurl(url):
        r=requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")



lottie_coding1 = load_lottieurl("https://lottie.host/9b2a89a5-d9a0-4608-9d4e-f030808d2413/NdNuH7Ucdv.json")
lottie_coding = load_lottieurl("https://lottie.host/bf24d36a-f102-4bae-8585-517913c5d179/3GeOb51MOw.json")
img_minecraft = Image.open("Images/images.jpeg")
img_free_fire = Image.open("Images/download.jpeg")

with st.container():
        left_column,right_column = st.columns(2)
        with left_column:
            st.subheader("Hi,I am Manthan :wave:")
            st.title("My First Project")
            st.write("Just chilling out with codding and here it's just an website with no hopes and no aim :partying_face:")
            st.write("[So,just go and watch Youtube >](https://www.youtube.com/)")
        with right_column:
            st_lottie(lottie_coding1,height=300,key="coding1")
            
with st.container():
        st.write("---")
        left_column,right_column = st.columns(2)
        with left_column:
            st.header("About me")
            st.write("##")
            st.write("""
                Hello guys !! :slightly_smiling_face: :wave:
                I am a student of a reputed school in school.
                I want to became a Software enginner in future.
                Also blah blah blah blah...........

                (Its just a example so just treat it as a example don't read it if you think your time is precisious 😎)
                """)



            st.write("[Former YT channel(make sure to subscribe it) :face_with_monocle:](https://www.youtube.com/@FreezingEYES21)")
        with right_column:
            st_lottie(lottie_coding,height=300,key="coding")


with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(img_minecraft)
        with text_column:
            st.subheader("My Minecraft animation ")
            st.write("""
                        Here I created a cool minecraft animation!!
                        Make sure to like and subscribe
                    """)
            st.markdown("[Watch Video...](https://youtube.com/shorts/J_tG6e-Dvic?si=RHPbTro8MyGXzZD9)")
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(img_free_fire)
        with text_column:
            st.subheader("Free Fire all evo guns emotes")
            st.write("""
                        Here I created a cool Free fire evo guns emote video!!
                        Make sure to like and subscribe
                    """)
            st.markdown("[Watch Video...](https://youtu.be/xbrqV_JKcwk?si=C0GdHb1cHxepcaDE)")   

with st.container():
        st.write("---")
        st.header("Get in touch with me!!")
        st.write("##")

        contact_form = """
        <form action="https://formsubmit.co/manthanrauthan1@email.com" method="POST">
             <input type="hidden" name="_recaptcha" value="false">
             <input type="text" name="name" placeholder = "Your name" required>
             <input type="email" name="email" placeholder = "Your email address" required>
             <textarea name ="message" placeholder = "Your message here" required></textarea>
             <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
    
