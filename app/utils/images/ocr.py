from pathlib import Path

OCR_IMAGE_PATH = Path("images/user-content/ocr")
OCR_IMAGE_PATH.mkdir(parents=True, exist_ok=True)

OCR_SEGMENTATION_IMAGE_PATH = Path("images/ml/ocr/segmentation")
OCR_SEGMENTATION_IMAGE_PATH.mkdir(parents=True, exist_ok=True)

OCR_CROPPED_IMAGE_PATH = Path("images/ml/ocr/cropped")
OCR_CROPPED_IMAGE_PATH.mkdir(parents=True, exist_ok=True)
