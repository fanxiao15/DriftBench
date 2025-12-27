import argparse
from utils import llm_generate

def main(args):
    
    if args.pollution_type == 'support':
        Prompt = """
        You will receive a news caption, which is a textual description of a news event.

        Your task is to rewrite this description into a supporting event — that is, to support the original statement.

        Here is the original caption: {}

        # Output (Json)
        Output:
        """
    if args.pollution_type == 'refute':
        Prompt = """
        You will receive a news caption, which is a textual description of a news event.

        Your task is to rewrite this description into a refuting event — that is, to refute the original statement.

        Here is the original caption: {}

        # Output (Json)
        Output:
        """

    caption = "Winter Up Top Summer Down Low Taken from my garden in Essert Romand French Alps after the first snowfall of the impending winter season"

    prompt = Prompt.format(caption)
    rewritten_caption = llm_generate(prompt)
    print(f"{args.pollution_type} Evidence: ", rewritten_caption)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--pollution_type', type=str, default='refute', choices=['refute', 'support'])  
    args = parser.parse_args()
    print(args)
    main(args)
