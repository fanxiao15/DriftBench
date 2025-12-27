import argparse
import json
import os
import sys 
import math
from utils import *

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def extract_json_string(s: str) -> str:
    first_brace = s.find("{")
    last_brace = s.rfind("}")
    if first_brace == -1 or last_brace == -1:
        raise ValueError("No valid JSON found in the string")
    return s[first_brace:last_brace+1]

def main(args):

    data_path = f"../datas/{args.label_type}_{args.data_type}.json"
    with open(data_path, encoding='utf-8') as file:
        datas = json.load(file)
    total_data_size = len(datas)
    
    print(f"Total data size: {total_data_size}")
   
    prompt_template = open("../Prompts/Vanilla_Detection.md", encoding='utf-8')
    pre_prompt = prompt_template.read()
    
    all_results = []

    sample_count = 0
    resume_count = 0
    root_image_path = "YOUR_IMAGE_ROOT_PATH/"  # todo: set your image root path here
    
    save_path = f"{args.save_root}/{args.model}/{args.label_type}_{args.data_type}.json"
    print("save_path: ", save_path)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    if args.resume:
        pre_result_path = open(f"{save_path}", encoding='utf-8')
        pre_results = json.load(pre_result_path)
        for index in range(len(pre_results)):
            all_results.append(pre_results[index])
            resume_count += 1
    
    for index in range(len(datas)):
        sample_count += 1
        if sample_count <= resume_count:
            continue
        image_id = datas[index]['image_id']
        article_id = datas[index]['article_id']
        caption = datas[index]['caption']

        print("-" * 80)
        print(f'Name: {article_id}_{image_id} | Index: {sample_count}')
        print("Caption: ", caption)

        image_path = root_image_path +  datas[index]['image_folder'] + f'/{article_id}_{image_id}.jpg'
       
        evidence_tmp = datas[index]['visual_search_evidence']
        print("visual_evidence: ", evidence_tmp)
        
        label = datas[index]['label']

        prompt = pre_prompt.format(caption, evidence_tmp)
        
        response = generate_lvlm(prompt, image_path, model=args.model)
                
        response_json = json.loads(extract_json_string(response))
        print("response: ", response_json)

        result = {
            "image_id": image_id, "article_id": article_id, "label": label,"caption": caption,
            "visual_search_evidence":evidence_tmp,
            "prediction":response_json['label'],
            "explanation": response_json['explanation'],
        }

        all_results.append(result)
        
        with open(f"{save_path}", 'w+', encoding='utf-8') as f:
                    f.write(json.dumps(all_results, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--label_type', type=str, default='Pristine', help='')
    parser.add_argument('--data_type', type=str, default='D_I_O_T', help='')
    parser.add_argument('--model', type=str, default='gpt-4o-mini-2024-07-18', help='')
    parser.add_argument('--save_root', type=str, default='./Results', help='')

    parser.add_argument('--resume', action='store_true', default=False, help='Resume from the last time')

    args = parser.parse_args()
    print(args)
    main(args)