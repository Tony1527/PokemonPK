from pk_utility import *
from AllPokemons import *
from Package import *
from PMList import *
from Player import *
import copy

class Team(object):
    def __init__(self,player):
        self.player=player
        self.package=None
        self.pm_list=None
    def SetPokemons(self,pokemon_names=[],levels=[50,50,50,50,50,60]):
        if len(pokemon_names)!=len(levels):
            raise ValueError('length of pokemon_names is not equal to level\'s')
        
        pokemons=[GetObjByChineseName(name) for name in pokemon_names]
        self.pm_list=PMList()
        for pm in pokemons:
            self.pm_list.append(pm)
        for i in range(len(pokemons)):
            pokemons[i].Grow(levels[i])
        self.pm_list.SetPlayer(self.player)
    def SetPackage(self,package):
        self.package=copy.deepcopy(package)
        self.package.SetPlayer(self.player)
    def SetPokemonsSkills(self,skills=[[]],auto_learn=False):
        if auto_learn==True:
            for i in range(len(self.pm_list)):
                self.pm_list[i].LearnSkills(auto_learn=True)
        else:
            for i in range(len(self.pm_list)):
                if i>=len(skills) or len(skills[i])==0:
                    self.pm_list[i].LearnSkills(auto_learn=True)
                else:
                    self.pm_list[i].LearnSkills(skills[i])
    

