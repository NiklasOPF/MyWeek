from UtilityFunctions.UtilityFunction import UtilityFunction


class WorkingHoursUtility(UtilityFunction):
    def GetUtility(self, hours):
        return hours * 4

    def GetPerformanceType(self):
        return "hoursSpentWorking"