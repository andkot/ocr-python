from pytesseract import pytesseract

tessdata_dir_config = '--tessdata-dir "./tessdata"'
pytesseract.run_tesseract('image.png', '__output__', lang=None, config='hocr', extension='box')

# def make_data(image_path, result):
#     pass
