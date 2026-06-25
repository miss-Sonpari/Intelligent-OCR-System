from ocr_engine import (
    extract_text_with_confidence
)

data = extract_text_with_confidence(
    "outputs/processed_image.png"
)

print(data)