import re


def extract_information(text):

    data = {
        "document_title": None,
        "name": None,
        "email": None,
        "phone": None,
        "date": None,
        "invoice_number": None,
        "total_amount": None,
        "address": None
    }

    # Email
    email = re.findall(
        r'[\w\.-]+@[\w\.-]+\.\w+',
        text
    )

    if email:
        data["email"] = email[0]

    # Phone
    phone = re.findall(
        r'\b\d{10}\b',
        text
    )

    if phone:
        data["phone"] = phone[0]

    # Date
    date = re.findall(
        r'\d{2}/\d{2}/\d{4}',
        text
    )

    if date:
        data["date"] = date[0]

    # Invoice Number
    invoice = re.findall(
        r'INV[- ]?\d+',
        text,
        re.IGNORECASE
    )

    if invoice:
        data["invoice_number"] = invoice[0]

    # Amount
    amount = re.findall(
        r'₹?\s?\d+(?:,\d+)*(?:\.\d+)?',
        text
    )

    if amount:
        data["total_amount"] = amount[-1]

    # Name
    lines = text.split("\n")

    for line in lines:

        if "name" in line.lower():

            parts = line.split(":")

            if len(parts) > 1:
                data["name"] = (
                    parts[1].strip()
                )

                break

    # Address
    for line in lines:

        if "address" in line.lower():

            parts = line.split(":")

            if len(parts) > 1:
                data["address"] = (
                    parts[1].strip()
                )

                break

    # Document Title
    if len(lines) > 0:
        data["document_title"] = (
            lines[0]
        )

    return data