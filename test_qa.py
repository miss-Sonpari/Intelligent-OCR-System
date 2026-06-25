from qa_engine import ask_question

document_text = """
Name: Sakshi Shinde

Email: sakshi@gmail.com

Phone: 8530668610

Address: Pune Maharashtra
"""

question = (
    "What is the candidate email?"
)

answer = ask_question(
    document_text,
    question
)

print(answer)