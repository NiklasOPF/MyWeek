class UtilityFunctions:

    def __init__(self, utilityFunctions):
        self.utilityFunctions = utilityFunctions

    def GetUtilityFunction(self, performanceType):
        fun = None
        for utilityFunction in self.utilityFunctions:
            if utilityFunction.GetPerformanceType().Equals(performanceType):
                fun = utilityFunction
        return fun