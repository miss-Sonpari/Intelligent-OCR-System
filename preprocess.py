import cv2
import numpy as np
import os


def deskew_image(image):
    """
    Deskew image if tilted
    """

    coords = np.column_stack(np.where(image > 0))

    if len(coords) == 0:
        return image

    angle = cv2.minAreaRect(coords)[-1]

    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    (h, w) = image.shape[:2]

    center = (w // 2, h // 2)

    matrix = cv2.getRotationMatrix2D(
        center,
        angle,
        1.0
    )

    rotated = cv2.warpAffine(
        image,
        matrix,
        (w, h),
        flags=cv2.INTER_CUBIC,
        borderMode=cv2.BORDER_REPLICATE
    )

    return rotated


def preprocess_image(image_path):
    """
    Complete OCR preprocessing pipeline
    """

    # Check file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(
            f"Image not found: {image_path}"
        )

    # Read image
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(
            "Unable to read image"
        )

    # Create output folder
    os.makedirs(
        "outputs",
        exist_ok=True
    )

    # Step 1 - Grayscale
    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    # Step 2 - Noise Removal
    denoised = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )

    # Step 3 - Thresholding
    thresh = cv2.threshold(
        denoised,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    # Step 4 - Deskew
    deskewed = deskew_image(
        thresh
    )

    # Step 5 - Morphological Cleanup
    kernel = np.ones(
        (1, 1),
        np.uint8
    )

    cleaned = cv2.morphologyEx(
        deskewed,
        cv2.MORPH_CLOSE,
        kernel
    )

    # Save processed image
    processed_path = (
        "outputs/processed_image.png"
    )

    cv2.imwrite(
        processed_path,
        cleaned
    )

    return processed_path