import PyPDF2


pdf_file = open('MyDP900.pdf', 'rb')

reader = PyPDF2.PdfReader(pdf_file)

page_number = reader.pages[0]

text = page_number.extract_text()
lines = text.split('\n')
selecteds = lines[1:11]

print(selecteds)

path = "YOUR PATH"

with open(path, "w") as arquivo:
    arquivo.write(text)

print("Content saved with success!")