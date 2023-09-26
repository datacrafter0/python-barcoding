import os
import cv2
from PIL import Image

# Photos directory
photos_directory = "C:/Personnel/Barcodes/unsplash/photos"
barcodes_directory = "C:/Personnel/Barcodes/unsplash/qr_output/"

# Output directory for photos with superimposed barcodes
output_directory = "C:/Personnel/Barcodes/unsplash/photos_with_barcode"

# List photo files
for photo_filename in os.listdir(photos_directory):
    if photo_filename.endswith(".jpg"):  # Adjust the extension according to the image type
        # Extract the identifier from the photo filename
        identifier = photo_filename.split('.')[0] # Assuming a format "photo_identifier.jpg"

        # Open the photo and the barcode using PIL (Pillow)
        photo_filename = photos_directory + "/" + identifier + ".jpg"

        photo = Image.open(photo_filename)

        try:
            if os.path.exists(barcodes_directory + identifier + ".png"):
                barcode = Image.open(barcodes_directory + identifier + ".png")

                # Resize the barcode
                # barcode = barcode.resize((159, 159), Image.Resampling.NEAREST)  # , Image.ANTIALIAS)

                # Ensure that the photo size remains unchanged when superimposing
                photo.thumbnail(photo.size)

                # Paste the barcode in the bottom-right corner of the photo
                # photo.paste(barcode, (photo.width - barcode.width, photo.height - barcode.height), barcode)
                photo.paste(barcode, (photo.width - barcode.width, photo.height - barcode.height),
                            barcode if barcode.mode == 'RGBA' else None)

                # Save the resulting photo in the output directory
                output_path = os.path.join(output_directory, identifier + ".jpg")
                photo.save(output_path)

            else:
                print(f"The file {photo_filename} does not exist. Skipping...")
        except Exception as e:
            print(f"An error occurred while opening the image {photo_filename}: {str(e)}")
