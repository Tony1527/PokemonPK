from __future__ import print_function
from pk_utility import *
import os
class Console(Singleton):
    def __init__(self):
        self.our_tm=None
        self.enenmy_tm=None
        self.msg_list=[]

    def display_pm(self):
        def display_hp(pm):
            if pm.HP()<20:
                unit=1
            else:
                unit=pm.HP()//20
            white_block=pm.hp//unit
            if white_block>20:
                white_block=20
            black_block=20-white_block
            for i in range(white_block):
                print('■■', end='')
            for i in range(black_block):
                print('□□', end='')
            print('')
        our_pm=self.our_tm.pm_list.Front()
        enemy_pm=self.enemy_tm.pm_list.Front()
        print('敌方宝可梦>'+enemy_pm.GetName()+"  level:"+str(enemy_pm.level))
        display_hp(enemy_pm)
        print('')
        print('我方宝可梦>'+our_pm.GetName()+"  level:"+str(our_pm.level)+'    HP:{}/{}'.format(our_pm.hp,our_pm.HP()))
        display_hp(our_pm)

    
    @classmethod
    def msg(cls,msg='',is_clean=False,sleep_time=0.15):
        def cls_and_display(instance):
            os.system('cls')

            if instance.our_tm!=None and instance.enemy_tm!=None:
                instance.display_pm()
        instance = cls.GetInstance()
        rest(sleep_time=sleep_time)
        if is_clean==True or len(instance.msg_list)>=10:
            cls_and_display(instance)
            if len(instance.msg_list)>=10:
                for i in range(5):
                    instance.msg_list.pop(0)
            for x in instance.msg_list:
                print(x)
            
        if msg!='':
            print(msg)
            instance.msg_list.append(msg)
        rest(sleep_time=sleep_time)

    @classmethod
    def start_game(cls,our_tm,enemy_tm):
        from Team import Team
        instance = cls.GetInstance()
        instance.our_tm=our_tm
        instance.enemy_tm=enemy_tm
        os.system('cls')
        instance.display_pm()
        