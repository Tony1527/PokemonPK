from Team import *
from AllPokemons import *
from Player import Player

g_globals.update(globals())



package=Package()
package.append(FullRestore(5))
package.append(FullHeal(5))
package.append(MaxRevive(3))

class XiaoChi(Team):
    def __init__(self):
        Team.__init__(self,Player('小赤'))
        self.SetPackage(package)
        self.SetPokemons(['妙蛙花','喷火龙','水箭龟','卡比兽','化石翼龙','皮卡丘'])
        self.SetPokemonsSkills()

# xiao_chi=Team()
# xiao_chi.SetPackage(package)
# xiao_chi.SetPokemons(['妙蛙花','喷火龙','水箭龟','卡比兽','化石翼龙','皮卡丘'])
# xiao_chi.SetPokemonsSkills(auto_learn=True)