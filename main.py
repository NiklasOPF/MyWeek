from InputFileReader import InputFileReader
from PerformanceRecord import PerformanceRecord
from PerformanceType import PerformanceType
from RunningHoursUtility import RunningHoursUtility
from WorkingHOursUtility import WorkingHoursUtility
from UtilityFucntions import UtilityFunctions

input_folder = "InputFiles"
input_filename = "Input.xlsx"



if __name__ == '__main__':


    # read data
    reader = InputFileReader()
    df = reader.ReadPerformanceTypes(input_folder + "/" + input_filename)
    a=1

    runningPerformanceType = PerformanceType("hoursSpentRunning", "sports")
    workingPerformanceType = PerformanceType("hoursSpentWorking", "career")
    performanceRecord1 = PerformanceRecord(time_range=7, performance_metric=2, performance_type=runningPerformanceType)
    performanceRecord2 = PerformanceRecord(time_range=7, performance_metric=2, performance_type=workingPerformanceType)

    runningUtilityFun = RunningHoursUtility(None)
    workingUtilityFun = WorkingHoursUtility(None)

    performanceRecords = {performanceRecord1, performanceRecord2}
    utilityFunctions = UtilityFunctions({runningUtilityFun, workingUtilityFun})

    # calculate score
    overall_score = 0
    for perfromanceRecord in performanceRecords:
        utility_function = utilityFunctions.GetUtilityFunction(perfromanceRecord.performance_type.name)
        new_score = utility_function.GetUtility(perfromanceRecord.GetPerformanceMetric())
        overall_score = overall_score + new_score

    print(overall_score)
    a=1

