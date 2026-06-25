from llm_engine import (
    correct_ocr_text,
    classify_document_llm,
    extract_json
)

sample_text = """
Narne: Sakshi Patil
Ernail: sakshi@gmail.com
Ph0ne: 9876543210
"""

corrected = correct_ocr_text(
    sample_text
)

print(
    "Corrected Text:"
)

print(corrected)

doc_type = classify_document_llm(
    corrected
)

print(
    "Document Type:"
)

print(doc_type)

json_output = extract_json(
    corrected
)

print(
    "JSON Output:"
)

print(json_output)