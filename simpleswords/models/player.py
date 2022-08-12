import enum


class HDTypes(enum.Enum):
    D6="d6"
    D8="d8"
    D10="d10"
    D12="d12"

class PlayerStats(object):
    STR: int
    DEX: int
    CON: int
    INT: int
    WIS: int
    CHA: int

    TOU: int

    HDTYPE: HDTypes

    @property
    def STRMOD(self):
        return (self.STR-10)/2
    
    @property
    def DEXMOD(self):
        return (self.DEX-10)/2

    @property
    def CONMOD(self):
        return (self.CON-10)/2

    @property
    def INTMOD(self):
        return (self.INT-10)/2
    
    @property
    def WISMOD(self):
        return (self.WIS-10)/2

    @property
    def CHAMOD(self):
        return (self.CHA-10)/2

    @property
    def BRN(self):
        return self.STRMOD+4
    
    @property
    def AGI(self):
        return self.DEXMOD+4
    
    @property
    def END(self):
        return self.CONMOD+4
    
    @property
    def HLT(self):
        return self.CONMOD+4
    
    @property
    def WIL(self):
        return self.WISMOD+4

    @property
    def WIT(self):
        return self.CHAMOD+4
    
    @property
    def PER(self):
        return self.WISMOD+4

    @property
    def MA(self):
        return self.INTMOD+1
    
    @property
    def ADR(self):
        return int((self.AGI+self.WIT)/2)
    
    @property
    def MOB(self):
        return int((self.BRN+self.AGI+self.END)/2)
    
    @property
    def CAR(self):
        return self.BRN + self.AGI
    
    @property
    def SOC(self):
        return int((self.WIL+self.WIT+self.PER)/2)
    
    @property
    def SDB(self):
        return int(self.BRN/2)
    
    @property
    def GRIT(self):
        if self.HDTYPE == HDTypes.D6:
            return self.WIL/2
        elif self.HDTYPE == HDTypes.D8:
            return self.WIL/2+1
        elif self.HDTYPE == HDTypes.D10:
            return self.WIL/2+2
        elif self.HDTYPE == HDTypes.D12:
            return self.WIL/2+3

class PlayerModel(object):
    # base stats

    def __init__(self, base_stats: PlayerStats):
        self.BASE = base_stats
        self.hlt_lost = 0
        self.encumbrance = 0
        self.fatigue = 0
    
    @property
    def BRN(self):
        if self.HLT < 2:
            return int(self.BASE.BRN/2)
        else:
            return self.BASE.BRN

    @property
    def AGI(self):
        if self.HLT < 2:
            return int(self.BASE.AGI/2)
        else:
            return self.BASE.AGI

    @property
    def END(self):
        if self.HLT < 2:
            return int(self.BASE.END/2)
        else:
            return self.BASE.END

    @property
    def HLT(self):
        return self.BASE.HLT - self.hlt_lost

    @property
    def WIL(self):
        if self.HLT < 2:
            return int(self.BASE.WIL/2)
        else:
            return self.BASE.WIL

    @property
    def WIT(self):
        if self.HLT < 2:
            return int(self.BASE.WIT/2)
        else:
            return self.BASE.WIT

    @property
    def PER(self):
        if self.HLT < 2:
            return int(self.BASE.PER/2)
        else:
            return self.BASE.PER
    
    @property
    def MA(self):
        if self.HLT < 2:
            return int(self.BASE.MA/2)
        else:
            return self.BASE.MA

    @property
    def MOB(self):
        if self.encumbrance < self.BASE.CAR:
            return self.BASE.MOB-self.fatigue_cp_penalty
        elif self.encumbrance < 2*self.BASE.CAR:
            return self.BASE.MOB-2-self.fatigue_cp_penalty
        elif self.encumbrance < 3*self.BASE.CAR:
            return self.BASE.MOB-4-self.fatigue_cp_penalty
        elif self.encumbrance < 4*self.BASE.CAR:
            return self.BASE.MOB-6-self.fatigue_cp_penalty
        elif self.encumbrance < 5*self.BASE.CAR:
            return self.BASE.MOB - 8 - self.fatigue_cp_penalty
        else:
            return 0

    @property
    def fatigue_cp_penalty(self):
        if self.fatigue < self.HLT+6:
            return 0
        elif self.fatigue < self.HLT+11:
            return 1
        elif self.fatigue < self.HLT+16:
            return 2
        elif self.fatigue < self.HLT+21:
            return 4
        else:
            return 6

class PlayerInventory(object):

    def __init__(self):
        pass

