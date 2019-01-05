from Team import *
from SkillFamalies import *

class Rounds(object):

    def __init__(self,our_tm,enemy_tm):
        self.our_tm=our_tm
        self.enemy_tm=enemy_tm
        self.our_pm=None
        self.enemy_pm=None
        self.our_skill=None
        self.enemy_skill=None
        self.weather=None
        self.first=True

    def Round(self):
        '''
            回合制战斗
        '''
        while True:
            #检查结束
            if self.CheckTeam():
                break
            if self.first:
                print('开战了！')
                self.our_pm=self.Admission(self.enemy_tm)
                self.enemy_pm=self.Admission(self.our_tm)
                self.first=False
                continue
            self.Choose()
            return

            
        pass
    
    def Choose(self):
        '''
            选择攻击、道具或者交换宝可梦
        '''
        
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
                        self.ourskill=retval
                        break
                elif choice == 1:
                    if self.our_tm.package.Open(self.our_tm.pm_list):
                        break
                elif choice == 2:
                    if self.our_tm.pm_list.SwitchPM():
                        self.Admission(self.our_tm)
                        break
            else:
                pass
        
        self._EnemyScriptChoose()

    def Admission(self,team):
        '''
            宝可梦入场
        '''
        rest()
        pokemon=team.pm_list.FirstAlive()
        if pokemon!=None:
            team.player.Speak('就决定是你了(゜-゜)つロ—    '+pokemon.GetName()+'!')
        return pokemon

    def UseProps(self):
        '''
            道具使用阶段
        '''
        pass

    def Fight(self):
        '''
            1.使用招式阶段
            2.判断宝可梦状态
            3.招式负面效果发动
        '''
        pass
    
    def End(self):
        '''
            1.天气变化
            2.回合结束
        '''
        pass

    def CheckTeam(self):
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

    def _EnemyScriptChoose(self):
        our_pm = self.our_tm.pm_list.FirstAlive()
        enemy_pm=self.enemy_tm.pm_list.FirstAlive()
        effect,effect_str=TypeChart.TypeVSType(our_pm.type,enemy_pm.type)
        end_flag=False

        self.enemy_tm.player.MockingOnFighting()

        #优先换精灵
        if not end_flag and effect>2:
            for i,pm in enumerate(self.enemy_tm.pm_list):
                if pm.IsAlive() and TypeChart.TypeVSType(our_pm.type,pm.type)[0]<=2:
                    self.enemy_tm.player.Speak('下来吧'+self.enemy_tm.pm_list.FirstAlive().GetName())
                    self.enemy_tm.pm_list.Swap(0,i)
                    self.Admission(self.enemy_tm)
                    enemy_pm=pm
                    end_flag=True
                    break
            
        #其次是使用药物
        if not end_flag and  enemy_pm.IsAlive() and enemy_pm.hp<enemy_pm.HP()*1:
            medicine=FullRestore(1)
            self.enemy_tm.player.Speak('对'+enemy_pm.GetName()+'使用了'+medicine.GetName())
            medicine.Use(enemy_pm)
            end_flag=True

        #最后是选择招式    
        if not end_flag:
            self._EnemyScriptSkillChoose()
            end_flag=True
        #TODO :something wrong
    def _EnemyScriptSkillChoose(self):
        our_pm = self.our_tm.pm_list.FirstAlive()
        enemy_pm=self.enemy_tm.pm_list.FirstAlive()
        choice=[0 for i in range(enemy_pm.skills)]
        struggle_flag=True
                        
                

        for i,skill in enumerate(enemy_pm.skills):
            if skill.pp>0:
                struggle_flag=False
                income=0
                if skill.IsHit(enemy_pm,our_pm,self.weather): 
                    if skill.GetPower()>0:
                        income=skill.DamageCal(enemy_pm,our_pm,self.weather)*skill.GetHit()
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

        if struggle_flag:
                return Struggle()
        else:
            return enemy_pm.skills[np.argmax(choice)]
        

