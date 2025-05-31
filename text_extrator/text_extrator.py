# Code for to extract the most important information and save as .txt file
import PyPDF2


# Open PDF file on binary mode
pdf_file = open('YOUR_FILE.pdf', 'rb')

# Read to memory
reader = PyPDF2.PdfReader(pdf_file)

# Select first page
page_number = reader.pages[0]

# Extract the text.
text = page_number.extract_text()

# Selecting the most important information 
selecteds = text[2:300]

# Check the strings
print(selecteds)

# Path to save
path_1 = "C:/Users/ YOUR_FOLDER /Desktop/my_output.txt"

# Try write the content to .txt file
try:
    with open(path_1, "w") as file:
        file.write(selecteds)
    print("Content saved with success!")

except Exception as err:
    print(err)