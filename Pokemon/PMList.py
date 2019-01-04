from AllPokemons import *

class PMList(object):
    def __init__(self):
        self.pm_list=[]
    
    def Swap(self,a,b):
        self.pm_list[b],self.pm_list[a]=self.pm_list[a],self.pm_list[b]


    def append(self,pokemon):
        if len(self.pm_list)<=5:
            self.pm_list.append(pokemon)
            return True
        else:
            return False

    def print(self):
        for i,pokemon in enumerate(self.pm_list):
            print('['+str(i+1)+'] '+str(pokemon))