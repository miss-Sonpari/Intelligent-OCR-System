import ssl

ssl._create_default_https_context = (
    ssl._create_unverified_context
)
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    pipeline
)

import torch

MODEL_NAME = (
    "microsoft/Phi-3-mini-4k-instruct"
)

print("Loading Phi-3 Model...")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype="auto",
    device_map="auto",
    trust_remote_code=True
)

generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer
)


def generate_response(prompt):

    response = generator(
        prompt,
        max_new_tokens=300,
        do_sample=False
    )

    return response[0]["generated_text"]


def correct_ocr_text(text):

    prompt = f"""
Correct OCR mistakes from the text below.

Text:
{text}

Return only corrected text.
"""

    return generate_response(
        prompt
    )


def classify_document_llm(text):

    prompt = f"""
Classify document into one category:

Invoice
Receipt
Resume
Aadhaar Card
PAN Card
Driving License
Passport
Bank Statement
Other

Document Text:
{text}

Return only category name.
"""

    return generate_response(
        prompt
    )


def extract_json(text):

    prompt = f"""
Extract information from document.

Return JSON only.

Fields:

Document Title
Name
Date
Email
Phone
Address
Invoice Number
Total Amount

Document Text:

{text}
"""

    return generate_response(
        prompt
    )