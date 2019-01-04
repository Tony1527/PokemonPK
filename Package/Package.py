from pk_utility import *
from Medicine import *

class Package(Singleton):
    def __init__(self):
        self.medicines=[]
    
    def Open(self,pokemon_list):
        close_flag=False
        while not close_flag:
            self.print()
            choice=input('请选择你要使用的药剂(输入0退出背包)：')
            if choice==0:
                close_flag=True
            elif choice<=len(self.medicines) and choice>0:
                self.UseItem(choice,pokemon_list)
            else:
                pass
    
    def UseItem(self,idx,pokemon_list):
        if self.medicines[idx].Use(pokemon):
            pass
            if self.medicines[idx].num==0:
                self.medicines.pop(idx)

    def append(self,medicine):
        if medicine.num!=0:
            self.medicines.append(medicine)

    def print(self):
        for i,medicine in enumerate(self.medicines):
            print('['+str(i+1)+'] '+str(medicine))