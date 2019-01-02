
import pandas as pd
import numpy as np
import threading
import time
import os
import sys


from  pk_enums  import *


from PokemonPK import pk_path

#从str到+1 int的字典switch
g_d4i = {'1':0,'2':1,'3':2,'4':3}
g_d5i = {'1':0,'2':1,'3':2,'4':3,'5':4}
g_d2i = {'1':0,'2':1}
g_d2b = {'1':True,'2':False}
g_c2e = {}
g_globals={}

#通用的Bool条件判断
def ToBeSure(msg=''):
    print('Are you sure that you want to '+msg +' ?')
    print('1.yes')
    print('2.no')
    choose = input('your choice:')
    return g_d2b[choose]


#Singleton Base Class
class Singleton(object):
    _mutex=threading.Lock()
    def __init__(self):
        pass

    
    @classmethod
    def GetInstance(cls,*args,**kwargs):
        if not hasattr(cls,'_instance'):
            cls._mutex.acquire(1)  
            if not hasattr(cls,'_instance'):
                cls._instance = cls()
            cls._mutex.release()
        return cls._instance




class TypeChart(Singleton):
    _type_chart=None
    _type_num=0
    def __init__(self):
        self._type_chart = pd.read_csv(pk_path+"StoreFiles/TypeChart.csv")
        self._type_num = len(self._type_chart.columns)
        indexes=[1<<i for i in range(0,self._type_num)]
        self._type_chart = pd.DataFrame(self._type_chart.values,index=indexes,columns=indexes)
       


    @classmethod
    def TypeVSType(cls,attack_type,defense_type):
       instance = TypeChart.GetInstance()
       effect = 1
       for i in range(0,instance._type_num):
           attack_index=1<<i
           if not (attack_index & attack_type):
               continue
           for j in range(0,instance._type_num):
               defense_index=1<<j
               if not (defense_index & defense_type):
                   continue
               effect = effect * instance._type_chart[defense_index][attack_index]   
               # print(effect,attack_index,defense_index)    
       

       effect_str = ''
       if effect>1:
           effect_str = u'效果拔群'
       elif effect<1 and effect >0:
           effect_str = u'效果一般'
       elif effect==0:
           effect_str = u'似乎没有效果'

       return (effect,effect_str)

class PokemonPKError(Exception):
    pass
        
        
def GetObjByChineseName(chinese_name):
    return g_globals[g_c2e[chinese_name]]()
        
    
def rest():
    time.sleep(0.2) 




