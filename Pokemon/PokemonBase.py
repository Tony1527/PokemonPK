import numpy as np
from pk_utility import *
from Stat import *
class PokemonBase(object):
    def __init__(self,stat,indiv_values,type=TypeEnum.NORMAL,name='???',level=1):
        self.level=level
        
        self._skills=[]
        self._type=None
        self._name=''
        self._hp=0
        self._attack=0
        self._defense=0
        self._special_attack=0
        self._special_defense=0
        self._speed=0

        self._stat=stat
        self._indiv_values=indiv_values
        
        self._type=type
        self._name=name
        self.Grow(level)
        self.ResetStat()
        


    def ResetStat(self):
        self.hp=self._hp
        self.attack=self._attack
        self.defense=self._defense
        self.special_attack=self._special_attack
        self.special_defense=self._special_defense
        self.speed=self._speed
        self.stage=Stage()
        self.status_cond=StatusCondEnum.NORMAL
        self.special_cond=SpecialCond()
        self.is_playing=False
        self.position=PositionEnum.PLAYGROUND

    def HP(self):
        return self._hp

    def Attack(self):
        return self._attack

    def Defense(self):
        return self._defense
    
    def SpecialAttack(self):
        return self._special_attack

    def SpecialDefense(self):
        return self._special_defense

    def Speed(self):
        return self._speed

    def GetType(self):
        return self._type

    def GetName(self):
        return self._name

    def SetName(self,name):
        self._name = name

    def GetStat(self):
        return self._stat
    
    def Grow(self,level):
        '''
            level up and increase stat of pokemon
        '''
        if level<self.level:
            raise PokemonPKError()
        else:
            self.level=level
            self._hp=int((self._stat.hp+self._indiv_values.hp)*self.level/50+10+self.level)
            self._attack=int((self._stat.attack+self._indiv_values.attack)*self.level/50+5)
            self._defense=int((self._stat.defense+self._indiv_values.defense)*self.level/50+5)
            self._special_attack=int((self._stat.special_attack+self._indiv_values.special)*self.level/50+5)
            self._special_defense=int((self._stat.special_defense+self._indiv_values.special)*self.level/50+5)
            self._speed=int((self._stat.speed+self._indiv_values.speed)*self.level/50+5)
            self.PrintInfo()

    #学习技能
    def LearnSkills(self,skills=[],auto_learn=False,auto_lu_num=2,auto_tm_num=2):
        global g_c2e
        skills = [GetObjByChineseName(chinese_name) for chinese_name in skills]

        if not auto_learn:
            for skill in skills:
                skill_name = skill.GetName()
                print('you have learned',skill_name)

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
                            print('You have forgotten',self._skills[choose_idx].GetName())
                            if choose_idx<=3:
                                print('And learned',skill_name)
                                self._skills[choose_idx]=skill
                            
                            self._skills.pop()
                            is_finished=True
                            
                        else:
                            self._skills.pop()
                            is_finished=False
        else:
            def random_add_skills(self,skills,add_num,random_fact=0.5):
                cnt=0
                while cnt<min(add_num,len(skills)):
                    for i,skill  in enumerate(skills):
                        if np.random.random()<random_fact**(i+1):
                            self._skills.append(skill)
                            skills.pop(i)
                            cnt=cnt+1
                            break
            file_tm=open(pk_path+'StoreFiles/'+self._name+'/SkillsByTrickMachine.csv',encoding='gb2312')
            file_lu=open(pk_path+'StoreFiles/'+self._name+'/SkillsByLevelUp.csv',encoding='gb2312')
            TM = pd.read_csv(file_tm)
            LU = pd.read_csv(file_lu)
            TM = TM.dropna(axis=0,how='all')
            LU = LU.dropna(axis=0,how='all')
            file_tm.close()
            file_lu.close()

            

            

            
            #learn auto_lu_num level up skills
            LU=LU.loc[:,['等级','招式']]
            LU_start=0
            LU_end=len(LU)
            learn_limit=0.5
            for i in range(len(LU)):
                skill_level=LU['等级'][i]
                if skill_level.isdigit() and int(skill_level)>self.level:
                    LU_end=i
                    break
            LU_start=int(LU_end*learn_limit)
            LU = [GetObjByChineseName(chinese_name) for chinese_name in LU['招式'][LU_start:LU_end]]
            LU.reverse()
            random_add_skills(self,LU,auto_lu_num)


            #learn auto_tm_num trick machine skills
            TM = [GetObjByChineseName(chinese_name) for chinese_name in TM['招式']]
            np.random.shuffle(TM)
            random_add_skills(self,TM,auto_tm_num)
                
            
                

                
        self.PrintSkills()

    #打印所有技能
    def PrintSkills(self):
        for i,skill in enumerate(self._skills):
            print(i+1,' ',skill.GetInfo())

    def PrintInfo(self):
        print('{}\tLevel:{}\t\tHP:{}\t\tAttack:{}\t\tDefense:{}\t\tSpecialAttack:{}\t\tSpecialDefense:{}\t\tSpeed:{}'.format(self._name,self.level,self._hp,self._attack,self._defense,self._special_attack,self._special_defense,self._speed))

   


# k = PokemonBase()
# k.LearnSkills(['撞击','火苗','叫声','摇尾','抓','火焰喷射','大文字','飞行','龙之怒'],auto_learn=True)
