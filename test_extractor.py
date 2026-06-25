from extractor import extract_information

sample_text = """
Resume

Name: Sakshi Shinde

Email: sakshi@gmail.com

Phone: 8530668610

Date: 15/06/2026

Address: Pune Maharashtra
"""

data = extract_information(
    sample_text
)

print(data)