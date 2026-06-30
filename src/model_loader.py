import joblib

from src.config import MODEL_DIR, load_model_and_tokenizer


def load_models():
    model, tokenizer = load_model_and_tokenizer()
    label_encoder = joblib.load(MODEL_DIR / "label_encoder.pkl")
    return model, tokenizer, label_encoder
