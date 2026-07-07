
import sys
print("Python:", sys.version)

try:
    print("Importing transformers...")
    from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
    print("Success.")
except Exception as e:
    print(f"Transformers Error: {e}")

try:
    print("Importing torch...")
    import torch
    print(f"Torch: {torch.__version__}")
except Exception as e:
    print(f"Torch Error: {e}")

MODEL_NAME = "unitary/multilingual-toxic-xlm-roberta"
print(f"Loading {MODEL_NAME}...")
try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
    print("Model loaded.")
except Exception as e:
    print(f"Model Load Error: {e}")
