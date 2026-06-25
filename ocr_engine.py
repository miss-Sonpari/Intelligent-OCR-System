import easyocr
import os

# EasyOCR Reader Load
reader = easyocr.Reader(
    ['en'],
    gpu=False
)


def extract_text(image_path):
    """
    Extract text from image using EasyOCR
    """

    if not os.path.exists(image_path):
        raise FileNotFoundError(
            f"Image not found: {image_path}"
        )

    results = reader.readtext(
        image_path,
        detail=1
    )

    extracted_text = ""

    for result in results:

        bbox, text, confidence = result

        extracted_text += (
            text + "\n"
        )

    return extracted_text


def extract_text_with_confidence(
        image_path):
    """
    Return OCR text with confidence
    """

    results = reader.readtext(
        image_path,
        detail=1
    )

    data = []

    for result in results:

        bbox, text, confidence = result

        data.append({
            "text": text,
            "confidence":
            round(
                confidence,
                2
            )
        })

    return data