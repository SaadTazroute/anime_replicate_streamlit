# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import replicate
    import os
    os.environ["REPLICATE_API_TOKEN"] = "81f2e4dc54d050256a9aa63fc1ad0679aa35a287"
    model = replicate.models.get("cjwbw/anything-v3-better-vae")

    version = model.versions.get("09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65")

    # https://replicate.com/cjwbw/anything-v3-better-vae/versions/09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65#input
    inputs = {
        # Input prompt
        'prompt': "masterpiece, best quality, illustration, beautiful detailed, finely detailed, dramatic light, intricate details, 1girl, brown hair, green eyes, colorful, autumn, cumulonimbus clouds, lighting, blue sky, falling leaves, garden",

        # The prompt or prompts not to guide the image generation (what you do
        # not want to see in the generation). Ignored when not using guidance.
        # 'negative_prompt': ...,

        # Width of output image. Maximum size is 1024x768 or 768x1024 because
        # of memory limits
        'width': 512,

        # Height of output image. Maximum size is 1024x768 or 768x1024 because
        # of memory limits
        'height': 512,

        # Number of images to output
        'num_outputs': 2,

        # Number of denoising steps
        # Range: 1 to 500
        'num_inference_steps': 20,

        # Scale for classifier-free guidance
        # Range: 1 to 20
        'guidance_scale': 7,

        # Choose a scheduler.
        'scheduler': "DPMSolverMultistep",

        # Random seed. Leave blank to randomize the seed
        # 'seed': ...,
    }

    # https://replicate.com/cjwbw/anything-v3-better-vae/versions/09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65#output-schema
    output = version.predict(**inputs)
    print(output)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
