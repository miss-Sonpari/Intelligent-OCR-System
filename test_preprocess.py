from preprocess import preprocess_image

image_path = "sample_docs/12.jpg"

processed_image = preprocess_image(
    image_path
)

print(
    "Processed Image Saved At:",
    processed_image
)