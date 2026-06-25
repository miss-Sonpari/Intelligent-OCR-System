from llm_engine import generate_response


def ask_question(document_text, question):

    prompt = f"""
You are a document assistant.

Document Content:
{document_text}

Question:
{question}

Answer the question only using
the document content.

If answer is not present,
reply:
"Information not found in document."
"""

    response = generate_response(
        prompt
    )

    return response