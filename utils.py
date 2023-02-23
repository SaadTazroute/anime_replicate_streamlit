import replicate

import variables
import random
import streamlit as st

list_of_prompts = variables.list_of_prompts

print(list_of_prompts)
# prompt = "lol"
width  = 512
height = 512
num_outputs = 1

prompt = None
if prompt == None :
    prompt = random.choice(list_of_prompts)
# if len(prompt.split(" ")) > 40 :
#     print("Prompt too long it should be under 40 char")
#     prompt = prompt[:40]

inputs = {
    # Input prompt
    'prompt': prompt,
    # The prompt or prompts not to guide the image generation (what you do
    # not want to see in the generation). Ignored when not using guidance.
    # 'negative_prompt': ...,

    # Width of output image. Maximum size is 1024x768 or 768x1024 because
    # of memory limits
    'width': width,

    # Height of output image. Maximum size is 1024x768 or 768x1024 because
    # of memory limits
    'height':height,

    # Number of images to output
    'num_outputs': num_outputs,

    # Number of denoising steps
    # Range: 1 to 500
    'num_inference_steps': 20,

    # Scale for classifier-free guidance
    # Range: 1 to 20
    'guidance_scale': 7,

    # Choose a scheduler.
    'scheduler': "DPMSolverMultistep",


}

def layout_streamlit():
    st.set_page_config(page_title="My App")
    st.title("Anime Generation")
    # st.header("this is the markdown")
    # st.markdown("this is the header")
    # st.subheader("this is the subheader")
    # st.caption("this is the caption")

def load_gan():
    model = replicate.models.get("cjwbw/anything-v3-better-vae")

    version = model.versions.get("09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65")
    return model,version


