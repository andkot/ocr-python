from tesserocr import PyTessBaseAPI, RIL, iterate_level


def get_font(image_path):
    api = PyTessBaseAPI(path='/src/tessdata_2')
    # with PyTessBaseAPI(path='/home/my_data/tessdata') as api:
    api.SetImageFile(image_path)
    api.Recognize()
    iter = api.GetIterator()
    level = RIL.SYMBOL

    for r in iterate_level(iter, level):
        symbol = r.GetUTF8Text(level)
        word_attributes = r.WordFontAttributes()
        # a = PyResultIterator.WordFontAttributes()

        if symbol:
            # name = word_attributes['font_name']
            print(f'symbol {symbol}, font: {word_attributes}')



if __name__ == '__main__':
    print("START")
    # api = PyTessBaseAPI(path='/home/andrei/my-space/prog/tessdata_2')
    get_font('page_1.jpg')