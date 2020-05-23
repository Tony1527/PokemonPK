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
    if pokemon.hp==pokemon.HP():
        return 0
    return ApplyDamage(pokemon,-pokemon.HP(),True)

'''
    恢复部分HP
'''
def RecoverHP(pokemon,value):
    if pokemon.hp==pokemon.HP():
        return 0
    value=int(value)
    return ApplyDamage(pokemon,-value,True)

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
    受到伤害/治疗
'''
def AffectHP(pokemon,damage=0,percent=0):
    ret_val=0
    is_alive=True
    is_full=True
    if percent!=0:
        damage=pokemon.HP()*percent
    if damage>0:
        is_full=False
        if not pokemon.IsAlive():
            ret_val=0
            is_alive=False
        elif pokemon.hp-damage<=0:
            ret_val = pokemon.hp
            pokemon.hp=0
            is_alive=False
        else:
            ret_val = damage
            pokemon.hp=pokemon.hp-ret_val
            is_alive=True
    elif damage<0:
        is_alive=True
        if pokemon.HP()==pokemon.hp:
            ret_val=0
            is_full=True
        elif pokemon.hp-damage>=pokemon.HP():
            ret_val = pokemon.hp-pokemon.HP()
            pokemon.hp=pokemon.HP()
            is_full=True
        else:
            ret_val = damage
            pokemon.hp=pokemon.hp-ret_val
            is_full=False

            
    return (ret_val,is_alive,is_full)


def ApplyDamage(target,damage,is_recover=False):
        damage = int(damage)
        if is_recover==False:
            if damage==0:
                Console.msg('似乎对'+target.GetName()+'没有造成什么效果')
                return
            elif damage<0:
                return
        else:
            if damage>=0:
                return
        delay_val=0
        if is_recover==False:
            damage_step=1
        else:
            damage_step=-1 #absorb

        while delay_val*damage_step<damage*damage_step:
            (value,is_alive,is_full)=AffectHP(target,damage_step)
            Console.refresh()
            if value!=0:
                delay_val = delay_val+damage_step
            if (not is_alive) or is_full:
                break
            
            # Console.msg('{}...'.format(delay_val),is_clean=True)
            
            
            
        #if delay_val>damage and target.IsAlive():
        #    Hurt(target,damage-(delay_val-damage_step))
        if is_recover==False:
            Console.msg('{}受到了{}点HP'.format(target.GetName(),delay_val))
        else:
            Console.msg('{}恢复了{}点HP'.format(target.GetName(),-delay_val))
        if not target.IsAlive():
            Console.msg(target.GetName()+'倒下了')
        return damage_step*delay_val
