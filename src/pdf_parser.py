from pdf2image import convert_from_path
import ghostscript
import locale


def pdf2jpeg(pdf_input_path, jpeg_output_path):
    args = ["pdf2jpeg",  # actual value doesn't matter
            "-dNOPAUSE",
            "-sDEVICE=jpeg",
            "-r400",
            "-sOutputFile=" + jpeg_output_path + 'page_%d.jpeg',
            pdf_input_path]

    encoding = locale.getpreferredencoding()
    args = [a.encode(encoding) for a in args]

    ghostscript.Ghostscript(*args)


def parse_pdf(path):
    """take a path to pdf-file and return .jpg images pages"""
    pages = convert_from_path(path, dpi=400, transparent=False, fmt='png')

    # Counter to store images of each page of PDF to image
    image_counter = 1

    # Iterate through all the pages stored above
    for page in pages:
        # Declaring filename for each page of PDF as JPG
        # For each page, filename will be:
        # PDF page 1 -> page_1.jpg
        # PDF page 2 -> page_2.jpg
        # PDF page 3 -> page_3.jpg
        # ....
        # PDF page n -> page_n.jpg
        filename = "page_" + str(image_counter) + ".png"

        # Save the image of the page in system
        page.save(filename, 'PNG')

        # Increment the counter to update filename
        image_counter = image_counter + 1


if __name__ == '__main__':
    print('START')
    # parse_pdf('docs/ex_2_vec.pdf')
    pdf2jpeg('docs/ex_2_vec.pdf', 'trsh/from_vector/')
