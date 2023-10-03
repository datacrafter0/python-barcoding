# python-barcoding

    generate_qr:
    This function takes a list of data as input and generates corresponding barcodes. 
    It returns a list of barcode images. These images can be saved or further processed as needed.

    insert_qr_to_pictures:
    This function inserts the generated barcodes into images in batches. 
    It takes a list of barcode images and a list of file paths for the target images. After execution,
    the images will have the respective barcodes embedded. When the barcodes are scanned,
    they will open the associated image's URL.
