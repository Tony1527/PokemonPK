from pk_utility import *
from AllPokemons import *

class PMList(object):
    def __init__(self):
        self._pm_list=[]
        self.player=None

    def __len__(self):
        return len(self._pm_list)

    def __iter__(self):
        return self._pm_list.__iter__()
    
    def SetPlayer(self,player):
        self.player=player

    def FirstAlive(self):
        if len(self._pm_list)>=1:
            for pm in self._pm_list:
                if pm.hp>0:
                    return pm
        return None

    def ChoosePM(self,msg='指定'):
        while True:
            self.print()
            choice=input('请选择你要'+msg+'的宝可梦(输入0返回)：')
            choice=a2i(choice,0,len(self._pm_list))
            if choice==-1:
                return None
            elif choice<len(self._pm_list) and choice>=0:
                if ToBeSure('选择'+self._pm_list[choice].GetName()):
                    return self._pm_list[choice]
            else:
                pass
    def SwitchPM(self):
        while True:
            pokemon=self.ChoosePM('上场')
            if pokemon==None:
                return False
            if pokemon.hp==0:
                print(pokemon.GetName()+'已经处于濒死状态，无法上场战斗')
                continue
            idx=self._GetIdxOfPM(pokemon)
            if idx==0:
                print('所选的宝可梦已经在场上,请重新选择')
            else:
                self.player.Speak('下来吧'+self._pm_list[0].GetName())
                self.Swap(0,idx)
                return True

    def _GetIdxOfPM(self,pokemon):
        for i,x in enumerate(self._pm_list):
            if x == pokemon:
                return i
        raise ValueError('pokemon isn\'t found in pm_list')

    def Swap(self,a,b):
        self._pm_list[b],self._pm_list[a]=self._pm_list[a],self._pm_list[b]


    def append(self,pokemon):
        if len(self._pm_list)<=5:
            self._pm_list.append(pokemon)
            return True
        else:
            return False

    def print(self):
        for i,pokemon in enumerate(self._pm_list):
            print('['+str(i+1)+'] '+str(pokemon))

    
def SkillChoose(pokemon):
    print('===============')
    print('选择招式')
    while True:
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
                    print('该招式已经用完，请选择其他技能')
        else:
            pass