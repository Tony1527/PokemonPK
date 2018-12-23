

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
    def __init__(self,skill_series=None,name='',obj_of_action=ObjOfAction.TAR,info='-'):
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

    # def __init__(self,skill_series,obj_of_action=ObjOfAction.TAR,info=''):
        
    #     self.__init__(skill_series['ChineseName'],obj_of_action)

    def Apply(self,src=None,target=None,weather=None):
        if not (isinstance(src,PokemonBase) and isinstance(target,PokemonBase)):
            raise ValueError('src or target must be derived from SkillBase')
        print('{}使用{}'.format(src.GetName(),self._name))

        if self._obj_of_action & ObjOfAction.SRC:
            self.ApplySrc(src,target,weather)
        if self._obj_of_action & ObjOfAction.TAR:
            self.ApplyTarget(src,target,weather)
        if self._obj_of_action & ObjOfAction.SRC_ABL:
            self.ApplySrcAblity(src)
        if self._obj_of_action & ObjOfAction.TAR_ABL:
            self.ApplySrcAblity(target)
        if self._obj_of_action & ObjOfAction.WEATHER:
            self.ApplyWeather(weather)

        

    def DamageCal(self,src,target,weather):
        if self._category==CategoryEnum.PHYSICS:
            A_div_D = src.attack / target.defense
        elif self._category == CategoryEnum.SPECIAL:
            A_div_D = src.special_attack / target.special_defense

        #属性相克系数
        modifier,effect_str = TypeChart.TypeVSType(self._type,target.GetType())
        #主属性与技能属性相同
        if src.GetType()==self._type:
            modifier = modifier*1.5
        #击中要害
        #TODO
        damage = int((((2*src.level/5+2)*self._power*A_div_D)/50+2)*modifier)

        cnt=0
        delay_val=50
        while delay_val<damage:
            print('{}...'.format(delay_val))
            delay_val = delay_val+10
            time.sleep(1)

        print('{}受到了{}点伤害'.format(target.GetName(),damage))
        print('{}'.format(effect_str))

        return damage

    def ApplySrc(self,src,target,weather):
        src.hp = src.hp - self.DamageCal(src,target,weather)
        if src.hp<=0:
            src.hp=0
            print('{}倒下了'.format(src.GetName()))

    def ApplyTarget(self,src,target,weather):
        target.hp = target.hp - self.DamageCal(src,target,weather)
        if target.hp<=0:
            target.hp=0
            print('{}倒下了'.format(target.GetName()))

    def ApplySrcAblity(self,src):
        pass

    def ApplyTargetAblity(self,target):
        pass

    def ApplyWeather(self,weather):
        pass

    def Print(self):
        print(self.GetInfo())

    def GetInfo(self):
        return '{}      描述:{}      属性:{}     PP:{}   威力:{}     命中率:{}'.format(self._name,self._info,TypeEnum.ToChinese(self._type),self.pp,self._power,self._hit)
        
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