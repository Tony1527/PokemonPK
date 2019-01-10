from Team import *
from AllPokemons import *


pokemon_names=['妙蛙花','喷火龙','水箭龟','卡比兽','化石翼龙','皮卡丘']
levels=[50,50,50,50,50,60]
pokemons=[GetObjByChineseName(name) for name in pokemon_names]
skills=[
    [],
    [],
    [],
    [],
    [],
    []
]
pm_list=PMList()
for pm in pokemons:
    pm_list.append(pm)

for i in range(len(pokemons)):
    pokemons.Grow(levels[i])

package=Package()
package.append(FullRestore(5))
package.append(FullHeal(5))
package.append(MaxRevive(3))

for i in range(len(pokemons)):
    if len(skills[i])==0:
        pokemons[i].LearnSkills(auto_learn=True)
    else:
        pokemons[i].LearnSkills(skills[i])

xiao_chi=Team(Player('小赤'),pm_list,package)