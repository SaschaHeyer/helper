from PIL import Image
import os

def convert_webp_to_png(input_folder, output_folder):
    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Iterate over all files in the input directory
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.webp'):
            # Open the webp image
            webp_image_path = os.path.join(input_folder, filename)
            with Image.open(webp_image_path) as img:
                # Define the output path
                png_image_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.png")
                # Save as PNG
                img.save(png_image_path, 'PNG')
            print(f"Converted {filename} to {os.path.basename(png_image_path)}")

if __name__ == "__main__":
    input_folder = '/Users/sascha/Desktop/development/image-similarity-search/products'  # Replace with the path to your input folder containing WebP images
    output_folder = '/Users/sascha/Desktop/development/image-similarity-search/products/png'  # Replace with the path to your desired output folder for PNG images
    convert_webp_to_png(input_folder, output_folder)
