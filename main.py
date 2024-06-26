import os
from pdf2image import convert_from_path

# Add your own FULL file path and output directory
def pdf_to_img(file_path=r"D:\pdf_to_img\cheatsheet.pdf", output_dir=r"D:\pdf_to_img\output"):
    try:
        os.makedirs(output_dir, exist_ok=True)
        print("Starting PDF to image conversion...")
        pages = convert_from_path(file_path, 500, poppler_path=r'C:\Program Files\poppler-24.02.0\Library\bin')
        print(f"Number of pages converted: {len(pages)}")
        
        for i, page in enumerate(pages):
            output_path = os.path.join(output_dir, f'page_{i}.jpg')
            print(f"Saving page {i} to {output_path}")
            page.save(output_path, 'JPEG')
        print("Conversion completed successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

pdf_to_img("D:\pdf_to_img\invoice.pdf")
