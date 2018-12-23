from PokemonBase import *

class Charizard(PokemonBase):
    def __init__(self):
        name='喷火龙'
        file_stats=pk_path+'StoreFiles/'+name+'/Stat.csv'
        stat=Stat(file_stats)
        indiv_values=IndivValues()
        PokemonBase.__init__(self,stat,indiv_values,type=TypeEnum.FIRE,name=name)