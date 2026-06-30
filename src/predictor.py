import torch
import torch.nn.functional as F

from src.preprocessing import preprocess_text
from src.model_loader import load_models

model, tokenizer, label_encoder = load_models()


def predict_news(text: str) -> dict:
    """Predict news topic category using fine-tuned IndoBERT.

    Args:
        text: Raw news headline or text.

    Returns:
        dict with keys:
            - category (str): predicted category name.
            - confidence (float): confidence percentage (0–100).
    """
    cleaned = preprocess_text(text)

    inputs = tokenizer(
        cleaned,
        truncation=True,
        padding=True,
        max_length=64,
        return_tensors="pt",
    )

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits

    probs = F.softmax(logits, dim=-1)
    best_idx = torch.argmax(probs, dim=-1).item()
    confidence = round(float(probs[0, best_idx] * 100), 2)
    category = label_encoder.inverse_transform([best_idx])[0]

    return {"category": category, "confidence": confidence}
