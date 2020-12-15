from tesserocr import PyTessBaseAPI, RIL, iterate_level, OEM, PSM


def get_words_info(image_path, tessdata_path):
    """
    get path to image and path to tessdata and return dict with info about each word
    """
    # api = PyTessBaseAPI(path=tessdata_path)
    words = []
    with PyTessBaseAPI(path=tessdata_path, oem=OEM.TESSERACT_ONLY, psm=10) as api:
        api.SetImageFile(image_path)
        words = api.GetWords()
        # api_ = PyTessBaseAPI(path=tessdata_path)

    result = []
    with PyTessBaseAPI(path=tessdata_path, oem=OEM.TESSERACT_ONLY, psm=13) as api:
        for word in words:
            # print(word[0])
            # print(type(word[0]))
            api.SetImage(word[0])
            # api.SetImageFile(image_path)
            # api.Recognize()
            text = api.GetUTF8Text()
            # words_ = api.GetWords()
            # print(word)
            print(text)
            # print(words_)
            api.Recognize()
            iter = api.GetIterator()
            level = RIL.WORD
            # # print(iter)
            # # rr = iter.WordFontAttributes()
            #
            for r in iterate_level(iter, level):
            #     # print(r)
            #     element = r.GetUTF8Text(level)
            #     # print(element)
                word_attributes = r.WordFontAttributes()
                print(word_attributes)
            #     base_line = r.BoundingBox(level)
            #
            #     if element:
            #         # print(element)
            #         word_attributes['word'] = element
            #         word_attributes['position'] = base_line
            #
            #     result.append(word_attributes)
    return result



if __name__ == '__main__':
    print("START")
    # api = PyTessBaseAPI(path='/home/andrei/my-space/prog/tessdata_2')
    result = get_words_info('page_1.png', 'tessdata')
    # for i in result:
    #     print(i['word'], ' - ', i['bold'], i['italic'], i['underlined'])
