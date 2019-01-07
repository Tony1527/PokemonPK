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


'''
    受到伤害后检查是否宝可梦处于濒死状态
'''
def Hurt(pokemon,damage=0,percent=0):
    if percent!=0:
        pokemon.hp = pokemon.hp - pokemon.HP()*percent    
    if damage!=0:
        pokemon.hp=pokemon.hp-damage
    if pokemon.hp<0:
        pokemon.hp=0
    return pokemon.hp


def ApplyDamage(target,damage):
        damage = int(damage)
        if damage==0:
            print('似乎对对方没有造成什么伤害')
            return
        elif damage==-1:
            return
        delay_val=50
        while delay_val<damage:
            print('{}...'.format(delay_val))
            delay_val = delay_val+10
            if delay_val>=target.hp:
                break
            rest()
        print('{}受到了{}点伤害'.format(target.GetName(),damage))
        if Hurt(target,damage)==0:
            print(target.GetName()+'倒下了')
