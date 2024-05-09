import os
import cv2
from PIL import Image 
import pytesseract as pt






test_img_path = "../test images/"
create_path = lambda f : os.path.join(test_img_path, f)

test_image_files = os.listdir(test_img_path)

for f in test_image_files:
    print(f)







def show_image(img_path, size=(500, 500)):
    image = cv2.imread(img_path)
    image = cv2.resize(image, size)
    
    cv2.imshow("IMAGE", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()





pt.pytesseract.tesseract_cmd = r"C:\Users\ASUS\Downloads\tesseract-ocr-w64-setup-5.3.3.20231005.exe"





avb_langs = pt.get_languages(config='')
for lang in avb_langs:
    print(lang)




image_path = test_image_files[12] 
path = create_path(image_path)

image = Image.open(path)
text = pt.image_to_string(image)

print(text)
show_image(path)





path = create_path("hin-text-2.jpg")

image = Image.open(path)
text = pt.image_to_string(image, lang='hin')

print(text)
show_image(path)





img_name_txt_file = "../paper/image-paths.txt"
text = pt.image_to_string(img_name_txt_file, lang='jpn')

print(text)




path = create_path("article.jpg")

image = Image.open(path)
text = 'NO TEXT TO BE APPEARED'

try:
    text = pt.image_to_string(image, lang='eng', timeout=5)
except RuntimeError as timeout_error:
    print("[TIMEOUT ERROR]")

print(text)
show_image(path)





path = create_path("paper.jpg")

image = Image.open(path)
bound_rects = pt.image_to_boxes(image, lang='jpn')

print(bound_rects)
show_image(path)





img = cv2.imread(path)
h, _, _ = img.shape

for b in bound_rects.splitlines():
    b = b.strip().split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow("CHARACTERIZED IMAGE", img)
cv2.waitKey(0)
cv2.destroyAllWindows()





image_path = test_image_files[2]
path = create_path(image_path)

image = Image.open(path)
text = pt.image_to_data(image)

print(text)
show_image(path)





image_path = "paper.jpg" 
path = create_path(image_path)

print(pt.image_to_osd(path, lang='hin'))





image_path = "article.jpg"
path = create_path(image_path)
file_save_path = "../files/"




image_path = "article.jpg"
path = create_path(image_path)
file_save_path = "../files/"




hocr = pt.image_to_pdf_or_hocr(path, extension='hocr')

file = open(os.path.join(file_save_path, "hocr-content.html"), 'w+b')
file.write(hocr)
file.close()





xml = pt.image_to_alto_xml(path)

file = open(os.path.join(file_save_path, "xml-content.xml"), 'w+b')
file.write(xml)
file.close()