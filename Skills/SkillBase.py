

from pk_enums import TypeEnum,CategoryEnum
from pk_utility import *
from PokemonBase import PokemonBase
from ManipulatePM import *

try:
    @unique
    class ObjOfAction(IntEnum):

        SRC=1,
        TAR=2,
        SRC_ABL=4,
        TAR_ABL=8,
        WEATHER=16

except ValueError as e:
    print(e)


g_skill_hit={
    100:255,
    95:242,
    90:229,
    85:216,
    80:204,
    75:191,
    70:178,
    60:153,
    55:140,
    50:127
}



class SkillBase(Singleton):
    _obj_of_action=None
    _type = None
    _power = 0
    _hit = 0
    _category=False
    _info = '-'
    _name = ''
    _priority=0
    _pp=0

    pp = 0
    is_ready=True
    def __init__(self,skill_series=None,obj_of_action=ObjOfAction.TAR,info='-'):
        if not isinstance(skill_series,pd.Series):
            raise ValueError
        
        
        self._obj_of_action=obj_of_action
        self._type = getattr(TypeEnum,skill_series['Type'])
        if skill_series['Power']!='-':
            self._power = int(skill_series['Power'])
        self._category = getattr(CategoryEnum,skill_series['Category'])
        self._info = info
        self._name = skill_series['ChineseName']
        if skill_series['Hit']!='-':
            self._hit = int(skill_series['Hit'])
        self._pp=int(skill_series['PP'])
        self.pp=self._pp
        self._priority=0
        self.SetDefault()

    def SetDefault(self):
        self.is_ready=True

    def Apply(self,src=None,target=None,weather=None,is_print=True):
        # if (src!=None and target!=None) and not (isinstance(src,PokemonBase) and isinstance(target,PokemonBase)):
        #     raise ValueError('src or target must be derived from SkillBase')
        target_damage=0
        if is_print:
            Console.msg('{}使用{}'.format(src.GetName(),self._name))
        if not self.PreApply(src,target,weather):
            # rest()
            # if is_print:
            #     Console.msg('==============')
            return target_damage
        
        if self.IsHit(src,target,weather):
            
            if src.IsAlive() and self._obj_of_action & ObjOfAction.SRC_ABL:
                self.ApplySrcAblity(src)
                # rest()
            if target.IsAlive() and self._obj_of_action & ObjOfAction.TAR:
                target_damage = int(self.ApplyTarget(src,target,weather))
                ApplyDamage(target,target_damage)
                # rest()
            if src.IsAlive() and self._obj_of_action &ObjOfAction.SRC:
                src_damage = int(self.ApplySrc(src,target_damage))
                ApplyDamage(src,src_damage)
                # rest()
            if target.IsAlive() and self._obj_of_action &ObjOfAction.TAR_ABL:
                self.ApplyTargetAblity(target,weather)
                # rest()
            if  self._obj_of_action &ObjOfAction.WEATHER:
                self.ApplyWeather(weather)
                # rest()
        else:
            if is_print:
                Console.msg('{}躲开了'.format(target.GetName()))
            self.SideEffect(src,target)
            # rest()
        self.PostApply(src,target,weather)
        # if is_print:
        #     Console.msg('==============')
        return target_damage

    def IsHit(self,src,target,weather):
        if target!=None and target.position==PositionEnum.UNDERGROUND or target.position==PositionEnum.SKY:
            return False
        if self._hit==0:
            return True
        rand_value = np.random.randint(1,256)
        hit_value=g_skill_hit[self._hit]*src.stage.Get(StageEnum.HIT)/target.stage.Get(StageEnum.DODGE)
        return rand_value<hit_value
    def _IsCriticalHit(self,src,target):
        return  np.random.rand()<src.GetStat().speed/2/256*src.stage.Get(StageEnum.CRITICAL_HITS)
    def SideEffect(self,src,target):
        pass
    def PreApply(self,src,target,weather):
        self.pp=self.pp-1
        return True
    def PostApply(self,src,target,weather):
        pass
    def DamageCal(self,src,target,weather,is_print=True):
        if self._category==CategoryEnum.PHYSICS:
            A_div_D = src.Attack()*src.stage.Get(StageEnum.ATTACK) / (target.Defense()*target.stage.Get(StageEnum.DEFENSE))
        elif self._category == CategoryEnum.SPECIAL:
            A_div_D = src.SpecialAttack()*src.stage.Get(StageEnum.SPECIAL_ATTACK) / (target.SpecialDefense()*target.stage.Get(StageEnum.SPECIAL_DEFENSE))

        #属性相克系数
        modifier,effect_str = TypeChart.TypeVSType(self._type,target.type)
        #主属性与技能属性相同
        if src.type==self._type:
            modifier = modifier*1.5

        #额外项
        addition=np.random.randint(85,101)/100
        #击中要害
        is_critical_hit=self._IsCriticalHit(src,target)


        if is_critical_hit:
            addition = addition*1.5

        if self._category==CategoryEnum.PHYSICS and target.special_cond.Get(SpecialCondEnum.REFLECT)!=0:
            addition=addition/2
        if self._category==CategoryEnum.SPECIAL and target.special_cond.Get(SpecialCondEnum.LIGHT_SCREEN)!=0:
            addition=addition/2
        if src.status_cond.Check(StatusCondEnum.BURN):
            addition=addition/2
        
        damage = int((((2*src.level/5+2)*self._power*A_div_D)/50+2)*modifier*addition)

        

        if is_critical_hit and not effect_str==u'似乎没有效果' and is_print:
            Console.msg('命中要害')
        
        if effect_str!='' and is_print:
            Console.msg('{}'.format(effect_str))

        
        return damage

    def ApplySrc(self,src,target_damage):
        return -1
        

    def ApplyTarget(self,src,target,weather):
        return self.DamageCal(src,target,weather)
        

    def ApplySrcAblity(self,src):
        pass

    def ApplyTargetAblity(self,target,weather):
        pass

    def ApplyWeather(self,weather):
        pass

    @classmethod
    def CauseSpecialCond(cls,target,percent,special_cond_enum,round=0,is_print=False):
        '''
            引发特殊的异常状态
        '''
        if np.random.rand()<percent:
            if target.special_cond.Get(special_cond_enum)==0:
                if round==0:
                    round=np.random.randint(2,5)
                target.special_cond.Set(special_cond_enum,round)
                Console.msg(target.GetName()+SpecialCondEnum.ToChinese(special_cond_enum)+"了")
            else:
                if is_print:
                    Console.msg(target.GetName()+'已经'+SpecialCondEnum.ToChinese(special_cond_enum)+"了")
            
                
    @classmethod
    def CauseStatusCond(cls,target,percent,status_cond_enum,round=0,is_print=False):
        if np.random.rand()<percent:
            if target.status_cond.IsNormal():
                if round==0:
                    round=np.random.randint(2,4)
                target.status_cond.Set(status_cond_enum,round)
                Console.msg(target.GetName()+str(target.status_cond)+"了")
            else:
                if is_print:
                    Console.msg('似乎没有什么效果')
                else:
                    pass
    
    def print(self):
        print(self)

    def __str__(self):
        return '{}      描述:{}      属性:{}     PP:{}/{}   威力:{}     命中率:{}'.format(self._name,self._info,TypeEnum.ToChinese(self._type),self.pp,self._pp,self._power,self._hit)
        
    def GetName(self):
        return self._name
    def GetPriority(self):
        return self._priority 
    def GetType(self):
        return self._type
    def GetPower(self):
        return self._power
    def GetHit(self):
        return self._hit
    def GetObjOfAction(self):
        return self._obj_of_action

class SkillChart(Singleton):
    _skill_chart=None
    _skill_num=0
    def __init__(self):
        global g_c2e
        self._skill_chart=pd.read_csv(pk_path+'StoreFiles/SkillChart.csv')
        skills_c2e=dict(zip(self._skill_chart['ChineseName'],self._skill_chart['EnglishName']))
        g_c2e.update(skills_c2e)
        self._skill_num=len(self._skill_chart)
        skill_index = self._skill_chart['EnglishName'].values
        for i in range(len(skill_index)):
            skill_index[i] = skill_index[i].lower()
        
        
        self._skill_chart.index=skill_index
    @classmethod
    def GetSkillChart(cls):
        instance = SkillChart.GetInstance()
        return instance._skill_chart

    @classmethod
    def GetSkillSeries(cls,skill_name):
        skill_name = skill_name.lstrip().rstrip().lower()
        instance = SkillChart.GetInstance()
        return instance._skill_chart.loc[skill_name]

    @staticmethod
    def LoadSkillChart():
        SkillChart.GetInstance()

class SkillFactory:

    @classmethod
    def GetInstance(cls,class_obj,*args,**kwargs):
        if not hasattr(class_obj,'GetInstance'):
            raise TypeError
        return class_obj.GetInstance()


SkillChart.LoadSkillChart()