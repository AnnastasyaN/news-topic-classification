from pathlib import Path

from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Root Project
BASE_DIR = Path(__file__).resolve().parent.parent

# Model Directory (IndoBERT fine-tuned)
MODEL_DIR = BASE_DIR / "saved_model"

# Paths for components
LABEL_ENCODER_PATH = MODEL_DIR / "label_encoder.pkl"
MODEL_PATH = str(MODEL_DIR)
TOKENIZER_PATH = str(MODEL_DIR)


def load_model_and_tokenizer():
    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_DIR, local_files_only=True
    )
    model.eval()
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_DIR, local_files_only=True
    )
    return model, tokenizer