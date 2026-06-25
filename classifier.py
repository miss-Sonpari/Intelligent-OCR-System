def classify_document(text):

    text = text.lower()

    # Resume
    if (
        "skills" in text or
        "education" in text or
        "experience" in text
    ):
        return {
            "document_type": "Resume",
            "confidence": 0.95
        }

    # Aadhaar
    elif (
        "aadhaar" in text or
        "government of india" in text
    ):
        return {
            "document_type": "Aadhaar Card",
            "confidence": 0.98
        }

    # PAN
    elif (
        "income tax department" in text or
        "permanent account number" in text
    ):
        return {
            "document_type": "PAN Card",
            "confidence": 0.97
        }

    # Passport
    elif (
        "passport" in text or
        "republic of india" in text
    ):
        return {
            "document_type": "Passport",
            "confidence": 0.96
        }

    # Driving License
    elif (
        "driving licence" in text or
        "driving license" in text
    ):
        return {
            "document_type": "Driving License",
            "confidence": 0.95
        }

    # Invoice
    elif (
        "invoice number" in text or
        "invoice" in text or
        "gst" in text
    ):
        return {
            "document_type": "Invoice",
            "confidence": 0.94
        }

    # Receipt
    elif (
        "receipt" in text
    ):
        return {
            "document_type": "Receipt",
            "confidence": 0.93
        }

    # Bank Statement
    elif (
        "account number" in text or
        "bank statement" in text or
        "transaction" in text
    ):
        return {
            "document_type": "Bank Statement",
            "confidence": 0.92
        }

    else:
        return {
            "document_type": "Other",
            "confidence": 0.50
        }