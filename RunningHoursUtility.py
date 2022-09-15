from UtilityFunction import UtilityFunction


class RunningHoursUtility(UtilityFunction):
    def GetUtility(self, hours):
        return hours * 3

    def GetPerformanceType(self):
        return "hoursSpentRunning"
