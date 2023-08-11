import PyPDF2

pdf_file = open('FMC_SparkDeveloper.pdf', 'rb')

reader = PyPDF2.PdfReader(pdf_file)

page_number = reader.pages[0]

text = page_number.extract_text()

print(text)