# from Stat import *
from SkillBase import *
from SkillFamalies import *
from ManipulatePM import *

class Pound(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Pound'))

class KarateChop(EasyCriticalHitSkill):
    def __init__(self):
        EasyCriticalHitSkill.__init__(self,SkillChart.GetSkillSeries('KarateChop'))
    

class DoubleSlap(MultiHitSkill):
    def __init__(self):
        MultiHitSkill.__init__(self,SkillChart.GetSkillSeries('DoubleSlap'))

class CometPunch(MultiHitSkill):
    def __init__(self):
        MultiHitSkill.__init__(self,SkillChart.GetSkillSeries('CometPunch'))

class MegaPunch(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('MegaPunch'))

class PayDay(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('PayDay'))

class FirePunch(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('FirePunch'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,0.1,StatusCondEnum.BURN)

class IcePunch(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('IcePunch'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)

    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,0.1,StatusCondEnum.FREEZE)

class ThunderPunch(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('ThunderPunch'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)

    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,0.1,StatusCondEnum.PARALYSIS)

class Scratch(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Scratch'))


class ViceGrip(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('ViceGrip'))


class Guillotine(MustKillSkill):
    def __init__(self):
        MustKillSkill.__init__(self,SkillChart.GetSkillSeries('Guillotine'))

class RazorWind(StockpileSkill,EasyCriticalHitSkill):
    def __init__(self):
        StockpileSkill.__init__(self,SkillChart.GetSkillSeries('RazorWind'),discription='蓄力中')

class SwordsDance(SrcBuffUp):
    def __init__(self):
        SrcBuffUp.__init__(self,SkillChart.GetSkillSeries('SwordsDance'),StageEnum.ATTACK,2)
    


class Cut(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Cut'))


class Gust(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Gust'))
    def IsHit(self,src,target,weather):
        if target.position==PositionEnum.UNDERGROUND:
            return False
        else:
            return SkillBase.IsHit(self,src,target,weather)
    
    def ApplyTarget(self,src,target,weather):
        if target.position==PositionEnum.SKY:
            return self.DamageCal(src,target,weather)*2
        else:
            return self.DamageCal(src,target,weather)


class WingAttack(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('WingAttack'))

class Whirlwind(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('WhirlWind'),ObjOfAction.TAR_ABL)
        self._priority=-6

class Fly(StockpileSkill):
    def __init__(self):
        StockpileSkill.__init__(self,SkillChart.GetSkillSeries('Fly'),PositionEnum.SKY,'飞上了高空')


class Bind(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Bind'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseSpecialCond(target,1,SpecialCondEnum.BOUND)


class Slam(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Slam'))


class VineWhip(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('VineWhip'))


class Stomp(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Stomp'))


class DoubleKick(MultiHitSkill):
    def __init__(self):
        MultiHitSkill.__init__(self,SkillChart.GetSkillSeries('doublekick'),2)


class MegaKick(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('megakick'))


class JumpKick(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('jumpkick'))
    def SideEffect(self,src,target):
        Console.msg(src.GetName()+'受到副作用')
        target_damage = self.ApplyTarget(src,target,None)
        ApplyDamage(src,target_damage//8)


class RollingKick(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('rollingkick'))


class SandAttack(TargetBuffDown):
    def __init__(self):
        TargetBuffDown.__init__(self,SkillChart.GetSkillSeries('sandattack'),StageEnum.HIT,1)
    

class Headbutt(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('headbutt'))


class HornAttack(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('HornAttack'))


class FuryAttack(MultiHitSkill):
    def __init__(self):
        MultiHitSkill.__init__(self,SkillChart.GetSkillSeries('furyattack'))


class HornDrill(MustKillSkill):
    def __init__(self):
        MustKillSkill.__init__(self,SkillChart.GetSkillSeries('horndrill'))


class Tackle(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('tackle'))


class BodySlam(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('bodyslam'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,0.3,StatusCondEnum.PARALYSIS)


class Wrap(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('wrap'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseSpecialCond(target,1,SpecialCondEnum.BOUND)


class TakeDown(ReboundSkill):
    def __init__(self):
        ReboundSkill.__init__(self,SkillChart.GetSkillSeries('takedown'),1/4)

class Thrash(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Thrash'),ObjOfAction.TAR+ObjOfAction.SRC_ABL)
    def ApplySrcAblity(self,src):
        self.CauseSpecialCond(src,1,SpecialCondEnum.FORCED,np.random.randint(2,4))


class DoubleEdge(ReboundSkill):
    def __init__(self):
        ReboundSkill.__init__(self,SkillChart.GetSkillSeries('doubleedge'),1/3)


class TailWhip(TargetBuffDown):
    def __init__(self):
        TargetBuffDown.__init__(self,SkillChart.GetSkillSeries('TailWhip'),StageEnum.DEFENSE,1)
        



class PoisonSting(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('poisonsting'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,0.3,StatusCondEnum.POISON)



class Twineedle(MultiHitSkill):
    def __init__(self):
        MultiHitSkill.__init__(self,SkillChart.GetSkillSeries('twineedle'),2)


class PinMissile(MultiHitSkill):
    def __init__(self):
        MultiHitSkill.__init__(self,SkillChart.GetSkillSeries('pinmissile'))


class Leer(TargetBuffDown):
    def __init__(self):
        TargetBuffDown.__init__(self,SkillChart.GetSkillSeries('leer'),StageEnum.DEFENSE,1)
        


class Bite(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('bite'))


class Growl(TargetBuffDown):
    def __init__(self):
        TargetBuffDown.__init__(self,SkillChart.GetSkillSeries('growl'),StageEnum.ATTACK,1)
        


class Roar(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('roar'),ObjOfAction.TAR_ABL)
        self._priority=-6


class Sing(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Sing'),ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,1,StatusCondEnum.SLEEP,is_print=True)


class Supersonic(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('supersonic'),ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseSpecialCond(target,1,SpecialCondEnum.CONFUSION,is_print=True)


class SonicBoom(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('SonicBoom'))
    def ApplyTarget(self,src,target,weather):
        return 20
    def IsHit(self,src,target,weather):
        rand_value = np.random.randint(1,256)
        hit_value=g_skill_hit[self._hit]*src.stage.Get(StageEnum.HIT)/target.stage.Get(StageEnum.DODGE)
        return rand_value<hit_value

#Deprecated
# class Disable(SkillBase):
#     def __init__(self):
#         SkillBase.__init__(self,SkillChart.GetSkillSeries('Disable'))


class Acid(TargetBuffDown):
    def __init__(self):
        TargetBuffDown.__init__(self,SkillChart.GetSkillSeries('acid'),StageEnum.SPECIAL_DEFENSE,1,0.1,ObjOfAction.TAR+ObjOfAction.TAR_ABL)

            


class Ember(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('ember'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,0.1,StatusCondEnum.BURN)

class Flamethrower(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('flamethrower'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,0.1,StatusCondEnum.BURN)


class Mist(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('mist'),ObjOfAction.WEATHER)

    def ApplyWeather(self,weather):
        if weather!=WeatherEnum.MIST:
            weather.Set(WeatherEnum.MIST,5)
            Console.msg('场地四周升起了白雾')
        else:
            Console.msg('似乎没有什么效果')
class WaterGun(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('watergun'))


class HydroPump(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('HydroPump'))


class Surf(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('surf'))


class IceBeam(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('IceBeam'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,0.1,StatusCondEnum.FREEZE)

class Blizzard(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('blizzard'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,0.1,StatusCondEnum.FREEZE)


class Psybeam(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('psybeam'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseSpecialCond(target,0.1,SpecialCondEnum.CONFUSION)


class BubbleBeam(TargetBuffDown):
    def __init__(self):
        TargetBuffDown.__init__(self,SkillChart.GetSkillSeries('bubblebeam'),StageEnum.SPEED,1,1,ObjOfAction.TAR+ObjOfAction.TAR_ABL)



class AuroraBeam(TargetBuffDown):
    def __init__(self):
        TargetBuffDown.__init__(self,SkillChart.GetSkillSeries('aurorabeam'),StageEnum.ATTACK,1,0.1,ObjOfAction.TAR+ObjOfAction.TAR_ABL)


class HyperBeam(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('hyperbeam'),ObjOfAction.TAR+ObjOfAction.SRC_ABL)
    def ApplySrcAblity(self,src):
        self.CauseSpecialCond(src,1,SpecialCondEnum.STIFF,2)


class Peck(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('peck'))


class DrillPeck(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('drillpeck'))


class Submission(ReboundSkill):
    def __init__(self):
        ReboundSkill.__init__(self,SkillChart.GetSkillSeries('submission'),1/4)


class LowKick(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('lowkick'))
    def ApplyTarget(self,src,target,weather):
        return src.level


class Counter(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('counter'))
        self._priority=-5
    def ApplyTarget(self,src,target,weather):
        return src.last_round.suffer_damage*2


class SeismicToss(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('seismictoss'))
    def ApplyTarget(self,src,target,weather):
        return src.level


class Strength(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('strength'))


class Absorb(AbsorbSkill):
    def __init__(self):
        AbsorbSkill.__init__(self,SkillChart.GetSkillSeries('absorb'))


class MegaDrain(AbsorbSkill):
    def __init__(self):
        AbsorbSkill.__init__(self,SkillChart.GetSkillSeries('megadrain'))


class LeechSeed(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('leechseed'),ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseSpecialCond(target,1,SpecialCondEnum.PARASITIC,4,is_print=True)


class Growth(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('growth'),ObjOfAction.SRC_ABL)
    def ApplySrcAblity(self,src):
        src.Up(StageEnum.ATTACK,1)
        src.Up(StageEnum.SPECIAL_ATTACK,1)

class RazorLeaf(EasyCriticalHitSkill):
    def __init__(self):
        EasyCriticalHitSkill.__init__(self,SkillChart.GetSkillSeries('RazorLeaf'))


class SolarBeam(StockpileSkill):
    def __init__(self):
        StockpileSkill.__init__(self,SkillChart.GetSkillSeries('SolarBeam'),discription='吸收了阳光...')
    

class PoisonPowder(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('PoisonPowder'),ObjOfAction.TAR_ABL)

    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,1,StatusCondEnum.POISON,is_print=True)


class StunSpore(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('StunSpore'),ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,1,StatusCondEnum.PARALYSIS,is_print=True)

class SleepPowder(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('SleepPowder'),ObjOfAction.TAR_ABL)

    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,1,StatusCondEnum.SLEEP,is_print=True)



class PetalDance(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('PetalDance'))


class StringShot(TargetBuffDown):
    def __init__(self):
        TargetBuffDown.__init__(self,SkillChart.GetSkillSeries('stringshot'),StageEnum.SPEED,2)


class DragonRage(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('DragonRage'))
    def ApplyTarget(self,src,target,weather):
        return 40


class FireSpin(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('firespin'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseSpecialCond(target,1,SpecialCondEnum.BOUND,is_print=True)


class ThunderShock(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('ThunderShock'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,0.1,StatusCondEnum.PARALYSIS)

class Thunderbolt(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Thunderbolt'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,0.1,StatusCondEnum.PARALYSIS)

class ThunderWave(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('thunderwave'),ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,1,StatusCondEnum.PARALYSIS,is_print=True)

class Thunder(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Thunder'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,0.3,StatusCondEnum.PARALYSIS)
    
    def IsHit(self,src,target,weather):
        if target.position==PositionEnum.UNDERGROUND:
            return False
        rand_value = np.random.randint(1,256)
        hit_value=g_skill_hit[self._hit]*src.stage.Get(StageEnum.HIT)/target.stage.Get(StageEnum.DODGE)
        if weather==WeatherEnum.SUN:
            return rand_value<0.5*hit_value
        elif weather==WeatherEnum.RAIN:
            return True
        else:
            return rand_value<hit_value


class RockThrow(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('rockthrow'))


class Earthquake(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('earthquake'))
    def ApplyTarget(self,src,target,weather):
        if target.position==PositionEnum.UNDERGROUND:
            return self.DamageCal(src,target,weather)*2
        else:
            return self.DamageCal(src,target,weather)

    def IsHit(self,src,target,weather):
        if target.position==PositionEnum.SKY:
            return False
        else:
            return SkillBase.IsHit(self,src,target,weather)


class Fissure(MustKillSkill):
    def __init__(self):
        MustKillSkill.__init__(self,SkillChart.GetSkillSeries('Fissure'))


class Dig(StockpileSkill):
    def __init__(self):
        StockpileSkill.__init__(self,SkillChart.GetSkillSeries('dig'),PositionEnum.UNDERGROUND,'潜入了地下...')

class Toxic(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Toxic'),ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,1,StatusCondEnum.BADLYPOISON,round=np.random.randint(2,7),is_print=True)

class Confusion(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('confusion'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseSpecialCond(target,0.1,SpecialCondEnum.CONFUSION)


class Psychic(TargetBuffDown):
    def __init__(self):
        TargetBuffDown.__init__(self,SkillChart.GetSkillSeries('psychic'),StageEnum.SPECIAL_DEFENSE,1,0.1,ObjOfAction.TAR+ObjOfAction.TAR_ABL)

class Hypnosis(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('hypnosis'),ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,1,StatusCondEnum.SLEEP,is_print=True)



class Meditate(SrcBuffUp):
    def __init__(self):
        SrcBuffUp.__init__(self,SkillChart.GetSkillSeries('meditate'),StageEnum.ATTACK,1)


class Agility(SrcBuffUp):
    def __init__(self):
        SrcBuffUp.__init__(self,SkillChart.GetSkillSeries('agility'),StageEnum.SPEED,2)


class QuickAttack(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('quickattack'))
        self._priority=1

class Rage(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('rage'),ObjOfAction.SRC_ABL+ObjOfAction.TAR)
    def ApplySrcAblity(self,src):
        self.CauseSpecialCond(src,1,SpecialCondEnum.FORCED,100000000)



class Teleport(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('teleport'))
    def ApplyTarget(self,src,target,weather):
        return 0


class NightShade(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('nightshade'))
    def ApplyTarget(self,src,target,weather):
        return src.level

#Deprecated
# class Mimic(SkillBase):
#     def __init__(self):
#         SkillBase.__init__(self,SkillChart.GetSkillSeries('mimic'))
    
        

class Screech(TargetBuffDown):
    def __init__(self):
        TargetBuffDown.__init__(self,SkillChart.GetSkillSeries('Screech'),StageEnum.SPECIAL_DEFENSE,2)

class DoubleTeam(SrcBuffUp):
    def __init__(self):
        SrcBuffUp.__init__(self,SkillChart.GetSkillSeries('doubleteam'),StageEnum.DODGE,1)

class Recover(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('recover'),ObjOfAction.SRC_ABL)
    def ApplySrcAblity(self,src):
        Console.msg(src.GetName()+'回复了'+str(RecoverHP(src,src.HP()*0.5))+'点HP')


class Harden(SrcBuffUp):
    def __init__(self):
        SrcBuffUp.__init__(self,SkillChart.GetSkillSeries('harden'),StageEnum.DEFENSE,1)


class Minimize(SrcBuffUp):
    def __init__(self):
        SrcBuffUp.__init__(self,SkillChart.GetSkillSeries('minimize'),StageEnum.DODGE,1)   


class Smokescreen(TargetBuffDown):
    def __init__(self):
        TargetBuffDown.__init__(self,SkillChart.GetSkillSeries('smokescreen'),StageEnum.HIT,1)


class ConfuseRay(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('confuseray'),ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseSpecialCond(target,1,SpecialCondEnum.CONFUSION,is_print=True)

class Withdraw(SrcBuffUp):
    def __init__(self):
        SrcBuffUp.__init__(self,SkillChart.GetSkillSeries('withdraw'),StageEnum.DEFENSE,1)

class DefenseCurl(SrcBuffUp):
    def __init__(self):
        SrcBuffUp.__init__(self,SkillChart.GetSkillSeries('DefenseCurl'),StageEnum.DEFENSE,1)

class Barrier(SrcBuffUp):
    def __init__(self):
        SrcBuffUp.__init__(self,SkillChart.GetSkillSeries('Barrier'),StageEnum.DEFENSE,2)


class LightScreen(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('lightscreen'),ObjOfAction.SRC_ABL)
    def ApplySrcAblity(self,src):
        self.CauseSpecialCond(src,1,SpecialCondEnum.LIGHT_SCREEN,5,is_print=True)


class Haze(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('haze'),ObjOfAction.SRC_ABL+ObjOfAction.TAR_ABL)
    def ApplySrcAblity(self,src):
        src.ResetStage()
    def ApplyTargetAblity(self,target,weather):
        target.ResetStage()
    def PostApply(self,src,target,weather):
        Console.msg('场上宝可梦的能力阶级已经重置！')

class Reflect(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('reflect'),ObjOfAction.SRC_ABL)
    def ApplySrcAblity(self,src):
        self.CauseSpecialCond(src,1,SpecialCondEnum.REFLECT,5,is_print=True)


class FocusEnergy(SrcBuffUp):
    def __init__(self):
        SrcBuffUp.__init__(self,SkillChart.GetSkillSeries('focusenergy'),StageEnum.CRITICAL_HITS,2)

class Bide(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('bide'),ObjOfAction.TAR+ObjOfAction.SRC_ABL)
        self._priority=1
    def SetDefault(self):
        self._is_ready=False
        self._round_num=0
        self._damage=0


    def PreApply(self,src,target,weather):
        if self._is_ready==False:
            self._round_num=self._round_num+1
            if self._round_num==1:
                self._damage=0
            else:
                self._damage=self._damage+src.last_round.suffer_damage
            if self._round_num==3:
                self._is_ready=True
                self.pp=self.pp-1
                Console.msg(src.GetName()+'爆发了！')
                return True
            else:
                Console.msg(src.GetName()+'忍耐中...')
            return False
        
        return True
    def ApplyTarget(self,src,target,weather):
        return self._damage*2
    def PostApply(self,src,target,weather):
        if self._is_ready==True:
            self.SetDefault()
    def ApplySrcAblity(self,src):
        src.special_cond.Set(SpecialCondEnum.FORCED,3)
    


class Metronome(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('metronome'))
    def Apply(self,src=None,target=None,weather=None):
        series=SkillChart.GetSkillChart()['ChineseName']
    
        name=series[np.random.randint(len(series))]
        
        while(name=='鹦鹉学舌' or name=='挥指'):
            name=series[np.random.randint(len(series))]
        Console.msg('{}使用{}，挥出了{}'.format(src.GetName(),self._name,name))
        return GetObjByChineseName(name).Apply(src,target,weather)

class MirrorMove(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('MirrorMove'))
    def Apply(self,src=None,target=None,weather=None):
        name=target.last_round.src_skill.GetName()
        if name=='双倍奉还' or name=='挣扎' or name=='鹦鹉学舌' or name=='':
            Console.msg(src.GetName()+'使用鹦鹉学舌失败')
            Console.msg('==============')
            return 0
        else:
            return GetObjByChineseName(name).Apply(src,target,weather)

class SelfDestruct(SelfLossSkill):
    def __init__(self):
        SelfLossSkill.__init__(self,SkillChart.GetSkillSeries('selfdestruct'),1)

class EggBomb(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('eggbomb'))


class Lick(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('lick'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,0.3,StatusCondEnum.PARALYSIS)


class Smog(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('smog'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,0.4,StatusCondEnum.POISON)

class Sludge(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('sludge'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,0.3,StatusCondEnum.POISON)


class BoneClub(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('boneclub'))


class FireBlast(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('fireblast'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,0.1,StatusCondEnum.BURN)



class Waterfall(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('waterfall'))


class Clamp(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('clamp'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseSpecialCond(target,1,SpecialCondEnum.BOUND)


class Swift(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('swift'))


class SkullBash(StockpileSkill):
    def __init__(self):
        StockpileSkill.__init__(self,SkillChart.GetSkillSeries('skullbash'),discription='缩起了脖子',obj_of_action=ObjOfAction.TAR+ObjOfAction.SRC_ABL)
    def ApplySrcAblity(self,src):
        src.Up(StageEnum.DEFENSE,1)


class SpikeCannon(MultiHitSkill):
    def __init__(self):
        MultiHitSkill.__init__(self,SkillChart.GetSkillSeries('spikecannon'))


class Constrict(TargetBuffDown):
    def __init__(self):
        TargetBuffDown.__init__(self,SkillChart.GetSkillSeries('constrict'),StageEnum.SPEED,1,0.1,ObjOfAction.TAR+ObjOfAction.TAR_ABL)


class Amnesia(SrcBuffUp):
    def __init__(self):
        SrcBuffUp.__init__(self,SkillChart.GetSkillSeries('Amnesia'),StageEnum.SPECIAL_DEFENSE,2)


class Kinesis(TargetBuffDown):
    def __init__(self):
        TargetBuffDown.__init__(self,SkillChart.GetSkillSeries('kinesis'),StageEnum.HIT,1)




class SoftBoiled(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('softboiled'),ObjOfAction.SRC_ABL)
    def ApplySrcAblity(self,src):
        Console.msg(src.GetName()+'回复了'+str(RecoverHP(src,src.HP()*0.5))+'点HP')
    


class HighJumpKick(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('highjumpkick'))
    def SideEffect(self,src,target):
        Console.msg(src.GetName()+'受到副作用')
        target_damage = self.ApplyTarget(src,target,None)
        ApplyDamage(src,target_damage//8)


class Glare(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('glare'),ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,1,StatusCondEnum.PARALYSIS,is_print=True)


class DreamEater(AbsorbSkill):
    def __init__(self):
        AbsorbSkill.__init__(self,SkillChart.GetSkillSeries('dreameater'))
    def PreApply(self,src,target,weather):
        self.pp=self.pp-1
        if target.status_cond.Get() == StatusCondEnum.SLEEP:
            return True
        else:
            Console.msg('似乎没有什么效果')
            return False
        


class PoisonGas(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('poisongas'),ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,1,StatusCondEnum.POISON,is_print=True)


class Barrage(MultiHitSkill):
    def __init__(self):
        MultiHitSkill.__init__(self,SkillChart.GetSkillSeries('Barrage'))


class LeechLife(AbsorbSkill):
    def __init__(self):
        AbsorbSkill.__init__(self,SkillChart.GetSkillSeries('leechlife'))


class LovelyKiss(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('lovelykiss'),ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,1,StatusCondEnum.SLEEP,is_print=True)


class SkyAttack(StockpileSkill,EasyCriticalHitSkill):
    def __init__(self):
        StockpileSkill.__init__(self,SkillChart.GetSkillSeries('skyattack'),discription='被强烈的光芒包围着')


#TODO :deprecated
# class Transform(SkillBase):
#     def __init__(self):
#         SkillBase.__init__(self,SkillChart.GetSkillSeries('transform'))


class Bubble(TargetBuffDown):
    def __init__(self):
        TargetBuffDown.__init__(self,SkillChart.GetSkillSeries('bubble'),StageEnum.SPEED,1,0.1,ObjOfAction.TAR+ObjOfAction.TAR_ABL)


class DizzyPunch(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('dizzypunch'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseSpecialCond(target,0.2,SpecialCondEnum.CONFUSION)
    


class Spore(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('spore'),ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        self.CauseStatusCond(target,1,StatusCondEnum.SLEEP,is_print=True)


class Flash(TargetBuffDown):
    def __init__(self):
        TargetBuffDown.__init__(self,SkillChart.GetSkillSeries('flash'),StageEnum.HIT,1)


class Psywave(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('psywave'))
    def ApplyTarget(self,src,target,weather):
        return int(src.level*np.random.randint(5,15)/10)


class Splash(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('splash'))
    def ApplyTarget(self,src,target,weather):
        return 0


class AcidArmor(SrcBuffUp):
    def __init__(self):
        SrcBuffUp.__init__(self,SkillChart.GetSkillSeries('acidarmor'),StageEnum.DEFENSE,2)




class Crabhammer(EasyCriticalHitSkill):
    def __init__(self):
        EasyCriticalHitSkill.__init__(self,SkillChart.GetSkillSeries('crabhammer'))


class Explosion(SelfLossSkill):
    def __init__(self):
        SelfLossSkill.__init__(self,SkillChart.GetSkillSeries('explosion'),1)


class FurySwipes(MultiHitSkill):
    def __init__(self):
        MultiHitSkill.__init__(self,SkillChart.GetSkillSeries('furyswipes'))


class Bonemerang(MultiHitSkill):
    def __init__(self):
        MultiHitSkill.__init__(self,SkillChart.GetSkillSeries('bonemerang'),2)

class Rest(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('rest'),ObjOfAction.SRC_ABL)
    def PreApply(self,src,target,weather):
        if src.status_cond.Get()==StatusCondEnum.SLEEP or src.hp==src.HP():
            Console.msg('似乎没有什么效果')
            return False
        else:
            self.pp=self.pp-1
            return True
    def ApplySrcAblity(self,src):
        Console.msg(src.GetName()+'回复了'+RecoverAllHP(src)+'点HP')
        if RecoverStatusCond(src):
            Console.msg(src.GetName()+'解除了所有异常状态')
        self.CauseStatusCond(src,1,StatusCondEnum.SLEEP,2)


class RockSlide(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('rockslide'))


class HyperFang(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('hyperfang'))


class Sharpen(SrcBuffUp):
    def __init__(self):
        SrcBuffUp.__init__(self,SkillChart.GetSkillSeries('sharpen'),SrcBuffUp)


class Conversion(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('conversion'),ObjOfAction.SRC_ABL)
    def ApplySrcAblity(self,src):
        if len(src.GetSkills())!=0:
            src.type=src.GetSkills()[0].GetType()
            Console.msg(src.GetName()+'战斗中属性变成了'+TypeEnum.ToChinese(src.type))

class TriAttack(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('triattack'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target,weather):
        value=np.random.randint(0,3)
        if value==0:
            self.CauseStatusCond(target,0.2,StatusCondEnum.BURN)
        elif value==1:
            self.CauseStatusCond(target,0.2,StatusCondEnum.FREEZE)
        elif value==2:
            self.CauseStatusCond(target,0.2,StatusCondEnum.PARALYSIS)


class SuperFang(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('superfang'))
    def ApplyTarget(self,src,target,weather):
        return int(target.hp/2)


class Slash(EasyCriticalHitSkill):
    def __init__(self):
        EasyCriticalHitSkill.__init__(self,SkillChart.GetSkillSeries('slash'))

#deprecated
# class Substitute(SkillBase):
#     def __init__(self):
#         SkillBase.__init__(self,SkillChart.GetSkillSeries('substitute'))


class Struggle(SelfLossSkill):
    def __init__(self):
        SelfLossSkill.__init__(self,SkillChart.GetSkillSeries('struggle'),1/4)

class SelfHarm(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('SelfHarm'),ObjOfAction.SRC)
    def ApplySrc(self,src,target_damage):
        return self.DamageCal(src,src,None)


