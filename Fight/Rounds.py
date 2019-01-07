from pk_utility import *
from pk_enums import *
from Team import *
from SkillFamalies import *
from AllSkills import *
from Weather import *
from ManipulatePM import *

class Rounds(object):

    def __init__(self,our_tm,enemy_tm):
        self.our_tm=our_tm
        self.enemy_tm=enemy_tm
        self.our_skill=None
        self.enemy_skill=None
        self.our_life_line=True
        self.enemy_life_line=True
        self.weather=Weather()
        self.first=True

    def Round(self):
        '''
            回合制战斗
        '''
        while True:
            #检查结束
            if self._CheckTeam():
                break
            if self.first:
                print('开战了！')
                self.our_pm=self._Admission(self.enemy_tm)
                self.enemy_pm=self._Admission(self.our_tm)
                self.first=False
                continue
            self._Choose()
            self._Fight()

            self._End()
            rest()
            

            
        pass
    
    def _Choose(self):
        '''
            选择攻击、道具或者交换宝可梦
        '''
        self.our_skill=None
        self.enemy_skill=None
        our_pm = self.our_tm.pm_list.FirstAlive()
        enemy_pm=self.enemy_tm.pm_list.FirstAlive()

        #我方选择
        if our_pm.special_cond.Check(SpecialCondEnum.FORCED):
            self.our_skill=our_pm.last_round.src_skill
        else:
            while(False):
                print('[1] 战斗')
                print('[2] 背包')
                print('[3] 精灵')
                choice=input('请选择你要进行的操作：')
                choice=a2i(choice,1,3)
                if choice<3 and choice>=0:
                    if choice == 0:
                        retval = SkillChoose(self.our_pm)
                        if retval!=None:
                            self.our_skill=retval
                            break
                    elif choice == 1:
                        if self.our_tm.package.Open(self.our_tm.pm_list):
                            break
                    elif choice == 2:
                        if our_pm.special_cond.Check(SpecialCondEnum.BOUND):
                            print(our_pm.GetName()+'被束缚，无法下场')
                            continue
                        if self.our_tm.pm_list.SwitchPM():
                            self._Admission(self.our_tm)
                            break
                else:
                    pass
        
        #敌方选择
        self._EnemyScriptChoose()
        print(self.our_skill)
        print(self.enemy_skill)

    def _Admission(self,team):
        '''
            宝可梦入场
        '''
        rest()
        pokemon=team.pm_list.FirstAlive()
        if pokemon!=None:
            team.player.Speak('就决定是你了(゜-゜)つロ—    '+pokemon.GetName()+'!')
        return pokemon

    def _UseProps(self):
        '''
            道具使用阶段
        '''
        pass

    def _Fight(self):
        '''
            1.使用招式阶段
            2.判断宝可梦状态
            3.招式负面效果发动
        '''
        our_pm = self.our_tm.pm_list.FirstAlive()
        enemy_pm=self.enemy_tm.pm_list.FirstAlive()
        if self.our_skill==None:
            if self.enemy_skill==None:
                pass
            else:
                self._CheckAndApplySkill(self.enemy_skill,enemy_pm,our_pm,self.weather)
        else:
            if self.enemy_skill==None:
                self._CheckAndApplySkill(self.our_skill,our_pm,enemy_pm,self.weather)
            else:
                if self.enemy_skill.priority>self.our_skill.priority:
                    self._CheckAndApplySkill(self.enemy_skill,enemy_pm,our_pm,self.weather)
                    self._CheckAndApplySkill(self.our_skill,our_pm,enemy_pm,self.weather)

                elif self.enemy_skill.priority<self.our_skill.priority:
                    self._CheckAndApplySkill(self.our_skill,our_pm,enemy_pm,self.weather)
                    self._CheckAndApplySkill(self.enemy_skill,enemy_pm,our_pm,self.weather)

                else:
                    our_speed = our_pm.Speed()
                    enemy_speed = enemy_pm.Speed()
                    if our_speed*our_pm.stage.Get(StageEnum.SPEED) > enemy_speed*enemy_pm.stage.Get(StageEnum.SPEED):
                        pass
                    elif our_speed*our_pm.stage.Get(StageEnum.SPEED) < enemy_speed*enemy_pm.stage.Get(StageEnum.SPEED):
                        self._CheckAndApplySkill(self.enemy_skill,enemy_pm,our_pm,self.weather)
                        self._CheckAndApplySkill(self.our_skill,our_pm,enemy_pm,self.weather)
                    else:
                        if our_speed > enemy_speed:
                            self._CheckAndApplySkill(self.enemy_skill,enemy_pm,our_pm,self.weather)
                            self._CheckAndApplySkill(self.our_skill,our_pm,enemy_pm,self.weather)
                        elif our_speed < enemy_speed:
                            self._CheckAndApplySkill(self.enemy_skill,enemy_pm,our_pm,self.weather)
                            self._CheckAndApplySkill(self.our_skill,our_pm,enemy_pm,self.weather)
                        else:
                            self._CheckAndApplySkill(self.enemy_skill,enemy_pm,our_pm,self.weather)
                            self._CheckAndApplySkill(self.our_skill,our_pm,enemy_pm,self.weather)
            
        #招式负面效果发动
        if our_pm.IsAlive():
            self._NegativeEffect(our_pm)
        if enemy_pm.IsAlive():
            self._NegativeEffect(enemy_pm)

    def _NegativeEffect(self,pm):

        if pm.status_cond.Check(StatusCondEnum.POISON):
            print(pm.GetName()+pm.status_cond.Discription())
            ApplyDamage(pm,pm.HP()*1/8)
        elif pm.status_cond.Check(StatusCondEnum.BADLYPOISON):
            print(pm.GetName()+pm.status_cond.Discription())
            time=pm.status_cond.LastTime()+1
            if time>15:
                time=15
            ApplyDamage(pm,pm.HP()*time/16)
        elif pm.status_cond.Check(StatusCondEnum.BURN):
            print(pm.GetName()+pm.status_cond.Discription())
            ApplyDamage(pm,pm.HP()*1/16)

        
    
    def _End(self):
        '''
            1.天气变化
            2.回合结束
        '''
        our_pm = self.our_tm.pm_list.FirstAlive()
        enemy_pm=self.enemy_tm.pm_list.FirstAlive()
        if our_pm!=None and our_pm.IsAlive():
            our_pm.status_cond.Reduce()
            our_pm.special_cond.Reduce()
        if enemy_pm!=None and enemy_pm.IsAlive():
            enemy_pm.status_cond.Reduce()
            enemy_pm.special_cond.Reduce()
        if self.weather!=None:
            last_weather=self.weather.Get()
            self.weather.Reduce()
            if self.weather!=last_weather:
                print(self.weather.Discription())
            else:
                if self.weather.IsNormal():
                    pass
                else:
                    print(self.weather.Discription())
                

    def _CheckTeam(self):
        '''
            检查战斗是否结束
        '''
        end=True
        for pm in self.enemy_tm.pm_list:
            if pm.hp>0:
                end=False
        if end==True:
            print('***************')
            print('你赢得了胜利！')
            print('***************')
            return True
        end=True
        for pm in self.our_tm.pm_list:
            if pm.hp>0:
                end=False
        if end==True:
            print('你输了...')
            return True
        return end
    def _CheckAndApplySkill(self,skill,src,target,weather):
        status=src.status_cond
        damage=0
        apply_flag=True
        if not(src.IsAlive() and target.IsAlive()):
            return False

        if not StatusCondEnum.IsNormal(status):
            if status==StatusCondEnum.PARALYSIS:
                if np.random.rand()<0.25:
                    print(src.GetName()+src.status_cond.Discription())
                    apply_flag=False
            elif status==StatusCondEnum.SLEEP:
                print(src.GetName()+src.status_cond.Discription())
                apply_flag=False
            elif status==StatusCondEnum.FREEZE:
                print(src.GetName()+src.status_cond.Discription())
                apply_flag=False
        special_cond=src.special_cond
        if special_cond.Check(SpecialCondEnum.STIFF):
            print(src.GetName()+SpecialCondEnum.Discription(src.special_cond.Get(SpecialCondEnum.STIFF)))
            apply_flag=False
        elif special_cond.Check(SpecialCondEnum.CONFUSION):
            print(src.GetName()+'混乱了')
            rest()
            if np.random.rand()<0.5:
                print(src.GetName()+SpecialCondEnum.Discription(src.special_cond.Get(SpecialCondEnum.CONFUSION)))
                damage=Struggle().Apply(src,src,weather)
                apply_flag=False
        # elif special_cond.Check(SpecialCondEnum.FORCED):
        #     return False
        if apply_flag:
            damage=skill.Apply(src,target,weather)
        if target.IsAlive():
            target.last_round.target_skill=skill
            target.suffer_damage=damage
        if src.IsAlive():
            src.last_round.src_skill=skill
        
    #     self._CheckLifeLine(target)
    #     self._CheckLifeLine(src)

    # def _CheckLifeLine(self,pm):
    #     if not pm.IsAlive() and pm.life_line:
    #         print(pm.GetName()+'倒下了...')
    #         pm.life_line=False

    def _EnemyScriptChoose(self):
        our_pm = self.our_tm.pm_list.FirstAlive()
        enemy_pm=self.enemy_tm.pm_list.FirstAlive()
        effect,effect_str=TypeChart.TypeVSType(our_pm.type,enemy_pm.type)

        self.enemy_tm.player.MockingOnFighting()
        if enemy_pm.special_cond.Check(SpecialCondEnum.FORCED):
            self.enemy_skill=enemy_pm.last_round.src_skill
            return True
        else:
            #优先换精灵
            if effect>2:
                if not enemy_pm.special_cond.Check(SpecialCondEnum.BOUND):
                    for i,pm in enumerate(self.enemy_tm.pm_list):
                        if pm.IsAlive() and TypeChart.TypeVSType(our_pm.type,pm.type)[0]<=2:
                            self.enemy_tm.player.Speak('下来吧'+self.enemy_tm.pm_list.FirstAlive().GetName())
                            self.enemy_tm.pm_list.Swap(0,i)
                            self._Admission(self.enemy_tm)
                            enemy_pm=pm
                            return True
                
            #其次是使用药物
            if enemy_pm.IsAlive() and enemy_pm.hp<enemy_pm.HP()*0.25:
                medicine=FullRestore(1)
                self.enemy_tm.player.Speak('对'+enemy_pm.GetName()+'使用了'+medicine.GetName())
                medicine.Use(enemy_pm)
                return True

            #最后是选择招式    
            self.enemy_skill=self._EnemyScriptSkillChoose()
            return True
            
    def _EnemyScriptSkillChoose(self):
        our_pm = self.our_tm.pm_list.FirstAlive()
        enemy_pm=self.enemy_tm.pm_list.FirstAlive()
        choice=[0 for i in range(len(enemy_pm.skills))]
        struggle_flag=True
                        
        

        for i,skill in enumerate(enemy_pm.skills):
            if skill.pp>0:
                struggle_flag=False
                income=0
                if skill.IsHit(enemy_pm,our_pm,self.weather): 
                    if skill.GetPower()>0:
                        income=skill.DamageCal(enemy_pm,our_pm,self.weather,is_print=False)*skill.GetHit()/100
                    if isinstance(skill,ReboundSkill) or isinstance(skill,SelfLossSkill):
                        income=income-enemy_pm.hp*skill.percent
                    obj_of_action=skill.GetObjOfAction()
                    if obj_of_action & ObjOfAction.SRC:
                        if skill.GetPower()>0:
                            income = income-30*np.random.randint(50,100)/100
                        else:
                            income = income+30*np.random.randint(50,100)/100
                    if obj_of_action & ObjOfAction.SRC_ABL:
                        if enemy_pm.stage.Mean()<=0:
                            income = income+30*np.random.randint(50,100)/100
                        else:
                            income = income+15*np.random.randint(50,100)/100
                    if obj_of_action & ObjOfAction.TAR_ABL:
                        if our_pm.stage.Mean()>=0:
                            income = income+30*np.random.randint(50,100)/100
                        else:
                            income = income+15*np.random.randint(50,100)/100
                choice[i]=income
            else:
                choice[i]=-1

        if struggle_flag:
            return Struggle()
        else:
            return enemy_pm.skills[np.argmax(choice)]
        

