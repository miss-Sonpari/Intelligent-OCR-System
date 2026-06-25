from pdf_handler import pdf_to_images

pdf_file = "sample_docs/Sakshi_Shinde.pdf"

images = pdf_to_images(
    pdf_file
)

for image in images:
    print(image)