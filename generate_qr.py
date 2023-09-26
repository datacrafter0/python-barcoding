import os
import qrcode

# Ouput folder for barcodes
output_folder = "C:/Personnel/Barcodes/unsplash/qr_output"

# Create a output_folder if it not exists
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# read the data
with open("C:/Personnel/Barcodes/unsplash/unsplash-photos-list.txt", "r") as file:
    photoNamesList = file.readlines()

for photoName in photoNamesList:
    # Divide in name and url
    parts = photoName.strip().split(',')
    if len(parts) != 2:
        print(f"Incorrect format in: {photoName}")
        continue  # Next

    name, url = map(str.strip, parts)

    # Create QR
    qr = qrcode.QRCode(
        version = 1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )
    qr.add_data(url)
    qr.make(fit = True)

    # Generate barcode QR as image
    qr_img = qr.make_image(fill_color = "purple", back_color = "white")

    # Nombre del archivo con el nombre especificado en la lista
    fileName = f"{output_folder}/{name}.png"

    # Guardar la imagen del código QR
    qr_img.save(fileName)
    print(f"QR for '{name}' saved in: {fileName}")
