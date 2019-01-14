# PokemonPK
基于Python的第一代宝可梦对战系统

## 依赖的库和环境
    Windows7及以上
    python3
    numpy
    pandas
    
## 安装
`
git clone https://github.com/Tony1527/PokemonPK.git
`

## 示例
开始对战只需如下设置即可
```
from PokemonPK import *

#新建队伍
our_tm=XiaoChi()
enemy_tm=ADu()

#新建对战系统
r=Rounds(our_tm,enemy_tm)

#进行对战
r.Run()
```

## 说明
PokemonPK由来是因为我在教朋友Python，然后本打算以游戏的形式启发他学习，不过我发现实现起来还是有点难，所以自己先写了一个。

PokemonPK是以口袋妖怪第一代对战系统为蓝本的回合制单机游戏，玩家可以扮演赤红来挑战对手。PokemonPK在作战系统上完全参考[wiki.52poke.com](wiki.52poke.com),感谢该部落的无私奉献。

游戏中由于加入了自己该写过的playsound库，所以只支持在Window7及以上的操作系统运行，暂不支持Linux和Mac

