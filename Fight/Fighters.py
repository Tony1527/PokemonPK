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
        Team.__init__(self,Player('赤红'))
        self.SetPackage(package)
        self.SetPokemons(['妙蛙花','乘龙','喷火龙','水箭龟','卡比兽','皮卡丘'])
        self.SetPokemonsSkills([['催眠粉','污泥攻击','日光束','超级吸取'],['泰山压顶','暴风雪','精神强念','冲浪'],['喷射火焰','劈开','翅膀攻击','火焰旋涡'],['暴风雪','冲浪','火箭头锤','水炮'],['地震','泰山压顶','睡觉','破坏光线'],['电光一闪','十万伏特','打雷','电电加速']])

class ADu(Team):
    def __init__(self):
        player=Player('阿渡')
        player.SetMockingSentences(['你有资格成为宝可梦联盟的冠军吗？','少年，我爱上了你那熊熊燃烧的斗志','你能战胜我吗？','你渴望力量吗？','是时候拿出我真正的实力了！','面对龙的怒吼吧！','轮到我的回合了！'],[])
        Team.__init__(self,player)
        self.SetPackage(package)
        
        self.SetPokemons(['暴鲤龙','化石翼龙','哈克龙','哈克龙','喷火龙','快龙'])
        self.SetPokemonsSkills([['水炮','龙之怒','破坏光线','瞪眼'],['超音波','咬住','岩崩','破坏光线'],['十万伏特','摔打','电磁波','破坏光线'],['泡沫光线','紧束','冰冻光束','破坏光线'],['喷射火焰','劈开','翅膀攻击','破坏光线'],['暴风雪','大字爆炎','打雷','破坏光线']])
