from tesserocr import PyTessBaseAPI, RIL, iterate_level, OEM, PSM


def get_words_info(image_path, tessdata_path):
    """
    get path to image and path to tessdata and return dict with info about each word
    """
    # api = PyTessBaseAPI(path=tessdata_path)
    with PyTessBaseAPI(path=tessdata_path, oem=OEM.TESSERACT_LSTM_COMBINED, psm=PSM.AUTO) as api:
        api.SetImageFile(image_path)
        # api.ProcessPages()
        api.Recognize()
        #
        # hocr = api.GetHOCRText(1)
        # print(hocr)
        iter = api.GetIterator()
        level = RIL.WORD
        result = []


        for r in iterate_level(iter, level):
            element = r.GetUTF8Text(level)
            # word_attributes = r.WordFontAttributes()
            word_attributes = {}

            atr = r.WordFontAttributes()
            # print(atr['bold'])
            # print(element)

            if element:
                word_attributes['word'] = element
                base_line = r.BoundingBox(level)
                word_attributes['position'] = base_line
                result.append(word_attributes)

        return result

# def make_text_from_words



if __name__ == '__main__':
    print("START")
    # api = PyTessBaseAPI(path='/home/andrei/my-space/prog/tessdata_2')
    result = get_words_info('page_1.png', 'tessdata')
    # print(result)
    for i in result:
        # print(i['word'], ' - ', i['bold'], i['italic'], i['underlined'])
        print(i['word'], i['position'])
