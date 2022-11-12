import pandas as pd


class Calculator:
    def CalculateOverallUtility(self, utilityFunctions, performanceRecords):
        overall_score = 0
        for perfromanceRecord in performanceRecords:
            utility_function = utilityFunctions.GetUtilityFunction(perfromanceRecord.performance_type)
            new_score = utility_function.GetUtility(perfromanceRecord.GetPerformanceMetric()) # TODO: Insert try-catch around this one
            overall_score = overall_score + new_score
        return overall_score


    def CalculateUtilityReport(self, utilityFunctions, performanceRecords, date):
        overall_score = 0
        df = pd.concat([pd.DataFrame(), pd.DataFrame([date], columns=['Date - Date'])], axis=1)
        df['Date - Date'] = pd.to_datetime(df['Date - Date'], format="%m/%d/%y")
        df = df.set_index('Date - Date')
        for perfromanceRecord in performanceRecords:
            performanceType = perfromanceRecord.GetPerformanceType()
            utility_function = utilityFunctions.GetUtilityFunction(performanceType)
            new_score = utility_function.GetUtility(perfromanceRecord.GetPerformanceMetric())
            overall_score = overall_score + new_score
            df[performanceType.GetCategory() + ' - ' + performanceType.GetName()] = [new_score]
        df['Total'] = [overall_score]
        return df