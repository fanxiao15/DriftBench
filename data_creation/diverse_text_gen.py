import argparse
from utils import llm_generate

def main(args):
    Prompt = """
        Below is a news headline. Please rewrite it while ensuring the original meaning remains unchanged.

        news headline: {}
        
        rewritten version: 
        """

    caption = "Winter Up Top Summer Down Low Taken from my garden in Essert Romand French Alps after the first snowfall of the impending winter season"

    prompt = Prompt.format(caption)
    rewritten_caption = llm_generate(prompt)
    print("falsified Caption: ", rewritten_caption)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    args = parser.parse_args()
    print(args)
    main(args)