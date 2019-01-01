from pk_enums import *
from PokemonBase import *

'''
    恢复所有状态
'''
def RecoverAll(pokemon):
    RecoverStage(pokemon)
    RecoverStatusCond(pokemon)
    RecoverHP(pokemon)

'''
    恢复HP
'''
def RecoverAllHP(pokemon):
    pokemon.hp=pokemon.HP()

'''
    恢复部分HP
'''
def RecoverHP(pokemon,value):
    if pokemon.hp!=0:
        if pokemon.hp+value>pokemon.HP():
            pokemon.hp=pokemon.HP()
            return value-pokemon.hp+pokemon.HP()
        else:
            pokemon.hp=pokemon.hp+value
            return value
    else:
        return False

'''
    恢复能力阶级
'''
def RecoverStage(pokemon):
    pokemon.stage.Clear()


'''
    恢复异常状态
'''
def RecoverStatusCond(pokemon):
    pokemon.status_cond=StatusCondEnum.NORMAL
