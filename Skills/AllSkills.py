from SkillBase import *

class Pound(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Pound'))

class KarateChop(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('KarateChop'))
    

class DoubleSlap(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('DoubleSlap'))
    def ApplyTarget(self,src,target,weather):
        damage=0
        hit_chance = np.random.rand()
        round_num=2
        if 1/6>hit_chance and hit_chance>=0:
            round_num=5
        elif 2/6>hit_chance and hit_chance>=1/6:
            round_num=4
        elif 4/6>hit_chance and hit_chance>=2/6:
            round_num=3
        elif 6/6>hit_chance and hit_chance>=4/6:
            round_num=2
        for i in range(round_num):
            print('击中'+str(i+1)+'次')
            damage = damage + self.DamageCal(src,target,weather)
            rest()
        return damage

class CometPunch(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('CometPunch'))
    def ApplyTarget(self,src,target,weather):
        damage=0
        hit_chance = np.random.rand()
        round_num=2
        if 1/6>hit_chance and hit_chance>=0:
            round_num=5
        elif 2/6>hit_chance and hit_chance>=1/6:
            round_num=4
        elif 4/6>hit_chance and hit_chance>=2/6:
            round_num=3
        elif 6/6>hit_chance and hit_chance>=4/6:
            round_num=2
        for i in range(round_num):
            print('击中'+str(i+1)+'次')
            damage = damage + self.DamageCal(src,target,weather)
            rest()
        return damage

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


class Guillotine(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Guillotine'))
    def ApplyTarget(self,src,target,weather):
        damage=target.hp
        return damage
    def _IsHit(self,src,target):
        if src.level<target.level:
            return False
        else:
            return np.random.rand()<(30+src.level-target.level)/100

class RazorWind(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('RazorWind'))

    def SetDefault(self):
        self.is_ready=False

    def PreApply(self,src,target,weather):
        if self.is_ready==False:
            print(src.GetName()+'蓄力中...')
            self.is_ready=True
            return False
        self.pp=self.pp-1
        return True

    def PostApply(self,src,target,weather):
        if self.is_ready==True:
            self.is_ready=False
        


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

class Fly(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Fly'))
        self.is_ready=False
    def PreApply(self,src,target,weather):
        if self.is_ready==False:
            print(src.GetName()+'飞上了高空...')
            self.is_ready=True
            src.position=PositionEnum.SKY
            return False
        self.pp=self.pp-1
        return True

    def PostApply(self,src,target,weather):
        if self.is_ready==True:
            self.is_ready=False
            src.position=PositionEnum.PLAYGROUND


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


class DoubleKick(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('doublekick'))
    def ApplyTarget(self,src,target,weather):
        damage=0
        for i in range(2):
            print('击中'+str(i+1)+'次')
            damage = damage + self.DamageCal(src,target,weather)
            rest()
        return damage


class MegaKick(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('megakick'))


class JumpKick(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('jumpkick'))
    def SideEffect(self,src):
        target_damage = self.ApplyTarget(src,target,weather)
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


class FuryAttack(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('furyattack'))
    def ApplyTarget(self,src,target,weather):
        damage=0
        hit_chance = np.random.rand()
        round_num=2
        if 1/6>hit_chance and hit_chance>=0:
            round_num=5
        elif 2/6>hit_chance and hit_chance>=1/6:
            round_num=4
        elif 4/6>hit_chance and hit_chance>=2/6:
            round_num=3
        elif 6/6>hit_chance and hit_chance>=4/6:
            round_num=2
        for i in range(round_num):
            print('击中'+str(i+1)+'次')
            damage = damage + self.DamageCal(src,target,weather)
            rest()
        return damage


class HornDrill(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('horndrill'))
    def ApplyTarget(self,src,target,weather):
        damage=target.hp
        return damage
    def _IsHit(self,src,target):
        if src.level<target.level:
            return False
        else:
            return np.random.rand()<(30+src.level-target.level)/100


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


class TakeDown(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('takedown'))


class Thrash(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Thrash'))


class DoubleEdge(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('doubleedge'))


class TailWhip(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('TailWhip'))


class PoisonSting(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('poisonsting'))


class Twineedle(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('twineedle'))


class PinMissile(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('pinmissile'))


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


class Submission(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('submission'))


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


class Absorb(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('absorb'))


class MegaDrain(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('megadrain'))


class LeechSeed(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('leechseed'))


class Growth(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('growth'))

class RazorLeaf(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('RazorLeaf'))


class SolarBeam(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('SolarBeam'))
    def SetDefault(self):
        self.is_ready=False

    def PreApply(self,src,target,weather):
        if self.is_ready==False:
            print(src.GetName()+'吸收了阳光...')
            self.is_ready=True
            return False
        self.pp=self.pp-1
        return True

    def PostApply(self,src,target,weather):
        if self.is_ready==True:
            self.is_ready=False

class PoisonPowder(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('PoisonPowder'))


class StunSpore(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('StunSpore'))


class SleepPowder(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('SleepPowder'))

    def ApplyTargetAblity(self,target):
        target.stat_condition=StatusCondition.SLEEP



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


class Fissure(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Fissure'))


class Dig(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('dig'))
        self.is_ready=False
    def PreApply(self,src,target,weather):
        if self.is_ready==False:
            print(src.GetName()+'潜入了地下...')
            self.is_ready=True
            src.position=PositionEnum.UNDERGROUND
            return False
        self.pp=self.pp-1
        return True

    def PostApply(self,src,target,weather):
        if self.is_ready==True:
            self.is_ready=False
            src.position=PositionEnum.PLAYGROUND


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


class SkullBash(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('skullbash'),ObjOfAction.TAR+ObjOfAction.SRC_ABL)
    def SetDefault(self):
        self.is_ready=False
    def PreApply(self,src,target,weather):
        if self.is_ready==False:
            
            print(src.GetName()+'缩起了脖子...')
            self.is_ready=True
            return False
        self.pp=self.pp-1
        return True

    def PostApply(self,src,target,weather):
        if self.is_ready==True:
            self.is_ready=False
    def ApplySrcAblity(self,src):
        print(src.stage.Up(StageEnum.DEFENSE,1))


class SpikeCannon(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('spikecannon'))


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


class Glare(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('glare'))


class DreamEater(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('dreameater'))


class PoisonGas(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('poisongas'))


class Barrage(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('Barrage'))


class LeechLife(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('leechlife'))


class LovelyKiss(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('lovelykiss'))


class SkyAttack(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('skyattack'))
    def SetDefault(self):
        self.is_ready=False

    def PreApply(self,src,target,weather):
        if self.is_ready==False:
            print(src.GetName()+'被强烈的光芒包围着...')
            self.is_ready=True
            return False
        self.pp=self.pp-1
        return True

    def PostApply(self,src,target,weather):
        if self.is_ready==True:
            self.is_ready=False

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
        SkillBase.__init__(self,SkillChart.GetSkillSeries('spore'))


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


class FurySwipes(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('furyswipes'))


class Bonemerang(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('bonemerang'))


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


class Struggle(SkillBase):
    def __init__(self):
        SkillBase.__init__(self,SkillChart.GetSkillSeries('struggle'))






