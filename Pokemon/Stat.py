from pk_utility import *

class Stat(object):
    hp=0
    attack=0
    defense=0
    special_attack=0
    special_defense=0
    speed=0
    def __init__(self,file_path):
        file_stats=open(file_path)
        data = pd.read_csv(file_stats)
        file_stats.close()
        data.index=data['Stat'].values
        print(data)
        self.hp = data.loc['HP']['Value']
        self.attack = data.loc['Attack']['Value']
        self.defense = data.loc['Defense']['Value']
        self.special_attack = data.loc['Sp.Atk']['Value']
        self.special_defense = data.loc['Sp.Def']['Value']
        self.speed = data.loc['Speed']['Value']


class IndivValues(object):
    hp=0
    attack=0
    defense=0
    special=0
    speed=0
    def __init__(self,attack=9,defense=8,special=8,speed=8):
        if attack >15 or defense >15 or special >15 or speed >15:
            raise PokemonPKError('Invalid Individual Values Found!')
        self.attack = attack
        self.defense = defense
        self.special = special
        self.speed = speed
        if attack%2:
            self.hp = self.hp+8
        if defense%2:
            self.hp = self.hp+4
        if speed%2:
            self.hp = self.hp+2
        if special%2:
            self.hp = self.hp+1
        