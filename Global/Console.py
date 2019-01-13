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

        def display_pm_list(tm):
            print(tm.player.GetName()+':',end=' ')
            for pm in tm.pm_list[::-1]:
                if pm.IsAlive():
                    print('○',end=' ')
                else:
                    print('●',end=' ')
            # print('')
        our_pm=self.our_tm.pm_list.Front()
        enemy_pm=self.enemy_tm.pm_list.Front()
        display_pm_list(self.enemy_tm)
        print('> '+enemy_pm.GetName()+"  L"+str(enemy_pm.level)+' 状态:'+str(enemy_pm.status_cond))
        display_hp(enemy_pm)
        print('')
        display_pm_list(self.our_tm)
        print('> '+our_pm.GetName()+"  L"+str(our_pm.level)+' 状态:'+str(our_pm.status_cond)+'    HP:{}/{}'.format(our_pm.hp,our_pm.HP()))
        display_hp(our_pm)
    @classmethod
    def refresh(cls,is_clean_total=False):
        if is_clean_total:
            time.sleep(0.5)
        Console.msg('',is_clean=True,sleep_time=0.03,is_clean_total=is_clean_total)
    
    @classmethod
    def msg(cls,msg='',is_clean=False,sleep_time=0.25,is_clean_total=False):
        def cls_and_display(instance):
            os.system('cls')

            if instance.our_tm!=None and instance.enemy_tm!=None:
                instance.display_pm()
        instance = cls.GetInstance()
        rest(sleep_time=sleep_time)
        if is_clean==True or len(instance.msg_list)>=10:
            cls_and_display(instance)
            
            if is_clean_total==True:
                instance.msg_list.clear()
            else:
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
        