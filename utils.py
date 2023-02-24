import replicate
import logging
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
    return model,version

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


def generate_text(version,inputs,placeholder):


    with st.spinner("Please wait while your image is being generated..."):
        # if len(inputs["prompt"])<2:
        #     st.session_state.text_error = "Please enter a correct description ! "
        # st.session_state.text_error = False
        # if st.session_state.text_error:
        #     print("mok")
        #     st.error(st.session_state.text_error)
        col1, col2,col3,col4 = st.columns(4)
        print(inputs)
        output = version.predict(**inputs)
        print(output)
        with col1 :
            ## image saving :
            res = requests.get(output[0])
            img_data = res.content

            st.image(output, caption='Generated image', use_column_width='auto')



def generate_text_lucky(version,inputs,placeholder):
    with st.spinner("Please wait while your image is being generated..."):

        inputs["prompt"] =  random.choice(list_of_prompts)

        print(inputs)
        output = version.predict(**inputs)

        ## image saving :
        res = requests.get(output[0])
        img_data = res.content
        col1, col2,col3,col4 = st.columns(4)
        with col1 :
            st.image(output, caption='Image from link', use_column_width="auto")



height = 768
width  = 768
num_outputs = 1
inputs = {
    # Input prompt
    'prompt': random.choice(list_of_prompts),
    'width': width,
    'height':height,
    'num_outputs': num_outputs,
    'num_inference_steps': 20,
    'guidance_scale': 7,
    'scheduler': "DPMSolverMultistep",
    }

