# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 00:23:23 2017

@author: narveer-rathore
"""

"""
    Parent Class for All Gates
"""
class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None
    
    def getLabel(self):
        return self.label
    
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


"""
    Class for Binary Gates
"""
class BinaryGate(LogicGate):
    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pinA = None
        self.pinB = None
        

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("No Empty Pins")

    def getPinA(self):
        if self.pinA == None:
            return int(input(" A input for gate " + self.getLabel() + " --> "))
        else:
            return self.pinA.getFrom().getOutput() 
        
    def getPinB(self):
        if self.pinB == None:
            return int(input(" B input for gate " + self.getLabel() + " --> "))
        else:
            return self.pinB.getFrom().getOutput() 


"""
    Class for Unary Gates
"""    
class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self, n)
        self.pin = None

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: No Empty Pin")
            
    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate " + self.getLabel() + " --> "))
        else:
            return self.pin.getFrom().getOutput()
        
        
""" 
    AND Gate
"""
class AndGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


""" 
    OR Gate
"""
class OrGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


""" 
    NOT Gate
"""
class NotGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPin()
        if a == 0:
            return 1
        else:
            return 0


"""
    Connector Class
"""
class Connector:
    def __init__(self, fgate, tgate):
        self.fromGate = fgate
        self.toGate = tgate
        
        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromGate

    def getTo(self):
        return self.toGate

""" 
    NAND Gate
"""
class NandGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 0
        else:
            return 1


""" 
    NOR Gate
"""
class NorGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 0
        else:
            return 1
    
    
g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1, g3)
c1 = Connector(g2, g3)
c1 = Connector(g3, g4)
# print(g4.getOutput())

nand = NandGate("n1")
#print(nand.getOutput())

nor = NorGate("n2")
#print(nor.getOutput())


# proving 
# NOT (( A and B) or (C and D)) = NOT( A and B ) and NOT (C and D)
abAnd = AndGate("AandB")
cdAnd = AndGate("CandD")
nor = NorGate("(AandB)nor(CandD)")
c1 = Connector(abAnd, nor)
c2 = Connector(cdAnd, nor)
print("LHS = ", nor.getOutput())

# RHS
abAnd2 = AndGate("AandB2")
cdAnd2 = AndGate("CandD2")
not1 = NotGate("AnotB")
not2 = NotGate("CnotD")
andAll = AndGate("andAll")

c1 = Connector(abAnd2, not1)
c2 = Connector(cdAnd2, not2)
c3 = Connector(not1, andAll)
v4 = Connector(not2, andAll)
print("RHS = ", andAll.getOutput())