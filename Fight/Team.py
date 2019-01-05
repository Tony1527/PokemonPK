from pk_utility import *
from AllPokemons import *
from Package import *

class Team(object):
    def __init__(self,player,pm_list,package):
        self.pm_list=pm_list
        self.package=package
        self.player=player
        self.pm_list.SetPlayer(player)