You are given a news post, inncluding an image, a piece of text, and a list of titles in which the image has appeared. Your task is to predict whether there is misinformation between the given image and text.


Generate a JSON object with two properties: 'label', 'explanation'. 
The return value of 'label' property should be selected from ["real", "fake"].
Fake indicates there is misinformation between the given image and text.
Real indicates that there is no misinformation between the given image and text.
The return value of 'explanation' property should be a detailed reasoning for the given 'label'.

Note that your response will be passed to the python interpreter, SO NO OTHER WORDS! And do not add Markdown syntax like ```json、'', just only output the json object.

The given text:
{}

The list of titles related to the image content:
{}

Your Response:
