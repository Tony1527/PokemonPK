import os
import sys

a=os.getcwd()
pk_path = a+"/PokemonPK/"
sys.path.append(pk_path+"Global")
sys.path.append(pk_path+"Pokemon")
sys.path.append(pk_path+"Package")
sys.path.append(pk_path+"Skills")
sys.path.append(pk_path+"StoreFiles")

from PokemonPK.Pokemon import AllPokemons

from PokemonPK.Global import *
from PokemonPK.Pokemon import *
from PokemonPK.Skills import *
from PokemonPK.Package import *


g_globals.update(globals())
