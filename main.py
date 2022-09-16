from Calculator import Calculator
from InputFileReader import InputFileReader
from PerformanceRecord import PerformanceRecord
from PerformanceType import PerformanceType
from UtilityFunctions.UtilityFunction import LinearUtilityFunction
from UtilityFunctions.UtilityFucntions import *

input_folder = "InputFiles"
input_filename = "Input.xlsx"


if __name__ == '__main__':
    # READ DATA
    reader = InputFileReader()
    df = reader.ReadPerformanceRecords(input_folder + "/" + input_filename, date="Sunday, 4 September 2022")

    # CREATE PERFORMANCE RECORDS FORM DATAFRAME
    performanceRecords = set()
    performanceTypes = set()
    for (colName, colData) in df.iteritems():
        performanceType = PerformanceType(colData[1], colData[0])
        performanceTypes.add(performanceType)
        performanceRecords.add(PerformanceRecord(7, colData[2], performanceType))

    # PARAMETER SETUP
    familyTalkUtilityFun = LinearUtilityFunction(params=[1, 2], performanceType=PerformanceType('HoursSpentTalkingToFamily', 'Relationships'))
    youtubeUploadUtilityFun = LinearUtilityFunction(params=[1, 2], performanceType=PerformanceType('MinutesOfUploadedContent', 'Youtube'))
    hoursTrainingUtilityFun = LinearUtilityFunction(params=[1, 2], performanceType=PerformanceType('HoursTraining', 'PhysicalActivities'))
    applicationSubmittedUtilityFun = LinearUtilityFunction(params=[1, 2], performanceType=PerformanceType('ApplicationsSubmitted', 'Work'))
    hoursReadingUtilityFun = LinearUtilityFunction(params=[1, 2], performanceType=PerformanceType('HoursSpentReading', 'Learning'))
    adHocUtilityFun = LinearUtilityFunction(params=[1, 2], performanceType=PerformanceType('ad-hoc', 'Relationships'))
    hoursSalsaUtilityFun = LinearUtilityFunction(params=[1, 2], performanceType=PerformanceType('HoursOfSalsa', 'PhysicalActivities'))
    hoursFightingUtilityFun = LinearUtilityFunction(params=[1, 2], performanceType=PerformanceType('HoursFighting', 'PhysicalActivities'))

    utilityFunctions = UtilityFunctions({ familyTalkUtilityFun, youtubeUploadUtilityFun, hoursTrainingUtilityFun, applicationSubmittedUtilityFun, hoursReadingUtilityFun, adHocUtilityFun, hoursSalsaUtilityFun, hoursFightingUtilityFun })

    # calculate score
    calculator = Calculator()
    overall_score = calculator.CalculateUtility(utilityFunctions, performanceRecords)
    print(overall_score)
    a=1

