# Data Description

### Data Types
Our dataset contains eight types of data. Among them, `Pristine` represents true information, while `Falsified` denotes misinformation. `O_I_O_T` corresponds to the original data, and the remaining types are diversified variants derived from `O_I_O_T`.

- `R_OI_OT`: A real news item sourced from a reputable outlet, consisting of an authentic image (\textit{OI}) and a human-written text (\textit{OT}) that are semantically aligned.
- `F_OI_OT`: An out-of-context (OOC) misinformation instance, created by mismatching the image and text from two different but individually trustworthy news reports—misleading when paired together.
- `R_DI_OT`: A real news instance where the image is diversified using GenAI (`DI`), while the original text remains unchanged.  
- `R_OI_DT`: A real news instance where the text is diversified (`DT`) while preserving the original image.  
- `R_DI_DT`: A real instance where both the image and text are diversified in a semantically faithful manner.  
- `F_DI_OT`: An out-of-context (OOC) fake instance where the image is replaced by a GenAI-diversified version, while keeping the mismatched original text.  
- `F_OI_FT`: A fake instance where the original image is paired with a GenAI-fabricated text (`FT`) that conveys a false narrative.  
- `F_FI_FT`: A fully fabricated fake instance where both the image (`FI`) and text (`FT`) are GenAI-synthesized.

### JSON Field Descriptions
Each JSON file contains a list of news instances with the following fields:

- `image_id`: The image ID corresponding to the VisualNews dataset.  
- `article_id`: The text ID corresponding to the VisualNews dataset.  
- `label`: The veracity label of the news item — `Real` or `Fake` (corresponding to `Pristine` or `Falsified`).  
- `caption`: The news headline.  
- `data_type`: The data type, corresponding to one of the defined categories (e.g., `P_OI_OT`, `F_OI_FT`, etc.).  
- `image_folder`: The path to the image storage directory in the DriftBench dataset.  
- `visual_search_evidence`: A list of evidence items retrieved based on image similarity search.  
- `textual_search_evidence`: A list of evidence items retrieved based on headline-based text search.



