from pdf_handler import pdf_to_images
from preprocess import preprocess_image
from ocr_engine import extract_text

pdf_file = "sample_docs/Sakshi_Shinde.pdf"

pages = pdf_to_images(
    pdf_file
)

full_text = ""

for page in pages:

    processed = preprocess_image(
        page
    )

    text = extract_text(
        processed
    )

    full_text += text + "\n"

print(full_text)