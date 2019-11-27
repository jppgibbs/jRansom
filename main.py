import os
import base64
from caesarCipher import *
from reverseCipher import *
from vigenereCipher import *

def encrypt():
    for root, dirs, files in os.walk('/'):
        for file in files:
            if file.endswith('.test1337'):
                print(os.path.join(root, file))
                f = open(os.path.join(root, file),"rb+")
                contents = f.read()
                print(contents)
                contents = contents.encode("base64")
                print(contents)
                contents += "=" * ((4 - len(contents) % 4) % 4)
                print(contents)
                contents = caesartranslate(contents, 3, "encrypt")
                print(contents)
                contents = reverse(contents)
                print(contents)
                contents = vtranslate(contents, "ASIMOV", "encrypt")
                print(contents)
                f.seek(0)
                f.write(contents)
                f.close()

def decrypt():
    for root, dirs, files in os.walk('/'):
        for file in files:
            if file.endswith('.test1337'):
                print(os.path.join(root, file))
                f = open(os.path.join(root, file),"r+")
                contents = f.read()
                print(contents)
                contents = vtranslate(contents, "ASIMOV", "decrypt")
                print(contents)
                contents = reverse(contents)
                print(contents)
                contents = caesartranslate(contents, 3, "decrypt")
                print(contents)
                contents = base64.b64decode(contents)
                print(contents)
                f.seek(0)
                f.write(contents)
                f.close()

decrypt()