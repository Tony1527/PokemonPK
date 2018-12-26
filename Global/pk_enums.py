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
        @classmethod
        def ToChinese(cls,type):
            if type==TypeEnum.NORMAL:
                return '一般'
            elif type==TypeEnum.FIGHT:
                return '格斗'
            elif type==TypeEnum.FLYING:
                return '飞行'
            elif type==TypeEnum.POISON:
                return '毒'
            elif type==TypeEnum.GROUND:
                return '地'
            elif type==TypeEnum.ROCK:
                return '岩石'
            elif type==TypeEnum.BUG:
                return '虫'
            elif type==TypeEnum.FIRE:
                return '火'
            elif type==TypeEnum.WATER:
                return '水'
            elif type==TypeEnum.GRASS:
                return '草'
            elif type==TypeEnum.ELECTR:
                return '电'
            elif type==TypeEnum.PSYCHC:
                return '超能力'
            elif type==TypeEnum.ICE:
                return '冰'
            elif type==TypeEnum.DRAGON:
                return '龙'
except ValueError as e:
    print(e)



class CategoryEnum(IntEnum):
    PHYSICS=0,
    SPECIAL=1
    @classmethod
    def ToChinese(cls,category):
        if category==PHYSICS:
            return '物理'
        elif category==SPECIAL:
            return '特殊'

class StatusCondEnum(IntEnum):
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
    def ToChinese(cls,stat_condition):
        if stat_condition==StatusCondEnum.NORMAL:
            return '正常'
        elif stat_condition==StatusCondEnum.BURN:
            return '烧伤'
        elif stat_condition==StatusCondEnum.FREEZE:
            return '冻伤'
        elif stat_condition==StatusCondEnum.PARALYSIS:
            return '麻痹'
        elif stat_condition==StatusCondEnum.POISON:
            return '中毒'
        elif stat_condition==StatusCondEnum.BADLYPOISON:
            return '剧毒'
        elif stat_condition==StatusCondEnum.SLEEP:
            return '睡觉'

class SpecialCondEnum(IntEnum):
    CONFUSION=0
    BOUND=1
    FORCED=2

    @classmethod
    def ToChinese(cls,value):
        if value==SpecialCondEnum.CONFUSION:
            return '混乱'
        elif value==SpecialCondEnum.BOUND:
            return '被束缚'
        elif value==SpecialCondEnum.FORCED:
            return '强制攻击'


class StageEnum(IntEnum):
    ATTACK=0,
    DEFENSE=1,
    SPECIAL_ATTACK=2,
    SPECIAL_DEFENSE=3,
    SPEED=4,
    HIT=5,
    DODGE=6
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

class PositionEnum(IntEnum):
    PLAYGROUND=0,
    UNDERGROUND=1,
    SKY=2

    