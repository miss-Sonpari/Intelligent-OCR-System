from validator import (
    validate_document_data
)

sample_data = {

    "email":
    "sakshi@gmail.com",

    "phone":
    "9876543210",

    "pan":
    "ABCDE1234F",

    "aadhaar":
    "123456789012",

    "gst":
    "27ABCDE1234F1Z5",

    "date":
    "15/06/2026"
}

result = validate_document_data(
    sample_data
)

print(result)