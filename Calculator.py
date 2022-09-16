class Calculator:
    def CalculateUtility(self, utilityFunctions, performanceRecords):
        overall_score = 0
        for perfromanceRecord in performanceRecords:
            utility_function = utilityFunctions.GetUtilityFunction(perfromanceRecord.performance_type)
            new_score = utility_function.GetUtility(perfromanceRecord.GetPerformanceMetric())
            overall_score = overall_score + new_score
        return overall_score