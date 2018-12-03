from enum import IntEnum,Enum,unique

try:
    @unique
    class TypeEnum(IntEnum):
        NORMAL=1,
        FIGHT=2,
        FLYING=4,
        POISION=8,
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
            elif type==TypeEnum.POISION:
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


