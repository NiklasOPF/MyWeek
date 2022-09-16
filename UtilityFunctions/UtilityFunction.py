from abc import ABC, abstractmethod

class UtilityFunction(ABC):
    @abstractmethod
    def GetUtility(self, performance_metric):
        pass
    @abstractmethod
    def GetUtilityFunctionType(self):
        pass

    @abstractmethod
    def GetPerformanceType(self):
        pass


""""
Deifines a linear utility function of the form:
        y = x * a/ b      if x<b
        y = a               if x>b
"""

class ScalingUtilityFunction(UtilityFunction):
    '''' THis constructor exrects list parameters '''

    def __init__(self, param, performanceType):
        self.a = param[0]
        self.performanceType = performanceType

    def GetUtility(self, x):
        if x < 0:
            return 0
        return self.a * x

    def GetUtilityFunctionType(self):
        return "Scaling"

    def GetPerformanceType(self):
        return self.performanceType

class LinearUtilityFunction(UtilityFunction):
    '''' THis constructor exrects list parameters '''

    def __init__(self, params, performanceType):
        self.a = params[0]
        self.b = params[1]
        self.performanceType = performanceType

    def GetUtility(self, hours):
        if hours < 0:
            return 0
        if hours < self.b:
            return hours * self.a / self.b
        return self.a

    def GetUtilityFunctionType(self):
        return "Linear"

    def GetPerformanceType(self):
        return self.performanceType

class DoubleLinearUtilityFunction(UtilityFunction):
    def __init__(self, params, performanceType):
        self.a1 = params[0]
        self.b1 = params[1]
        self.a2 = params[2]
        self.b2 = params[3]
        self.performanceType = performanceType

    def GetUtility(self, x):
        if x < 0:
            return 0
        if x < self.b1:
            return x * self.a1 / self.b1
        if x < self.b2:
            self.a1 + (self.a2 - self.a1) / (self.b2 - self.b1) * (x - self.b1)
        return self.a2

    def GetUtilityFunctionType(self):
        return "DoubleLinear"

    def GetPerformanceType(self):
        return self.performanceType
