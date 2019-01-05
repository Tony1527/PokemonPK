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


def SkillChoose(pokemon):
    print('===============')
    print('选择招式')
    while True:
        pokemon.PrintSkills()
        choice=input('请选择你要使用的技能(输入0返回)：')
        choice=a2i(choice,0,len(pokemon.skills))
        if choice==-1:
            return None
        elif choice<len(pokemon.skills) and choice>=0:
            if pokemon.skills[choice].pp>0:
                return pokemon.skills[choice]
            else:
                struggle_flag=True
                for skill in pokemon.skills:
                    if skill.pp>0:
                        struggle_flag=False
                if struggle_flag:
                    return Struggle()
                else:
                    print('该招式已经用完，请选择其他技能')
        else:
            pass
