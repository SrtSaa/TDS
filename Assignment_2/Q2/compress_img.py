import os
from PIL import Image

def compress_to_target_size(input_image_path, output_image_path):
    img = Image.open(input_image_path)
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    img.save(output_image_path, 'JPEG', quality=10, optimize=True)

if __name__ == "__main__":
    INPUT_IMAGE = "boxes.png"
    OUTPUT_IMAGE = "boxes_compressed.png"

    compress_to_target_size(INPUT_IMAGE, OUTPUT_IMAGE)
