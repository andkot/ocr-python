import PyPDF2


pdfFileObj = open('pdf_clear/doc_2.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
t = pageObj.extractText()
print(t)