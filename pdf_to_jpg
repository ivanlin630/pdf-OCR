import os
from pdf2image import convert_from_path

PDF_dir = './PDF'
output_dir = './image'

for filename in os.listdir(PDF_dir):
    pages = convert_from_path(os.path.join(PDF_dir, filename))
    for i in range(len(pages)):
        pages[i].save(filename+ str(i) +'.jpg', 'JPEG')
