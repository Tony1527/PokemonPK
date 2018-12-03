import numpy as np
from pk_utility import *
class PokemonBase(object):
    hp=0
    attack=0
    defense=0
    special_attack=0
    special_defense=0
    speed=0
    level=0
    _skills=[]
    _type=None
    _name=''

    def __init__(self,level=5,hp=39,attack=52,defense=43,special_attack=60,special_defense=50,speed=65,type=TypeEnum.NORMAL,name='???'):
        self.hp=hp
        self.attack=attack
        self.defense=defense
        self.specialattack=special_attack
        self.special_defense=special_defense
        self.speed=speed
        self.level = level
        self._type=type
        self._name=name
    

    #学习技能
    def LearnSkills(self,skills=[]):
        for skill in skills:
            print('you have learned',skill)

            #如果技能数小于4，直接学会技能，否则需要进行学习判断
            if len(self._skills)<4:
                self._skills.append(skill)
            else:
                is_finished=False
                while not is_finished:
                    print('your skills are full. If you want to learn more skills, please forget one skill first.')
                    self._skills.append(skill)
                    self.PrintSkills()
                    choose = input('your choice:')
                    choose_idx = g_d5i[choose]
                    if ToBeSure('forget '+self._skills[choose_idx]):
                        print('You have forgotten',self._skills[choose_idx])
                        if choose_idx<=3:
                            print('And learned',skill)
                            self._skills[choose_idx]=skill
                        
                        self._skills.pop()
                        is_finished=True
                        
                    else:
                        self._skills.pop()
                        is_finished=False

                
        self.PrintSkills()

    #打印所有技能
    def PrintSkills(self):
        for i,skill in enumerate(self._skills):
            print(i+1,skill.GetName())
            skill.Print()
            print('')
    def GetType(self):
        return self._type

    def GetName(self):
        return self._name

    def SetName(self,name):
        self._name = name


# k = PokemonBase()
# k.LearnSkills(['撞击','火苗','叫声','摇尾','抓'])