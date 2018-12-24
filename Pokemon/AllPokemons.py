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

class Dragonite(PokemonBase):
    def __init__(self):
        name='快龙'
        file_stats=pk_path+'StoreFiles/'+name+'/Stat.csv'
        stat=Stat(file_stats)
        indiv_values=IndivValues()
        PokemonBase.__init__(self,stat,indiv_values,type=TypeEnum.DRAGON+TypeEnum.FLYING,name=name)

class Dragonite(PokemonBase):
    def __init__(self):
        name='暴鲤龙'
        file_stats=pk_path+'StoreFiles/'+name+'/Stat.csv'
        stat=Stat(file_stats)
        indiv_values=IndivValues()
        PokemonBase.__init__(self,stat,indiv_values,type=TypeEnum.WATER+TypeEnum.FLYING,name=name)

class Dragonair(PokemonBase):
    def __init__(self):
        name='哈克龙'
        file_stats=pk_path+'StoreFiles/'+name+'/Stat.csv'
        stat=Stat(file_stats)
        indiv_values=IndivValues()
        PokemonBase.__init__(self,stat,indiv_values,type=TypeEnum.DRAGON,name=name)


class Dewgong(PokemonBase):
    def __init__(self):
        name='白海狮'
        file_stats=pk_path+'StoreFiles/'+name+'/Stat.csv'
        stat=Stat(file_stats)
        indiv_values=IndivValues()
        PokemonBase.__init__(self,stat,indiv_values,type=TypeEnum.WATER+TypeEnum.ICE,name=name)


class Lapras(PokemonBase):
    def __init__(self):
        name='乘龙'
        file_stats=pk_path+'StoreFiles/'+name+'/Stat.csv'
        stat=Stat(file_stats)
        indiv_values=IndivValues()
        PokemonBase.__init__(self,stat,indiv_values,type=TypeEnum.WATER+TypeEnum.ICE,name=name)


class Cloyster(PokemonBase):
    def __init__(self):
        name='刺甲贝'
        file_stats=pk_path+'StoreFiles/'+name+'/Stat.csv'
        stat=Stat(file_stats)
        indiv_values=IndivValues()
        PokemonBase.__init__(self,stat,indiv_values,type=TypeEnum.WATER+TypeEnum.ICE,name=name)



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