from PokemonBase import *

class Charizard(PokemonBase):
    def __init__(self):
        name='喷火龙'
        file_stats=pk_path+'StoreFiles/'+name+'/Stat.csv'
        stat=Stat(file_stats)
        indiv_values=IndivValues()
        PokemonBase.__init__(self,stat,indiv_values,type=TypeEnum.FIRE+TypeEnum.FLYING,name=name)


class Snorlax(PokemonBase):
    def __init__(self):
        name='卡比兽'
        file_stats=pk_path+'StoreFiles/'+name+'/Stat.csv'
        stat=Stat(file_stats)
        indiv_values=IndivValues()
        PokemonBase.__init__(self,stat,indiv_values,type=TypeEnum.NORMAL,name=name)

class Aerodactyl(PokemonBase):
    def __init__(self):
        name='化石翼龙'
        file_stats=pk_path+'StoreFiles/'+name+'/Stat.csv'
        stat=Stat(file_stats)
        indiv_values=IndivValues()
        PokemonBase.__init__(self,stat,indiv_values,type=TypeEnum.ROCK+TypeEnum.FLYING,name=name)

class Pikachu(PokemonBase):
    def __init__(self):
        name='皮卡丘'
        file_stats=pk_path+'StoreFiles/'+name+'/Stat.csv'
        stat=Stat(file_stats)
        indiv_values=IndivValues()
        PokemonBase.__init__(self,stat,indiv_values,type=TypeEnum.ELECTR,name=name)


class Blastoise(PokemonBase):
    def __init__(self):
        name='水箭龟'
        file_stats=pk_path+'StoreFiles/'+name+'/Stat.csv'
        stat=Stat(file_stats)
        indiv_values=IndivValues()
        PokemonBase.__init__(self,stat,indiv_values,type=TypeEnum.WATER,name=name)

class Venusaur(PokemonBase):
    def __init__(self):
        name='妙蛙花'
        file_stats=pk_path+'StoreFiles/'+name+'/Stat.csv'
        stat=Stat(file_stats)
        indiv_values=IndivValues()
        PokemonBase.__init__(self,stat,indiv_values,type=TypeEnum.GRASS+TypeEnum.POISON,name=name)


pokemons_dir={
    '喷火龙':'Charizard',
    '卡比兽':'Snorlax',
    '妙蛙花':'Venusaur',
    '化石翼龙':'Aerodactyl',
    '水箭龟':'Blastoise',
    '皮卡丘':'Pikachu',
}
g_c2e.update(pokemons_dir)
del pokemons_dir