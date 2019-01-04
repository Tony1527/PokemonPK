from ManipulatePM import *

class Medicine(object):
    def __init__(self,num=0):
        self.num=num

    def Use(self,pokemon):
        if self.num<=0:
            return False
        return self.UseImplement(pokemon)
    def UseImplement(self,pokemon):
        return True


class FullRestore(Medicine):
    def UseImplement(self,pokemon):
        recover_value,retstat = RecoverAll(pokemon)
        if recover_value==0 and retstat==False:
            print('使用痊愈药无效')
            return False
        else:
            print(pokemon.GetName()+'回复了全部HP且解除了所有异常状态')
            self.num=self.num-1
            return True
    def __str__(self):
        return '痊愈药 x '+str(self.num)+': 回复全部HP且解除所有异常状态'

class FullHeal(Medicine):
    def UseImplement(self,pokemon):
        retstat = RecoverStatusCond(pokemon)
        if retstat==False:
            print('使用万灵药无效')
            return False
        else:
            print(pokemon.GetName()+'异常状态解除了')
            self.num=self.num-1
            return True
    def __str__(self):
        return '万灵药 x '+str(self.num)+': 解除所有异常状态'
class MaxPotion(Medicine):
    def UseImplement(self,pokemon):
        recover_value = RecoverAllHP(pokemon)
        if recover_value==0 :
            print('使用全满药无效')
            return False
        else:
            print(pokemon.GetName()+'回复了全部HP')
            self.num=self.num-1
            return True
    def __str__(self):
        return '全满药 x '+str(self.num)+': 回复所有HP'


class Revive(Medicine):
    def UseImplement(self,pokemon):
        if pokemon.hp!=0:
            print('使用活力碎片无效')
            return False
        else:
            recover_value = RecoverHP(pokemon,pokemon.HP()*0.5)
            print(pokemon.GetName()+'从濒死状态复苏了')
            self.num=self.num-1
            return True
    def __str__(self):
        return '活力碎片 x '+str(self.num)+': 复苏濒死状态的宝可梦，且回复一半HP'


class MaxRevive(Medicine):
    def UseImplement(self,pokemon):
        if pokemon.hp!=0:
            print('使用活力块无效')
            return False
        else:
            recover_value = RecoverAllHP(pokemon)
            print(pokemon.GetName()+'从濒死状态复苏了')
            self.num=self.num-1
            return True
    def __str__(self):
        return '活力块 x '+str(self.num)+': 复苏濒死状态的宝可梦，且回复所有HP'