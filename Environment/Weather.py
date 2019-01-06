from pk_enums import *

class Weather(object):
    def __init__(self):
        self.Clear()
    def __eq__(self,other):
        if isinstance(other,WeatherEnum):
            return self._weather==other
        else:
            return self._weather==other._weather
    
    def Reduce(self):
        if self._round>0:
            self._round=self._round-1
        if self._round==0:
            self._weather=WeatherEnum.NORMAL
    def Set(self,weather_enum,round):
        self._weather=weather_enum
        self._round=round

    def Get(self):
        return self._weather

    def Clear(self):
        self._weather=WeatherEnum.NORMAL
        self._round=0

    def IsNormal(self):
        return WeatherEnum.IsNormal(self._weather)
