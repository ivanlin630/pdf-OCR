import os
import pytesseract

image_dir = './image'
output_dir = './output'
for filename in os.listdir(image_dir):
    img_path = os.path.join(image_dir, filename)
    print(pytesseract.image_to_string(img_path))
    text = pytesseract.image_to_string(img_path)
    with open(os.path.join(output_dir, filename.replace('.jpg', '.txt')), 'w', encoding='utf-8') as f:
        f.write(text)
