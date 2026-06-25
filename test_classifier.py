from classifier import classify_document

sample_text = """
Name : Sakshi Patil

Skills :
Python
Machine Learning

Education :
B.E AI & DS
"""

result = classify_document(
    sample_text
)

print(result)