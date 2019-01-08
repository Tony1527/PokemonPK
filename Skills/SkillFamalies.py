from SkillBase import *


class MultiHitSkill(SkillBase):
    '''
        多次攻击型技能
    '''
    def __init__(self,skill_series,fix_hit_times=0,obj_of_action=ObjOfAction.TAR,info='连续攻击型技能'):
        SkillBase.__init__(self,skill_series,obj_of_action,info)
        self._fix_hit_times=fix_hit_times
    
    def ApplyTarget(self,src,target,weather):
        damage=0   
        round_num=2
        if self._fix_hit_times!=0:
            round_num=self._fix_hit_times    
        else:
            hit_chance = np.random.rand()
            if 1/6>hit_chance and hit_chance>=0:
                round_num=5
            elif 2/6>hit_chance and hit_chance>=1/6:
                round_num=4
            elif 4/6>hit_chance and hit_chance>=2/6:
                round_num=3
            elif 6/6>hit_chance and hit_chance>=4/6:
                round_num=2
        for i in range(round_num):
            print('击中'+str(i+1)+'次')
            damage = damage + self.DamageCal(src,target,weather)
            rest()
        return damage

class MustKillSkill(SkillBase):
    def __init__(self,skill_series,obj_of_action=ObjOfAction.TAR,info='一击必杀'):
        SkillBase.__init__(self,skill_series,obj_of_action,info)
    def ApplyTarget(self,src,target,weather):
        damage=target.hp
        print('一击必杀')
        return damage
    def IsHit(self,src,target,weather):
        if src.level<target.level:
            return False
        else:
            return np.random.rand()<(30+src.level-target.level)/100

class ReboundSkill(SkillBase):
    def __init__(self,skill_series,percent,obj_of_action=ObjOfAction.TAR+ObjOfAction.SRC,info='双刃剑技能'):
        SkillBase.__init__(self,skill_series,obj_of_action,info)
        self.percent=percent
    def ApplySrc(self,src,target_damage):
        print(src.GetName()+'受到反弹伤害')
        return int(target_damage*self.percent)


class SelfLossSkill(SkillBase):
    def __init__(self,skill_series,percent,obj_of_action=ObjOfAction.TAR+ObjOfAction.SRC,info='自损技能'):
        SkillBase.__init__(self,skill_series,obj_of_action,info)
        self.percent=percent
    def ApplySrc(self,src,target_damage):
        print(src.GetName()+'受到自损伤害')
        return int(src.HP()*self.percent)

class StockpileSkill(SkillBase):
    def __init__(self,skill_series,position=PositionEnum.PLAYGROUND,discription='',obj_of_action=ObjOfAction.TAR,info='蓄力型技能'):
        SkillBase.__init__(self,skill_series,obj_of_action,info)
        self._position=position
        self._discription=discription
        
    def SetDefault(self):
        self._is_ready=False
    def PreApply(self,src,target,weather):
        if self._is_ready==False:
            print(src.GetName()+self._discription+'...')
            self._is_ready=True
            src.position=self._position
            src.special_cond.Set(SpecialCondEnum.FORCED,2)
            return False
        self.pp=self.pp-1
        return True

    def PostApply(self,src,target,weather):
        if self._is_ready==True:
            self._is_ready=False
            src.position=PositionEnum.PLAYGROUND

class AbsorbSkill(SkillBase):
    def __init__(self,skill_series,percent=0.5,obj_of_action=ObjOfAction.TAR+ObjOfAction.SRC,info='吸收型技能'):
        SkillBase.__init__(self,skill_series,obj_of_action,info)
        self.percent=percent
    def ApplySrc(self,src,target_damage):
        absorb_value=int(target_damage*self.percent)
        print(src.GetName()+'吸收了'+str(absorb_value)+'点生命')
        return -1

class EasyCriticalHitSkill(SkillBase):
    def _IsCriticalHit(self,src,target):
        return np.random.rand()<src.GetStat().speed*4/256*src.stage.Get(StageEnum.CRITICAL_HITS)