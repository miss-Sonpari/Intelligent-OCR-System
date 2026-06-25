import re
from datetime import datetime


def validate_email(email):

    if not email:
        return False

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return bool(
        re.match(
            pattern,
            email
        )
    )


def validate_phone(phone):

    if not phone:
        return False

    pattern = r'^[6-9]\d{9}$'

    return bool(
        re.match(
            pattern,
            phone
        )
    )


def validate_pan(pan):

    if not pan:
        return False

    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'

    return bool(
        re.match(
            pattern,
            pan
        )
    )


def validate_aadhaar(aadhaar):

    if not aadhaar:
        return False

    pattern = r'^\d{12}$'

    return bool(
        re.match(
            pattern,
            aadhaar
        )
    )


def validate_gst(gst):

    if not gst:
        return False

    pattern = (
        r'^[0-9]{2}'
        r'[A-Z]{5}'
        r'[0-9]{4}'
        r'[A-Z]{1}'
        r'[1-9A-Z]{1}'
        r'Z'
        r'[0-9A-Z]{1}$'
    )

    return bool(
        re.match(
            pattern,
            gst
        )
    )


def validate_date(date_text):

    if not date_text:
        return False

    formats = [
        "%d/%m/%Y",
        "%d-%m-%Y",
        "%Y-%m-%d"
    ]

    for fmt in formats:

        try:
            datetime.strptime(
                date_text,
                fmt
            )

            return True

        except:
            pass

    return False


def validate_document_data(data):

    results = {}

    results["email"] = (
        validate_email(
            data.get(
                "email"
            )
        )
    )

    results["phone"] = (
        validate_phone(
            data.get(
                "phone"
            )
        )
    )

    results["pan"] = (
        validate_pan(
            data.get(
                "pan"
            )
        )
    )

    results["aadhaar"] = (
        validate_aadhaar(
            data.get(
                "aadhaar"
            )
        )
    )

    results["gst"] = (
        validate_gst(
            data.get(
                "gst"
            )
        )
    )

    results["date"] = (
        validate_date(
            data.get(
                "date"
            )
        )
    )

    return results