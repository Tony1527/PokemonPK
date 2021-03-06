from enum import IntEnum,Enum,unique

try:
    @unique
    class TypeEnum(IntEnum):
        NORMAL=1,
        FIGHT=2,
        FLYING=4,
        POISON=8,
        GROUND=16,
        ROCK=32,
        BUG=64,
        GHOST=128,
        FIRE=256,
        WATER=512,
        GRASS=1024,
        ELECTR=2048,
        PSYCHC=4096,
        ICE=8192,
        DRAGON=16384


        def __str__(self):
            raise RuntimeError('Please use ToChinese instead!')
            return ''

        @classmethod
        def ToChinese(cls,type):
            mask=1
            s=''
            for i in range(0,15):
                mask=1<<i
                flag=type&mask
                if flag==TypeEnum.NORMAL:
                    s=s+'一般 '
                elif flag==TypeEnum.FIGHT:
                   s=s+'格斗 '
                elif flag==TypeEnum.FLYING:
                   s=s+'飞行 '
                elif flag==TypeEnum.POISON:
                   s=s+'毒 '
                elif flag==TypeEnum.GROUND:
                   s=s+'地 '
                elif flag==TypeEnum.ROCK:
                   s=s+'岩石 '
                elif flag==TypeEnum.BUG:
                   s=s+'虫 '
                elif flag==TypeEnum.GHOST:
                   s=s+'幽灵 '
                elif flag==TypeEnum.FIRE:
                   s=s+'火 '
                elif flag==TypeEnum.WATER:
                   s=s+'水 '
                elif flag==TypeEnum.GRASS:
                   s=s+'草 '
                elif flag==TypeEnum.ELECTR:
                   s=s+'电 '
                elif flag==TypeEnum.PSYCHC:
                   s=s+'超能力 '
                elif flag==TypeEnum.ICE:
                   s=s+'冰 '
                elif flag==TypeEnum.DRAGON:
                   s=s+'龙 '
            return s
except ValueError as e:
    print(e)

class ConditionEnum(IntEnum):

    def __str__(self):
        return self.ToChinese(self)
    @classmethod
    def ToChinese(cls,value):
        return ''

    

class CategoryEnum(IntEnum):
    PHYSICS=0,
    SPECIAL=1
    @classmethod
    def ToChinese(cls,category):
        if category==PHYSICS:
            return '物理'
        elif category==SPECIAL:
            return '特殊'

class StatusCondEnum(ConditionEnum):
    NORMAL=0,
    BURN=1,
    FREEZE=2,
    PARALYSIS=3,
    POISON=4,
    BADLYPOISON=5,
    SLEEP=6

    @classmethod
    def IsNormal(cls,status_cond):
        return status_cond==StatusCondEnum.NORMAL

    @classmethod
    def ToChinese(cls,value):
        if value==StatusCondEnum.NORMAL:
            return '正常'
        elif value==StatusCondEnum.BURN:
            return '烧伤'
        elif value==StatusCondEnum.FREEZE:
            return '冻伤'
        elif value==StatusCondEnum.PARALYSIS:
            return '麻痹'
        elif value==StatusCondEnum.POISON:
            return '中毒'
        elif value==StatusCondEnum.BADLYPOISON:
            return '剧毒'
        elif value==StatusCondEnum.SLEEP:
            return '呼呼大睡'

    @classmethod
    def Discription(cls,value):
        if value == StatusCondEnum.NORMAL:
            return '正常'
        elif value==StatusCondEnum.BURN:
            return '处于灼烧状态'
        elif value==StatusCondEnum.FREEZE:
            return '处于冻伤状态，无法行动'
        elif value==StatusCondEnum.PARALYSIS:
            return '处于麻痹状态，无法行动'
        elif value==StatusCondEnum.POISON:
            return '处于中毒状态'
        elif value==StatusCondEnum.BADLYPOISON:
            return '处于中剧毒状态'
        elif value==StatusCondEnum.SLEEP:
            return 'zzzz呼呼大睡中'

    @classmethod
    def BackToNormal(cls,value):
        if value==StatusCondEnum.NORMAL:
            return ''
        elif value==StatusCondEnum.BURN:
            return '从灼烧状态中解除'
        elif value==StatusCondEnum.FREEZE:
            return '从冰冻状态中解除'
        elif value==StatusCondEnum.PARALYSIS:
            return '从麻痹状态中解除'
        elif value==StatusCondEnum.POISON:
            return '从中毒状态中解除'
        elif value==StatusCondEnum.BADLYPOISON:
            return '从剧毒状态中解除'
        elif value==StatusCondEnum.SLEEP:
            return '清醒了'

class SpecialCondEnum(ConditionEnum):
    STIFF=0,
    FORCED=1,
    BOUND=2,
    CONFUSION=3,
    PARASITIC=4,
    LIGHT_SCREEN=5,
    REFLECT=6

    @classmethod
    def ToChinese(cls,value):
        if value==SpecialCondEnum.CONFUSION:
            return '混乱'
        elif value==SpecialCondEnum.BOUND:
            return '被束缚'
        elif value==SpecialCondEnum.FORCED:
            return '强制攻击'
        elif value==SpecialCondEnum.STIFF:
            return '僵硬'
        elif value==SpecialCondEnum.PARASITIC:
            return '被寄生'
        elif value==SpecialCondEnum.LIGHT_SCREEN:
            return '被光墙包围'
        elif value==SpecialCondEnum.REFLECT:
            return '被反射壁包围'

    @classmethod
    def Discription(cls,value):
        if value == SpecialCondEnum.CONFUSION:
            return '混乱中攻击了自身'
        elif value==SpecialCondEnum.BOUND:
            return '被紧紧束缚，无法脱身'
        elif value==SpecialCondEnum.FORCED:
            return '处于强制攻击状态'
        elif value==SpecialCondEnum.STIFF:
            return '处于僵硬状态，无法行动'
        elif value==SpecialCondEnum.PARASITIC:
            return '被寄生种子寄生了'
        elif value==SpecialCondEnum.LIGHT_SCREEN:
            return '被光墙包围，特殊攻击伤害减弱'
        elif value==SpecialCondEnum.REFLECT:
            return '被反射壁包围，物理攻击伤害减弱'

    @classmethod
    def BackToNormal(cls,value):
        if value == SpecialCondEnum.CONFUSION:
            return '从混乱中解除了'
        elif value==SpecialCondEnum.BOUND:
            return '从束缚中挣脱了'
        elif value==SpecialCondEnum.FORCED:
            return ''
        elif value==SpecialCondEnum.STIFF:
            return '身体的僵硬感解除了'
        elif value==SpecialCondEnum.PARASITIC:
            return '身上的寄生种子消失了'
        elif value==SpecialCondEnum.LIGHT_SCREEN:
            return '光墙消失了'
        elif value==SpecialCondEnum.REFLECT:
            return '反射壁消失了'
        

class StageEnum(IntEnum):
    ATTACK=0,
    DEFENSE=1,
    SPECIAL_ATTACK=2,
    SPECIAL_DEFENSE=3,
    SPEED=4,
    HIT=5,
    DODGE=6,
    CRITICAL_HITS=7
    @classmethod
    def ToChinese(cls,value):
        if value==StageEnum.ATTACK:
            return '攻击力'
        elif value==StageEnum.DEFENSE:
            return '防御力'
        elif value==StageEnum.SPECIAL_ATTACK:
            return '特攻'
        elif value==StageEnum.SPECIAL_DEFENSE:
            return '特防'
        elif value==StageEnum.SPEED:
            return '速度'
        elif value==StageEnum.HIT:
            return '命中率'
        elif value==StageEnum.DODGE:
            return '闪避'
        elif value==StageEnum.CRITICAL_HITS:
            return '易中要害'

class PositionEnum(IntEnum):
    PLAYGROUND=0,
    UNDERGROUND=1,
    SKY=2

class WeatherEnum(IntEnum):
    NORMAL=0,
    MIST=1,
    SUN=2,
    RAIN=3

    def __str__(self):
        return WeatherEnum.ToChinese(self)
    
    @classmethod
    def IsNormal(cls,value):
        return value == WeatherEnum.NORMAL

    @classmethod
    def Discription(cls,value):
        if value == WeatherEnum.NORMAL:
            return '天气回复了晴朗'
        elif value==WeatherEnum.MIST:
            return '雾很浓'
        elif value==WeatherEnum.SUN:
            return '日照很强'
        elif value==WeatherEnum.RAIN:
            return '雨继续下'

    @classmethod
    def ToChinese(cls,value):
        if value==WeatherEnum.NORMAL:
            return '正常'
        elif value==WeatherEnum.MIST:
            return '白雾'
        elif value==WeatherEnum.SUN:
            return '大晴天'
        elif value==WeatherEnum.RAIN:
            return '下雨'

    
        