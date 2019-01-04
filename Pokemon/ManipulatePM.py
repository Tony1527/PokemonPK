from pk_enums import *
from PokemonBase import *

'''
    恢复所有状态
'''
def RecoverAll(pokemon):
    recover_value = RecoverAllHP(pokemon)
    retstat=RecoverStatusCond(pokemon)
    return recover_value,retstat
'''
    恢复HP
'''
def RecoverAllHP(pokemon):
    recover_value=pokemon.HP()-pokemon.hp
    pokemon.hp=pokemon.HP()
    return str(recover_value)

'''
    恢复部分HP
'''
def RecoverHP(pokemon,value):
    value=int(value)
    recover_value=0
    if pokemon.hp!=0:
        if pokemon.hp+value>=pokemon.HP():
            recover_value = pokemon.HP()-pokemon.hp
            pokemon.hp=pokemon.HP()
        else:
            pokemon.hp=pokemon.hp+value
            recover_value =  value
    
    return str(recover_value)

'''
    恢复能力阶级
'''
def RecoverStage(pokemon):
    pokemon.stage.Clear()
    return True


'''
    恢复异常状态
'''
def RecoverStatusCond(pokemon):
    if pokemon.status_cond.IsNormal():
        return False
    else:
        pokemon.status_cond.Clear()
        return True
