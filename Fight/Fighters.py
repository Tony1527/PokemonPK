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
        self.SetPokemonsSkills([['破坏光线']])

class ADu(Team):
    def __init__(self):
        Team.__init__(self,Player('阿渡'))
        self.SetPackage(package)
        self.SetPokemons(['化石翼龙'],[1,1,1,1,1])
        # self.SetPokemons(['化石翼龙','哈克龙','暴鲤龙','哈克龙','快龙'],[1,1,1,1,1])
        self.SetPokemonsSkills()
