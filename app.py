import streamlit as st
import os

from preprocess import preprocess_image
from ocr_engine import extract_text
from pdf_handler import pdf_to_images
from llm_engine import (
    correct_ocr_text
)
from classifier import (
    classify_document
)
from extractor import (
    extract_information
)
from validator import (
    validate_document_data
)
from qa_engine import (
    ask_question
)

st.set_page_config(
    page_title="Intelligent OCR System",
    layout="wide"
)

st.title(
    "📄 Intelligent OCR System"
)

uploaded_file = st.file_uploader(
    "Upload PDF or Image",
    type=[
        "pdf",
        "jpg",
        "jpeg",
        "png"
    ]
)

if uploaded_file:

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    file_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(
        file_path,
        "wb"
    ) as f:

        f.write(
            uploaded_file.getbuffer()
        )

    st.success(
        "File Uploaded Successfully"
    )

    full_text = ""

    # PDF Handling

    if uploaded_file.name.endswith(
        ".pdf"
    ):

        pages = pdf_to_images(
            file_path
        )

        for page in pages:

            processed = (
                preprocess_image(
                    page
                )
            )

            text = extract_text(
                processed
            )

            full_text += (
                text + "\n"
            )

    else:

        processed = (
            preprocess_image(
                file_path
            )
        )

        full_text = (
            extract_text(
                processed
            )
        )

    # OCR Output

    st.subheader(
        "Extracted OCR Text"
    )

    st.text_area(
        "",
        full_text,
        height=250
    )

    # OCR Correction

    corrected_text = (
        correct_ocr_text(
            full_text
        )
    )

    st.subheader(
        "Corrected Text"
    )

    st.text_area(
        "",
        corrected_text,
        height=250
    )

    # Classification

    classification = (
        classify_document(
            corrected_text
        )
    )

    st.subheader(
        "Document Type"
    )

    st.json(
        classification
    )

    # Information Extraction

    extracted_data = (
        extract_information(
            corrected_text
        )
    )

    st.subheader(
        "Extracted JSON"
    )

    st.json(
        extracted_data
    )

    # Validation

    validation_results = (
        validate_document_data(
            extracted_data
        )
    )

    st.subheader(
        "Validation Results"
    )

    st.json(
        validation_results
    )

    # Question Answering

    st.subheader(
        "Ask Question"
    )

    user_question = (
        st.text_input(
            "Enter Question"
        )
    )

    if st.button(
        "Get Answer"
    ):

        answer = ask_question(
            corrected_text,
            user_question
        )

        st.success(
            answer
        )