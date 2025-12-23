import argparse
import json
from sklearn.metrics import classification_report, confusion_matrix
import sys

def main(args):

    namespace = [f"./{args.method}/{args.method}_Pristine_{args.data_type}", f"./{args.method}/{args.method}_Falsified_{args.data_type}"]
    
    
    
    labels = []
    predictions = []
    current_index = 0
    
    for path_name in namespace:
        r_path = f"{path_name}.json"
        print(r_path)
        result_path = open(r_path, encoding='utf-8')
        results = json.load(result_path)
        if args.method == "SNIFFER":
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
    parser.add_argument('--data_type', type=str, choices=['O_I_O_T', 'D_I_O_T'], default='O_I_O_T')
    args = parser.parse_args()
    
    print(args)
    main(args)