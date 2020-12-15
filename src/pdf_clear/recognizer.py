import io

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTChar
from pdfminer.pdfpage import PDFPage


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                  password=password,
                                  caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)

    fp.close()
    device.close()
    text = retstr.getvalue()
    retstr.close()
    return text


def get_bold_italic_pos(pdf_path, page_number):
    resource_manager = PDFResourceManager()
    layout_params = LAParams()
    device = PDFPageAggregator(resource_manager, laparams=layout_params)
    pdf_file = open(pdf_path, 'rb')
    pdf_page_interpreter = PDFPageInterpreter(resource_manager, device)
    global actual_font_size_pt, actual_font_name

    bold = []
    italic = []

    for current_page_number, page in enumerate(PDFPage.get_pages(pdf_file)):
        if current_page_number == int(page_number) - 1:
            pdf_page_interpreter.process_page(page)
            layout = device.get_result()
            for textbox_element in layout:
                # if isinstance(textbox_element, LTTextBox):
                #     for line in textbox_element:
                #         word_from_textbox = line.get_text().strip()
                #         if word in word_from_textbox:
                #             for char in line:
                #                 ch = []
                #                 if isinstance(char, LTChar):
                #                     # convert pixels to points
                #                     actual_font_size_pt = int(char.size) * 72 / 96
                #                     # remove prefixed font name, such as QTBAAA+
                #                     actual_font_name = char.fontname[7:]
                #                     print(char)
                #                     ch.append(str(char.__repr__()))

                if isinstance(textbox_element, LTTextBox):
                    for line in textbox_element:
                        for char in line:

                            if isinstance(char, LTChar):
                                fontname = char.fontname
                                info = char.bbox
                                if 'Bold' in fontname:
                                    bold.append({'position': info})
                                elif 'Italic' in fontname:
                                    italic.append({'position': info})

    pdf_file.close()
    device.close()
    return {'bold': bold, 'italic': italic, 'page': page}


if __name__ == '__main__':
    path = 'doc_2.pdf'
    text = convert_pdf_to_txt(path)
    f = get_bold_italic_pos(path, 1)
    print(f['bold'])
    print(text)
