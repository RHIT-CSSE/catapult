import threading
from winsound import Beep
import random

class Beeper(threading.Thread):
    def run(self):
        sauce = 'a'
        #for i in range(25):
            #Beep(random.randint(200,600),50)