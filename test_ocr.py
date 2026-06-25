from preprocess import preprocess_image
from ocr_engine import extract_text

image_path = "sample_docs/12.jpg"

processed = preprocess_image(
    image_path
)

text = extract_text(
    processed
)

print(text)