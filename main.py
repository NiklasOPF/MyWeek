from Calculator import Calculator
from InputFileReader import InputFileReader
from PerformanceRecord import PerformanceRecord
from PerformanceType import PerformanceType
from UtilityFunctions.UtilityFunction import LinearUtilityFunction
from UtilityFunctions.UtilityFucntions import *

input_folder = "InputFiles"
input_filename = "Input.xlsx"


if __name__ == '__main__':
    # read data
    # reader = InputFileReader()
    # df = reader.ReadPerformanceTypes(input_folder + "/" + input_filename)

    # PARAMETER SETUP
    runningPerformanceType = PerformanceType("hoursSpentRunning", "sports")
    workingPerformanceType = PerformanceType("hoursSpentWorking", "career")

    runningUtilityFun = LinearUtilityFunction(params=[1, 2], performanceType=runningPerformanceType)
    workingUtilityFun = LinearUtilityFunction(params=[8, 3], performanceType=workingPerformanceType)

    performanceRecord1 = PerformanceRecord(time_range=7, performance_metric=2, performance_type=runningPerformanceType)
    performanceRecord2 = PerformanceRecord(time_range=7, performance_metric=2, performance_type=workingPerformanceType)

    # STRATEGIC PARAMETERIZATION OF UTILITY FUNCTIONS
    performanceRecords = {performanceRecord1, performanceRecord2}
    utilityFunctions = UtilityFunctions({runningUtilityFun, workingUtilityFun})

    # calculate score
    calculator = Calculator()
    overall_score = calculator.CalculateUtility(utilityFunctions, performanceRecords)
    print(overall_score)
    a=1

