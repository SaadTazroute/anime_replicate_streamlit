from io import BytesIO

import numpy as np
import replicate
import logging
from skimage.transform import resize
import streamlit as st
import streamlit.components.v1 as components

from PIL import Image

import variables
import random
import streamlit as st
import requests

list_of_prompts = variables.list_of_prompts


# print(list_of_prompts)
# prompt = "lol"

# if len(prompt.split(" ")) > 40 :
#     print("Prompt too long it should be under 40 char")
#     prompt = prompt[:40]


def load_gan():
    model = replicate.models.get("cjwbw/anything-v3-better-vae")

    version = model.versions.get("09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65")
    return model, version


logging.basicConfig(format="\n%(asctime)s\n%(message)s", level=logging.INFO, force=True)


# def generate_images(prompt:str):
#     model,version = load_gan()
#
#     if st.session_state.n_requests >= 5:
#         st.session_state.text_error = "Too many requests. Please wait a few seconds before generating another text or image."
#         logging.info(f"Session request limit reached: {st.session_state.n_requests}")
#         st.session_state.n_requests = 1
#         return
#     with image_spinner_placeholder:
#         with st.spinner("Please wait while your image is being generated..."):
#
#
#             st.session_state.n_requests += 1
#             st.session_state.image = openai.image(processed_prompt)
#             logging.info(f"Tweet: {prompt}\nImage prompt: {processed_prompt}")


def generate_img(version, inputs, placeholder):
    st.session_state.text_error = ""
    # if len(inputs["prompt"])<2:
    #     st.session_state.text_error = "Please enter a correct description ! "
    # st.session_state.text_error = False
    # if st.session_state.text_error:
    #     print("mok")
    #     st.error(st.session_state.text_error)

    col1, col2, col3, col4 = st.columns(4)
    output = version.predict(**inputs)

    ## image saving :

    return output


def generate_text_lucky(version, inputs, placeholder):
    with st.spinner("Please wait while your image is being generated..."):
        inputs["prompt"] = random.choice(list_of_prompts)

        print("Random description ", inputs["prompt"])
        output = version.predict(**inputs)

        return output


height = 512
width = 512
num_outputs = 1
inputs = {
    # Input prompt
    'prompt': random.choice(list_of_prompts),
    'width': width,
    'height': height,
    'num_outputs': num_outputs,
    'num_inference_steps': 10,
    'guidance_scale': 7,
    'scheduler': "DPMSolverMultistep",
}


def add_images(output):
    col1, col2, col3 = st.columns(3)

    res = requests.get(output[0])
    image = res.content
    img = np.asarray(Image.open(BytesIO(image)))

    with col1:
        print(output)

        image1 = st.image(img, caption='Generated image1 ', use_column_width='auto')

    with col2:
        # resize
        resized_img = resize(img, (100, 100))
        image2 = st.image(resized_img, caption='Generated image', use_column_width='auto')
    with col3:
        # resize
        resized_img = resize(img, (800, 800))
        image2 = st.image(resized_img, caption='Generated image', use_column_width='auto')
    return img


import base64


def share_button(output):
    # Get the URL of the image
    URL = output[0]
    Facebook_url = f"https://www.facebook.com/sharer/sharer.php?u={URL}"

    #
    # components.html(
    #
    #
    # f"""
    # <a href="https://www.facebook.com/sharer/sharer.php?u={URL}" target="_blank">
    #     <img src="https://en.m.wikipedia.org/wiki/File:Facebook_Logo_%282019%29.png" alt="Share on Facebook" />
    # </a>
    # """
    #
    #
    #
    # )
    components.html(
        f"""
            <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" 
            data-text="Check my cool Streamlit Web-App🎈" 
            data-url="{URL}"
            data-show-count="false">
            data-size="Large" 
            data-hashtags="streamlit,python"
            Tweet
            </a>
            <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        """
    )
    # st.image(url, width=400)


def initialize_template():
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    components.html(
        '''
        <style>
          html {
            background-color: #F7F9FC;
          }
          .stApp {
            background-color: #F7F9FC;
            border-radius: 20px;
            font-family: 'Sawarabi Gothic', sans-serif;
            font-size: 16px;
            padding: 10px;
          }
          h1 {
            font-size: 20px;
            font-weight: bold;
            color: #F7F9FC;
            text-align: center;
            font-family: 'Sawarabi Gothic', sans-serif;
          }
          img {
            width: 300px;
            border-radius: 10px;
          }
          .stText {
            font-family: 'Sawarabi Gothic', sans-serif;
            font-size: 16px;
            padding-top: 10px;
          }
        </style>
        '''
    )
