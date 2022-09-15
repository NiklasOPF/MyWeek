class UtilityFunctions:
    def __init__(self, utilityFunctions):
        self.utilityFunctions = utilityFunctions

    def GetUtilityFunction(self, name):
        fun = None
        for utilityFunction in self.utilityFunctions:
            if utilityFunction.GetPerformanceType() == name:
                fun = utilityFunction
        return fun