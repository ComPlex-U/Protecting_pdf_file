from PyPDF2 import PdfFileWriter, PdfFileReader

def pdf_secure(file, password):
    parser =PdfFileWriter()
    pdf = PdfFileReader(file)
    for page in range(pdf.numPages):
        parser.addPage(pdf.getPage(page))
    parser.encrypt(password)
    with open(f"Feito_{file}", "wb")as f:
        parser.write(f)
        f.close()
        print(f"feito_{file} Created..")
if __name__== "__main__":
    file = "MESI-2021-FC-Av.pdf"
    password = input('Enter the Password: ')
    print('Starting scan on host: ', password)
    # password = "bala"
    pdf_secure(file, password)