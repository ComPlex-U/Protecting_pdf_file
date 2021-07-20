from PyPDF2 import PdfFileWriter, PdfFileReader

def pdf_secure(file, password):
    parser =PdfFileWriter()
    pdf = PdfFileReader(file)
    for page in range(pdf.numPages):
        parser.addPage(pdf.getPage(page))
    parser.encrypt(password)
    with open(f"Protect_{file}", "wb")as f:
        parser.write(f)
        f.close()
        print(f"Feito {file} Created..")
if __name__== "__main__":
    file = input('PDF a encriptar: ')
    password = input('Enter the Password: ')
    print('Starting scan on host: ', password)
    # password = "bala"
    pdf_secure(file, password)