import argparse
import json
from sklearn.metrics import classification_report, confusion_matrix
import sys

def main(args):

    namespace = [f"./{args.method}/{args.method}_{args.label_type}_{args.data_type}"]


    labels = []
    predictions = []
    current_index = 0
    
    for path_name in namespace:
        r_path = f"{path_name}.json"
        print(r_path)
        result_path = open(r_path, encoding='utf-8')
        results = json.load(result_path)
        
        if args.method == "SNIFFER":
            for i, item in enumerate(results):
                if item['prediction'] != "unknow":
                    if item['prediction'] == 'real':
                        predictions.append(0)
                    else:
                        predictions.append(1)
                    if item['label'] == 'real':
                        labels.append(0)
                    else:
                        labels.append(1)
        else:
            for i in range(len(results)):
                image_id = results[i]['image_id']
                article_id = results[i]['article_id']
                if article_id != image_id:
                    labels.append(1)
                else:
                    labels.append(0)
                if results[i]['prediction'] == 'fake':
                    predictions.append(1)
                else:
                    predictions.append(0)
                current_index += 1
        target_names = ['TrueInformation', 'MisInformation']
        print(classification_report(labels, predictions, target_names=target_names, digits=4))
        print(confusion_matrix(labels, predictions))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--method', type=str, default='GPT-4o', choices=['GPT-4o', 'claude-3-7', 'qwen-3', 'CMIE', 'LEMMA', 'SNIFFER'])
    parser.add_argument('--data_type', type=str, choices=['O_I_O_T', 'D_I_O_T', "O_I_D_T", 'D_I_D_T', "O_I_F_T", "F_I_F_T"], default='O_I_O_T')
    parser.add_argument('--label_type', type=str, default='Pristine', choices=['Pristine', 'Falsified'])
    args = parser.parse_args()
    print(args)
    main(args)
    # python ./eval_tab_4.py --method ['GPT-4o', 'claude-3-7', 'qwen-3', 'CMIE', 'LEMMA', 'SNIFFER'] --label_type ['Pristine', 'Falsified'] --data_type ['O_I_O_T', 'D_I_O_T', "O_I_D_T", 'D_I_D_T', "O_I_F_T", "F_I_F_T"]