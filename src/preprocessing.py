import re


def basic_text_cleaning(text):
    """Clean and normalize text for classification.

    Mirrors the function defined in the notebook for consistency
    between local inference and Colab training.

    Steps:
    1. Handle None/NaN -> empty string
    2. Convert to string
    3. Convert to lowercase
    4. Remove URLs
    5. Remove HTML tags
    6. Collapse extra whitespace
    7. Strip leading/trailing whitespace

    Args:
        text: Raw input text.

    Returns:
        Cleaned text string.
    """
    if not isinstance(text, str):
        text = ""

    text = text.lower()

    text = re.sub(r"http\S+|www\S+", "", text)

    text = re.sub(r"<.*?>", "", text)

    text = re.sub(r"\s+", " ", text)

    text = text.strip()

    return text


preprocess_text = basic_text_cleaning
