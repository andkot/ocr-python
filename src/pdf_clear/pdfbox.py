from PDFContentConverter import PDFContentConverter

pdf = 'doc_2.pdf'

converter = PDFContentConverter(pdf)

result = converter.pdf2pandas()
r = result.to_dict()
print(r)
b = converter.get_media_boxes()
print(b)