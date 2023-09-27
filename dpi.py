import argparse
import os

from PIL import Image


def batch_set_dpi(input_dir, dpi, start_number):
    input_folder = input_dir
    output_folder = f"{input_dir}_dpi_{dpi}"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [f for f in os.listdir(input_folder) if f.split(".")[-1].lower() in ["jpg", "jpeg", "png"]]
    total_images = len(image_files)
    processed_images = 0

    for file_name in image_files:
        input_path = os.path.join(input_folder, file_name)
        output_file_name = f"{start_number:03d}.jpg"
        output_path = os.path.join(output_folder, output_file_name)

        with Image.open(input_path) as img:
            img.save(output_path, format="JPEG", dpi=(dpi, dpi), quality=100)

        processed_images += 1
        start_number += 1
        progress = (processed_images / total_images) * 100
        print(f"Processed {processed_images}/{total_images} images ({progress:.2f}%).")


def main():
    parser = argparse.ArgumentParser(description="Batch set DPI of images in a folder.")
    parser.add_argument("dir", help="The input folder containing images.")
    parser.add_argument("--dpi", type=int, default=300, help="The target DPI value (default: 300)")
    parser.add_argument("--start_number", type=int, default=1, help="The starting number for output image filenames (default: 1)")

    args = parser.parse_args()

    batch_set_dpi(args.dir, args.dpi, args.start_number)


if __name__ == "__main__":
    main()
