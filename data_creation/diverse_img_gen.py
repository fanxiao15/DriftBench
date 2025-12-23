import torch
from diffusers import FluxPriorReduxPipeline, FluxPipeline
from diffusers.utils import load_image
import os
import json
import sys
import argparse
from pathlib import Path

def main(args):

    pipe_prior_redux = FluxPriorReduxPipeline.from_pretrained("black-forest-labs/FLUX.1-Redux-dev", torch_dtype=torch.bfloat16).to("cuda:1")
    pipe = FluxPipeline.from_pretrained(
        "black-forest-labs/FLUX.1-dev" , 
        text_encoder=None,
        text_encoder_2=None,
        torch_dtype=torch.bfloat16
    ).to(args.device)

    folder_path = args.ori_data_folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            print(file_path)
            save_name = file_path.split("/")[-1]

            image = load_image(file_path)
            pipe_prior_output = pipe_prior_redux(image)
            images = pipe(
                guidance_scale=2.0,
                num_inference_steps=20,
                generator=torch.Generator("cpu").manual_seed(0),
                **pipe_prior_output,
            ).images
            save_file = os.path.join(args.save_folder, save_name)
            images[0].save(save_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--ori_data_folder", type=str, default="Original_images") 
    parser.add_argument("--save_folder", type=str, default="Diverse_Image") 
    parser.add_argument("--device", type=str, default="cuda:0")
    args = parser.parse_args()
    main(args)