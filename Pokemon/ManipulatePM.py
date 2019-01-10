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
            Console.msg('似乎对对方没有造成什么伤害')
            return
        elif damage==-1:
            return
        delay_val=0
        damage_step=1
        while delay_val<damage:
            Hurt(target,damage_step)
            Console.msg('',is_clean=True,sleep_time=0.05)
            # Console.msg('{}...'.format(delay_val),is_clean=True)
            delay_val = delay_val+damage_step
            
            if not target.IsAlive():
                break
        if delay_val>damage and target.IsAlive():
            Hurt(target,damage-(delay_val-damage_step))
        Console.msg('{}受到了{}点伤害'.format(target.GetName(),damage))
        if not target.IsAlive():
            Console.msg(target.GetName()+'倒下了')
