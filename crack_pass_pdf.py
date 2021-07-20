import pikepdf
from tqdm import tqdm

wordlist = input('Enter the Password Wordlist: ')
pdf = input('Enter the pdf: ')
passwrd= [line.strip() for line in open(wordlist)]
for password in tqdm (passwrd, ""):
    try:
        with pikepdf.open(pdf, password=password) as pdf:
            print("\n [+] password encontrada:", password)
            break
    except pikepdf._qpdf.PasswordError as e:
        continue
