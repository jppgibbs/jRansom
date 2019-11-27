import os
from caesarCipher import *
from reverseCipher import *
from vigenereCipher import *

for root, dirs, files in os.walk('/root'):
       for file in files:
           if file.endswith('.test1337'):
            print(os.path.join(root, file))
