from PIL import Image

import utils
from utils import inputs, layout_streamlit
import streamlit as st
import replicate
import os
import requests # request img from web
import shutil # save img locally
from utils import load_gan

os.environ["REPLICATE_API_TOKEN"] = "81f2e4dc54d050256a9aa63fc1ad0679aa35a287"


def main() :
    model,version = load_gan()


    layout_streamlit()
    prompt = st.text_input('Enter Text')


    # https://replicate.com/cjwbw/anything-v3-better-vae/versions/09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65#input
    inputs = utils.inputs
    inputs['prompt'] = prompt
    # print(inputs["prompt"])
    # print(inputs)
    # https://replicate.com/cjwbw/anything-v3-better-vae/versions/09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65#output-schema

    # Add a generate button
    if st.button("Generate"):

        output = version.predict(**inputs)


        ## image saving :
        res = requests.get(output[0])
        img_data = res.content
        # import io
        # image = Image.open(io.BytesIO(img_data))

        st.image(output, caption='Image from link', use_column_width=True)

        if st.button('Download'):
            # st.markdown("<a href=" + output[0] + " download>Download Image</a>", unsafe_allow_html=True)
            st.markdown('<a href="' + model.to_base64(output) + '" download>Download Image</a>', unsafe_allow_html=True)
            # st.markdown("<a href=" + image_url + " download>Download Image</a>", unsafe_allow_html=True)
        #
        # # Add a share button
        # if st.button("Share on Twitter"):
        #     st.text("Share this on Twitter")
        #     st.text("https://twitter.com/intent/tweet?text=" + prompt)
        # if st.button("Share"):
        #     if st.button("Share"):

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    main()


















































#
#
#
# layout_streamlit()
# prompt = st.text_input('Enter Text')
#
# from utils import load_gan
# model,version = load_gan()
# # https://replicate.com/cjwbw/anything-v3-better-vae/versions/09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65#input
# inputs = inputs
# print(inputs["prompt"])
# print(inputs)
# # https://replicate.com/cjwbw/anything-v3-better-vae/versions/09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65#output-schema
#
# output = version.predict(**inputs)
#
# print(len(output))
# print(output)
#
# ## image saving :
# res = requests.get(output[0])
# img_data = res.content
# st.image(img_data, caption='Image from link', use_column_width=True)
#
# # if res.status_code == 200:
# #     file_name = "zabba.jpg"
# #     with open(file_name, 'wb') as f:
# #         shutil.copyfileobj(res.content, f)
# #     print('Image sucessfully Downloaded: ', file_name)
# # else:
# #     print('Image Couldn\'t be retrieved')
