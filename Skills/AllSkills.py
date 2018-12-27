# from Stat import *
from SkillBase import *
from SkillFamalies import *

class Pound(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Pound'))

class KarateChop(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('KarateChop'))
    

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
    def ApplyTargetAblity(self,target):
        self.CauseStatusCond(target,0.1,StatusCondEnum.BURN)

class IcePunch(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('IcePunch'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)

    def ApplyTargetAblity(self,target):
        self.CauseStatusCond(target,0.1,StatusCondEnum.FREEZE)

class ThunderPunch(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('ThunderPunch'),ObjOfAction.TAR+ObjOfAction.TAR_ABL)

    def ApplyTargetAblity(self,target):
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

class RazorWind(StockpileSkill):
    def __init__(self):
        StockpileSkill.__init__(self,SkillChart.GetSkillSeries('RazorWind'),discription='蓄力中')

class SwordsDance(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('SwordsDance'),ObjOfAction.SRC_ABL)
    
    def ApplySrcAblity(self,src):
        print(src.stage.Up(StageEnum.ATTACK,2))


class Cut(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Cut'))


class Gust(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Gust'))
    def ApplyTarget(self,src,target,weather):
        if target.position==PositionEnum.SKY:
            return self.DamageCal(src,target,weather)*2
        elif target.position==PositionEnum.UNDERGROUND:
            return 0
        else:
            return self.DamageCal(src,target,weather)


class WingAttack(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('WingAttack'))


class Whirlwind(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('WhirlWind'),ObjOfAction.TAR_ABL)
        self.priority=-6
    def ApplyTargetAblity(self,src,target,weather):
        target.is_playing=False

class Fly(StockpileSkill):
    def __init__(self):
        StockpileSkill.__init__(self,SkillChart.GetSkillSeries('Fly'),PositionEnum.SKY,'飞上了高空')


class Bind(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Bind'))


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
        print(src.GetName()+'受到副作用')
        target_damage = self.ApplyTarget(src,target,None)
        self.ApplyDamage(src,target_damage//8)


class RollingKick(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('rollingkick'))


class SandAttack(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('sandattack'),ObjOfAction.TAR_ABL)
    
    def ApplyTargetAblity(self,target):
        print(target.stage.Down(StageEnum.HIT,1))

class headbutt(SkillBase):
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
    def ApplyTargetAblity(self,target):
        self.CauseStatusCond(target,0.3,StatusCondEnum.PARALYSIS)


class Wrap(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('wrap'))


class TakeDown(ReboundSkill):
    def __init__(self):
        ReboundSkill.__init__(self,SkillChart.GetSkillSeries('takedown'),1/4)


class Thrash(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Thrash'))


class DoubleEdge(ReboundSkill):
    def __init__(self):
        ReboundSkill.__init__(self,SkillChart.GetSkillSeries('doubleedge'),1/3)


class TailWhip(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('TailWhip'))


class PoisonSting(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('poisonsting'))


class Twineedle(MultiHitSkill):
    def __init__(self):
        MultiHitSkill.__init__(self,SkillChart.GetSkillSeries('twineedle'),2)


class PinMissile(MultiHitSkill):
    def __init__(self):
        MultiHitSkill.__init__(self,SkillChart.GetSkillSeries('pinmissile'))


class Leer(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('leer'))


class Bite(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('bite'))


class Growl(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('growl'))


class Roar(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('roar'))


class Sing(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Sing'))


class Supersonic(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('supersonic'))


class SonicBoom(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('SonicBoom'))


class Disable(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Disable'))


class Acid(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('acid'))


class Ember(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('ember'))


class Flamethrower(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('flamethrower'))


class Mist(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('mist'))


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
        SkillBase.__init__(self,SkillChart.GetSkillSeries('icebeam'))


class Blizzard(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('blizzard'))


class Psybeam(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('psybeam'))


class BubbleBeam(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('bubblebeam'))


class AuroraBeam(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('aurorabeam'))


class HyperBeam(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('hyperbeam'))


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


class Counter(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('counter'))


class SeismicToss(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('seismictoss'))


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
    def ApplyTargetAblity(self,target):
        target.special_cond.Set(SpecialCondEnum.PARASITIC,np.random.randint(3,9))


class Growth(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('growth'))

class RazorLeaf(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('RazorLeaf'))


class SolarBeam(StockpileSkill):
    def __init__(self):
        StockpileSkill.__init__(self,SkillChart.GetSkillSeries('SolarBeam'),discription='吸收了阳光...')
    

class PoisonPowder(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('PoisonPowder'),ObjOfAction.TAR_ABL)

    def ApplyTargetAblity(self,target):
        target.status_cond=StatusCondEnum.POISON
        print(target.GetName()+'中毒了...')


class StunSpore(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('StunSpore'),ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target):
        target.status_cond=StatusCondEnum.PARALYSIS
        print(target.GetName()+'麻痹了...')

class SleepPowder(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('SleepPowder'),ObjOfAction.TAR_ABL)

    def ApplyTargetAblity(self,target):
        target.status_cond=StatusCondEnum.SLEEP
        print(target.GetName()+'陷入了睡眠...')



class PetalDance(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('PetalDance'))


class StringShot(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('stringshot'))


class DragonRage(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('DragonRage'))


class FireSpin(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('firespin'))


class ThunderShock(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('thundershock'))


class Thunderbolt(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('thunderbolt'))


class ThunderWave(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('thunderwave'))


class Thunder(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('thunder'))


class RockThrow(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('rockthrow'))


class Earthquake(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('earthquake'))
    def ApplyTarget(self,src,target,weather):
        if target.position==PositionEnum.UNDERGROUND:
            return self.DamageCal(src,target,weather)*2
        elif target.position==PositionEnum.SKY:
            return 0
        else:
            return self.DamageCal(src,target,weather)


class Fissure(MustKillSkill):
    def __init__(self):
        MustKillSkill.__init__(self,SkillChart.GetSkillSeries('Fissure'))


class Dig(StockpileSkill):
    def __init__(self):
        StockpileSkill.__init__(self,SkillChart.GetSkillSeries('dig'),PositionEnum.UNDERGROUND,'潜入了地下...')

class Toxic(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('toxic'))


class Confusion(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('confusion'))


class Psychic(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('psychic'))


class Hypnosis(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('hypnosis'))


class Meditate(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('meditate'))


class Agility(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('agility'))


class QuickAttack(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('quickattack'))


class Rage(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('rage'))


class Teleport(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('teleport'))


class NightShade(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('nightshade'))


class Mimic(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('mimic'))


class Screech(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Screech'))


class DoubleTeam(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('doubleteam'))


class Recover(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('recover'))


class Harden(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('harden'))


class Minimize(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('minimize'))


class Smokescreen(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('smokescreen'))


class ConfuseRay(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('confuseray'))


class Withdraw(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('withdraw'))


class DefenseCurl(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('defensecurl'))


class Barrier(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('barrier'))


class LightScreen(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('lightscreen'))


class Haze(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('haze'))


class Reflect(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('reflect'))


class FocusEnergy(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('focusenergy'))


class Bide(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('bide'))


class Metronome(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('metronome'))


class MirrorMove(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('MirrorMove'))


class SelfDestruct(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('selfdestruct'))


class EggBomb(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('eggbomb'))


class Lick(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('lick'))


class Smog(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('smog'))


class Sludge(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('sludge'))


class BoneClub(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('boneclub'))


class FireBlast(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('fireblast'))


class Waterfall(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('waterfall'))


class Clamp(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('clamp'))


class Swift(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('swift'))


class SkullBash(StockpileSkill):
    def __init__(self):
        StockpileSkill.__init__(self,SkillChart.GetSkillSeries('skullbash'),discription='缩起了脖子',obj_of_action=ObjOfAction.TAR+ObjOfAction.SRC_ABL)
    def ApplySrcAblity(self,src):
        print(src.stage.Up(StageEnum.DEFENSE,1))


class SpikeCannon(MultiHitSkill):
    def __init__(self):
        MultiHitSkill.__init__(self,SkillChart.GetSkillSeries('spikecannon'))


class Constrict(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('constrict'))


class Amnesia(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Amnesia'))


class Kinesis(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('kinesis'))



class SoftBoiled(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('softboiled'))



class HighJumpKick(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('highjumpkick'))
    def SideEffect(self,src,target):
        print(src.GetName()+'受到副作用')
        target_damage = self.ApplyTarget(src,target,None)
        self.ApplyDamage(src,target_damage//8)


class Glare(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('glare'))


class DreamEater(AbsorbSkill):
    def __init__(self):
        AbsorbSkill.__init__(self,SkillChart.GetSkillSeries('dreameater'))
    def PreApply(self,src,target,weather):
        self.pp=self.pp-1
        if target.status_cond == StatusCondEnum.SLEEP:
            return True
        else:
            print('似乎没有什么效果')
            return False
        


class PoisonGas(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('poisongas'))


class Barrage(MultiHitSkill):
    def __init__(self):
        MultiHitSkill.__init__(self,SkillChart.GetSkillSeries('Barrage'))


class LeechLife(AbsorbSkill):
    def __init__(self):
        AbsorbSkill.__init__(self,SkillChart.GetSkillSeries('leechlife'))


class LovelyKiss(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('lovelykiss'))


class SkyAttack(StockpileSkill):
    def __init__(self):
        StockpileSkill.__init__(self,SkillChart.GetSkillSeries('skyattack'),discription='被强烈的光芒包围着')

class Transform(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('transform'))


class Bubble(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('bubble'))


class DizzyPunch(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('dizzypunch'))


class Spore(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('spore'),ObjOfAction.TAR_ABL)
    def ApplyTargetAblity(self,target):
        target.status_cond=StatusCondEnum.SLEEP
        print(target.GetName()+'陷入了睡眠...')


class Flash(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('flash'))


class Psywave(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('psywave'))


class Splash(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('splash'))


class AcidArmor(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('acidarmor'))


class Crabhammer(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('crabhammer'))


class Explosion(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('explosion'))


class FurySwipes(MultiHitSkill):
    def __init__(self):
        MultiHitSkill.__init__(self,SkillChart.GetSkillSeries('furyswipes'))


class Bonemerang(MultiHitSkill):
    def __init__(self):
        MultiHitSkill.__init__(self,SkillChart.GetSkillSeries('bonemerang'),2)


class Rest(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('rest'))


class RockSlide(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('rockslide'))


class HyperFang(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('hyperfang'))


class Sharpen(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('sharpen'))


class Conversion(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('conversion'))


class TriAttack(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('triattack'))


class SuperFang(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('superfang'))


class Slash(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('slash'))


class Substitute(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('substitute'))


class Struggle(SelfLossSkill):
    def __init__(self):
        SelfLossSkill.__init__(self,SkillChart.GetSkillSeries('struggle'),1/4)






