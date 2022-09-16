from InputFileReader import InputFileReader
from PerformanceRecord import PerformanceRecord
from PerformanceType import PerformanceType
from UtilityFunctions.UtilityFunction import LinearUtilityFunction
from UtilityFunctions.UtilityFucntions import *

input_folder = "InputFiles"
input_filename = "Input.xlsx"



if __name__ == '__main__':
    # read data
    reader = InputFileReader()
    df = reader.ReadPerformanceTypes(input_folder + "/" + input_filename)

    # PARAMETER SETUP
    runningPerformanceType = PerformanceType("hoursSpentRunning", "sports")
    workingPerformanceType = PerformanceType("hoursSpentWorking", "career")
    performanceRecord1 = PerformanceRecord(time_range=7, performance_metric=2, performance_type=runningPerformanceType)
    performanceRecord2 = PerformanceRecord(time_range=7, performance_metric=2, performance_type=workingPerformanceType)

    runningUtilityFun = LinearUtilityFunction([1, 2], runningPerformanceType)
    workingUtilityFun = LinearUtilityFunction([8, 3], workingPerformanceType)

    performanceRecords = {performanceRecord1, performanceRecord2}
    utilityFunctions = UtilityFunctions({runningUtilityFun, workingUtilityFun})

    # STRATEGIC PARAMETERIZATION OF UTILITY FUNCTIONS
    #utilityFunctions = UtilityFunctions()

    # calculate score
    overall_score = 0
    for perfromanceRecord in performanceRecords:
        utility_function = utilityFunctions.GetUtilityFunction(perfromanceRecord.performance_type)
        new_score = utility_function.GetUtility(perfromanceRecord.GetPerformanceMetric())
        overall_score = overall_score + new_score

    print(overall_score)
    a=1

