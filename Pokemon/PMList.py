from pk_utility import *
from AllPokemons import *
from AllSkills import *

class PMList(object):
    def __init__(self):
        self._pm_list=[]
        self.player=None

    def __len__(self):
        return len(self._pm_list)

    def __iter__(self):
        return self._pm_list.__iter__()
    
    def __getitem__(self,idx):
        return self._pm_list[idx]
    
    def SetPlayer(self,player):
        self.player=player

    def FirstAlive(self):
        if len(self._pm_list)>=1:
            for pm in self._pm_list:
                if pm.IsAlive():
                    return pm
        return None

    def LastAlive(self):
        if len(self._pm_list)>=1:
            for i in range(len(self._pm_list)-1,-1,-1):
                if self._pm_list[i].IsAlive():
                    return self._pm_list[i]
        return None

    def Front(self):
        return self._pm_list[0]

    def ChoosePM(self,msg='指定'):
        while True:
            self.print()
            choice=input('请选择你要'+msg+'的宝可梦(输入0返回)：')
            choice=a2i(choice,0,len(self._pm_list))
            if choice==-1:
                return None
            elif choice<len(self._pm_list) and choice>=0:
                pokemon=self._DisplayPMMenu(choice)
                if pokemon!=None:
                    return pokemon
            else:
                pass
    def _DisplayPMMenu(self,idx):
        while True:
            print('==========')
            print('1.技能信息')
            print('2.选择')
            choice=input('宝可梦菜单(输入0返回)：')
            choice=a2i(choice,0,2)
            if choice==-1:
                return None
            elif choice==0:
                self._pm_list[idx].PrintSkills()
                pass
            elif choice==1:
                if ToBeSure('选择'+self._pm_list[choice].GetName()):
                    return self._pm_list[idx]
                else:
                    pass
            else:
                pass
    def SwitchPM(self):
        while True:
            pokemon=self.ChoosePM('上场')
            if pokemon==None:
                return False
            if pokemon.hp==0:
                Console.msg(pokemon.GetName()+'已经处于濒死状态，无法上场战斗')
                continue
            idx=self._GetIdxOfPM(pokemon)
            if idx==0:
                Console.msg('所选的宝可梦已经在场上,请重新选择')
            else:
                self.player.Speak('下来吧'+self._pm_list[0].GetName())
                self.Swap(0,idx)
                return True

    def _GetIdxOfPM(self,pokemon):
        for i,x in enumerate(self._pm_list):
            if x == pokemon:
                return i
        raise ValueError('pokemon isn\'t found in pm_list')

    def Choose(self,pokemon):
        idx=self._GetIdxOfPM(pokemon)
        if idx!=0:
            self.Swap(0,idx)
        

    def Swap(self,a,b):
        self._pm_list[a].special_cond.Clear()
        self._pm_list[b],self._pm_list[a]=self._pm_list[a],self._pm_list[b]


    def append(self,pokemon):
        if len(self._pm_list)<=5:
            self._pm_list.append(pokemon)
            return True
        else:
            return False

    def print(self):
        Console.refresh(is_clean_total=True)
        for i,pokemon in enumerate(self._pm_list):
            print('['+str(i+1)+'] '+str(pokemon))

    
def SkillChoose(pokemon):
    Console.msg('选择招式')
    while True:
        Console.refresh(is_clean_total=True)
        pokemon.PrintSkills()
        choice=input('请选择你要使用的技能(输入0返回)：')
        choice=a2i(choice,0,len(pokemon.skills))
        if choice==-1:
            return None
        elif choice<len(pokemon.skills) and choice>=0:
            if pokemon.skills[choice].pp>0:
                return pokemon.skills[choice]
            else:
                struggle_flag=True
                for skill in pokemon.skills:
                    if skill.pp>0:
                        struggle_flag=False
                        break
                if struggle_flag:
                    return Struggle()
                else:
                    Console.msg('该招式已经用完，请选择其他技能')
        else:
            pass