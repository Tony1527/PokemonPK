from pk_utility import *
from Medicine import *

class Package(Singleton):
    def __init__(self):
        self.medicines=[]
        self.player=None
    
    def Open(self,pokemon_list):
        Console.msg('打开背包')
        while True:
            self.print()
            choice=input('请选择你要使用的药剂(输入0返回)：')
            choice=a2i(choice,0,len(self.medicines))
            if choice==-1:
                return False
            elif choice<len(self.medicines) and choice>=0:
                if self.UseItem(choice,pokemon_list):
                    return True
            else:
                pass
    def SetPlayer(self,player):
        self.player=player
    
    def UseItem(self,idx,pokemon_list):
        while True:
            pokemon=pokemon_list.ChoosePM('对其使用'+self.medicines[idx].GetName())
            #没用药
            if pokemon==None:
                return False
            #用了药
            elif self.medicines[idx].Use(pokemon):
                if self.medicines[idx].num==0:
                    self.medicines.pop(idx)
                return True
            

    def append(self,medicine):
        if medicine.num!=0:
            self.medicines.append(medicine)

    def print(self):
        for i,medicine in enumerate(self.medicines):
            print('['+str(i+1)+'] '+str(medicine))