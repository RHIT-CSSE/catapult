import threading
from winsound import Beep
import random

class APBeeper(threading.Thread):
    
    def __init__(self,freq,dur):
        threading.Thread.__init__(self)
        self.freq = freq
        self.dur = dur
    
    def run(self):
        Beep(self.freq,self.dur)