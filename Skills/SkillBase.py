

from pk_enums import TypeEnum,CategoryEnum
from pk_utility import *
from PokemonBase import PokemonBase

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

g_special_critical_skills=[
    '劈开','飞叶快刀','空手劈','蟹钳','旋风刀'
]

class SkillBase(Singleton):
    _obj_of_action=None
    _type = None
    _power = 0
    _hit = 0
    _category=False
    _info = '-'
    _name = ''
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
        self.priority=0
        self.SetDefault()

    def SetDefault(self):
        self.is_ready=True

    def Apply(self,src=None,target=None,weather=None):
        # if (src!=None and target!=None) and not (isinstance(src,PokemonBase) and isinstance(target,PokemonBase)):
        #     raise ValueError('src or target must be derived from SkillBase')
        
        print('{}使用{}'.format(src.GetName(),self._name))
        if not self.PreApply(src,target,weather):
            rest()
            print('==============')
            return
        
        if self._IsHit(src,target,weather):
            target_damage=0
            if  self._obj_of_action & ObjOfAction.SRC_ABL:
                self.ApplySrcAblity(src)
                rest()
            if self._obj_of_action & ObjOfAction.TAR:
                target_damage = self.ApplyTarget(src,target,weather)
                self.ApplyDamage(target,target_damage)
                rest()
            if  self._obj_of_action &ObjOfAction.SRC:
                src_damage = self.ApplySrc(src,target_damage)
                self.ApplyDamage(src,src_damage)
                rest()
            if  self._obj_of_action &ObjOfAction.TAR_ABL:
                self.ApplyTargetAblity(target,weather)
                rest()
            if  self._obj_of_action &ObjOfAction.WEATHER:
                self.ApplyWeather(weather)
                rest()
        else:
            print('{}躲开了'.format(target.GetName()))
            self.SideEffect(src,target)
            rest()
        self.PostApply(src,target,weather)
        print('==============')

    def _IsHit(self,src,target,weather):
        if target!=None and target.position==PositionEnum.UNDERGROUND or target.position==PositionEnum.SKY:
            return False
        if self._hit==0:
            return True
        rand_value = np.random.randint(1,256)
        hit_value=g_skill_hit[self._hit]*src.stage.Get(StageEnum.HIT)/target.stage.Get(StageEnum.DODGE)
        return rand_value<hit_value
    def SideEffect(self,src,target):
        pass
    def PreApply(self,src,target,weather):
        self.pp=self.pp-1
        return True
    def PostApply(self,src,target,weather):
        pass
    def DamageCal(self,src,target,weather):
        if self._category==CategoryEnum.PHYSICS:
            A_div_D = src.attack*src.stage.Get(StageEnum.ATTACK) / (target.defense*target.stage.Get(StageEnum.DEFENSE))
        elif self._category == CategoryEnum.SPECIAL:
            A_div_D = src.special_attack*src.stage.Get(StageEnum.SPECIAL_ATTACK) / (target.special_defense*target.stage.Get(StageEnum.SPECIAL_DEFENSE))

        #属性相克系数
        modifier,effect_str = TypeChart.TypeVSType(self._type,target.GetType())
        #主属性与技能属性相同
        if src.GetType()==self._type:
            modifier = modifier*1.5

        #额外项
        addition=np.random.randint(85,101)/100
        #击中要害
        if self._name in g_special_critical_skills:
            is_critical_hit= np.random.rand()<src.GetStat().speed*4/256
        else:
            is_critical_hit= np.random.rand()<src.GetStat().speed/2/256


        if is_critical_hit:
            addition = addition*1.5
            
        
        damage = int((((2*src.level/5+2)*self._power*A_div_D)/50+2)*modifier*addition)

        
        if is_critical_hit and not effect_str==u'似乎没有效果':
            print('命中要害')
        
        if effect_str!='':
            print('{}'.format(effect_str))
        return damage

    def ApplySrc(self,src,target_damage):
        return 0
        

    def ApplyTarget(self,src,target,weather):
        return self.DamageCal(src,target,weather)
        

    def ApplySrcAblity(self,src):
        pass

    def ApplyTargetAblity(self,target,weather):
        pass

    def ApplyWeather(self,weather):
        pass

    def CauseSpecialCond(self,target,percent,special_cond,round=0):
        if np.random.rand()<percent:
            if target.special_cond.Get(special_cond)==0:
                if round==0:
                    num=np.random.randint(1,4)
                target.special_cond.Set(special_cond,num)
                print(target.GetName()+SpecialCondEnum.ToChinese(special_cond)+"了")
            
                

    def CauseStatusCond(self,target,percent,status_cond):
        if np.random.rand()<percent:
            if StatusCondEnum.IsNormal(target.status_cond):
                target.status_cond = status_cond
                print(target.GetName()+StatusCondEnum.ToChinese(status_cond)+"了")
            else:
                print('似乎没有什么效果')
    def ApplyDamage(self,target,damage):
        if damage==0:
            print('似乎对对方没有造成什么伤害')
            return
        delay_val=50
        while delay_val<damage:
            print('{}...'.format(delay_val))
            delay_val = delay_val+10
            if delay_val>=target.hp:
                break
            rest()
        print('{}受到了{}点伤害'.format(target.GetName(),damage))
        target.hp = target.hp - damage
        if target.hp<=0:
            target.hp=0
            print('{}倒下了'.format(target.GetName()))
    def Print(self):
        print(self.GetInfo())

    def GetInfo(self):
        return '{}      描述:{}      属性:{}     PP:{}   威力:{}     命中率:{}      剩余PP:{}'.format(self._name,self._info,TypeEnum.ToChinese(self._type),self._pp,self._power,self._hit,self.pp)
        
    def GetName(self):
        return self._name
        

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
    def GetSkillSeries(cls,skill_name):
        skill_name = skill_name.lstrip().rstrip().lower()
        # print(skill_name)
        instance = SkillChart.GetInstance()
        return instance._skill_chart.ix[skill_name]

    @staticmethod
    def LoadSkillChart():
        SkillChart.GetInstance()

class SkillFactory:
    def __init__(self):
        print('in skill_factory.')

    @classmethod
    def GetInstance(cls,class_obj,*args,**kwargs):
        if not hasattr(class_obj,'GetInstance'):
            raise TypeError
        return class_obj.GetInstance()


SkillChart.LoadSkillChart()