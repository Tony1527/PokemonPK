import numpy as np
from pk_utility import *
from Stat import *
from Console import *
class PokemonBase(object):
    def __init__(self,stat,indiv_values,type=TypeEnum.NORMAL,name='???',level=1):
        self.level=level
        
        self.skills=[]
        self._type=None
        self._name=''
        self._hp=1
        self._attack=1
        self._defense=1
        self._special_attack=1
        self._special_defense=1
        self._speed=1

        self._stat=stat
        self._indiv_values=indiv_values
        
        self._type=type
        self._name=name
        self.ResetStat()
        self.Grow(level)
        


    def ResetStat(self):
        self.hp=self._hp
        self.type=self._type
        self.stage=Stage()
        self.status_cond=StatusCond()
        self.special_cond=SpecialCond()
        self.is_playing=False
        self.position=PositionEnum.PLAYGROUND
        self.last_round=LastRound()

    def ResetStage(self):
        self.stage.Clear()

    def IsAlive(self):
        return self.hp!=0

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

    def Type(self):
        return self._type

    def GetSkills(self):
        return self.skills

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
            origin_HP=self._hp
            self._hp=int((self._stat.hp+self._indiv_values.hp)*self.level/50+10+self.level)
            self._attack=int((self._stat.attack+self._indiv_values.attack)*self.level/50+5)
            self._defense=int((self._stat.defense+self._indiv_values.defense)*self.level/50+5)
            self._special_attack=int((self._stat.special_attack+self._indiv_values.special)*self.level/50+5)
            self._special_defense=int((self._stat.special_defense+self._indiv_values.special)*self.level/50+5)
            self._speed=int((self._stat.speed+self._indiv_values.speed)*self.level/50+5)
            if self.hp!=0:
                self.hp=(self._hp-origin_HP)+self.hp

    def Down(self,stage_enum,num):
        Console.msg(self._name+'的'+self.stage.Down(stage_enum,num))

    def Up(self,stage_enum,num):
        Console.msg(self._name+'的'+self.stage.Up(stage_enum,num))

    #学习技能
    def LearnSkills(self,skills=[],auto_learn=False,auto_lu_num=2,auto_tm_num=2):
        global g_c2e
        skills = [GetObjByChineseName(chinese_name) for chinese_name in skills]

        if not auto_learn:
            for skill in skills:
                skill_name = skill.GetName()
                Console.msg('你学习了'+skill_name+'!')

                #如果技能数小于4，直接学会技能，否则需要进行学习判断
                if len(self.skills)<4:
                    self.skills.append(skill)
                else:
                    is_finished=False
                    while not is_finished:
                        Console.msg('你的技能已满，如果要学习其他技能，请选择想要忘记的技能')
                        self.skills.append(skill)
                        self.PrintSkills()
                        choose = input('你的选择是:')
                        choose_idx = g_d5i[choose]
                        if ToBeSure('忘记 '+self.skills[choose_idx]):
                            Console.msg('你选择忘记了'+self.skills[choose_idx].GetName())
                            if choose_idx<=3:
                                Console.msg(self.GetName()+'学会了'+skill_name)
                                self.skills[choose_idx]=skill
                            
                            self.skills.pop()
                            is_finished=True
                            
                        else:
                            self.skills.pop()
                            is_finished=False
        else:
            def random_add_skills(self,skills,add_num,random_fact=0.5):
                cnt=0
                while cnt<min(add_num,len(skills)):
                    for i,skill  in enumerate(skills):
                        if skill in self.skills:
                            continue
                        if np.random.random()<random_fact**(i+1):
                            self.skills.append(skill)
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
                
            
                

                
        # self.PrintSkills()

    #打印所有技能
    def PrintSkills(self):
        for i,skill in enumerate(self.skills):
            print(str(i+1)+' '+str(skill))

    def __str__(self):
        return '{}\t等级:{}    异常状态:{}    HP:{}/{}    属性:{}    攻击:{}    防御:{}    特攻:{}    特防:{}    速度:{}'.format(self._name,self.level,self.status_cond,self.hp,self._hp,TypeEnum.ToChinese(self.type),self._attack,self._defense,self._special_attack,self._special_defense,self._speed)
    def print(self):
        print(str(self))
   


# k = PokemonBase()
# k.LearnSkills(['撞击','火苗','叫声','摇尾','抓','火焰喷射','大文字','飞行','龙之怒'],auto_learn=True)
