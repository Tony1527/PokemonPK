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
def RecoverHP(pokemon):
    pokemon.hp=pokemon.HP()


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
