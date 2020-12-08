from tesserocr import PyTessBaseAPI, RIL, iterate_level, iterate_choices
from tesserocr import PyResultIterator


def get_font(image_path):
    with PyTessBaseAPI() as api:
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
    get_font('page_1.jpg')