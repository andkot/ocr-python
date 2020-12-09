from tesserocr import PyTessBaseAPI, RIL, iterate_level


def get_words_info(image_path, tessdata_path):
    # api = PyTessBaseAPI(path=tessdata_path)
    with PyTessBaseAPI(path=tessdata_path) as api:
        api.SetImageFile(image_path)
        api.Recognize()
        iter = api.GetIterator()
        level = RIL.WORD

        for r in iterate_level(iter, level):
            element = r.GetUTF8Text(level)
            word_attributes = r.WordFontAttributes()
            base_line = r.BoundingBox(level)

            if element:
                print(f'symbol {element}, font: {word_attributes}')
                print(f'baseline: {base_line}')


if __name__ == '__main__':
    print("START")
    # api = PyTessBaseAPI(path='/home/andrei/my-space/prog/tessdata_2')
    get_words_info('/src/docs/doc_1.png', '/src/tessdata/')
