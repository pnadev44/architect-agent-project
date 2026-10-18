import os

# Centralizing the model configuration
# Defaulting to gemini-2.5-flash which is available and cost-effective
MODEL = os.getenv("MODEL_NAME", "gemini-2.5-flash")
MAX_REJECTIONS = int(os.getenv("MAX_REJECTIONS", "1"))