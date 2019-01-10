from pk_utility import *
from Console import *

class Player(object):
    def __init__(self,name):
        self._name=name
        self._fighting=[]
        self._defeating=[]
    def Speak(self,msg):
        Console.msg(self._name+" : "+msg)
    def SetMockingSentences(self,fighting=[],defeating=[]):
        self._fighting=fighting
        self._defeating=defeating
    def MockingOnFighting(self,percent=1):
        if np.random.rand()<percent:
            self.Speak(self._fighting[np.random.randint(len(self._fighting))])
    def MockingOnDefeating(self,percent=1):
        if np.random.rand()<percent:
            self.Speak(self._fighting[np.random.randint(len(self._fighting))])