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
        y = x * a/(2b)      if x<2b
        y = a               if x>2b
"""

class LinearUtilityFunction(UtilityFunction):
    '''' THis constructor exrects list parameters '''

    def __init__(self, params, performanceType):
        self.a = params[0]
        self.b = params[1]
        self.performanceType = performanceType

    def GetUtility(self, hours):
        if hours < 0:
            return 0
        if hours < 2 * self.b:
            return hours * self.a / (2 * self.b)
        return self.a

    def GetUtilityFunctionType(self):
        return "Linear"

    def GetPerformanceType(self):
        return self.performanceType
