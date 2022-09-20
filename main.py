from Calculator import Calculator
from IO import IO
from PerformanceRecord import PerformanceRecord
from PerformanceType import PerformanceType
from UtilityFunctions.UtilityFunction import LinearUtilityFunction, UtilityFunction, DoubleLinearUtilityFunction, \
    ScalingUtilityFunction
from UtilityFunctions.UtilityFucntions import *
import pandas as pd

input_folder = "InputFiles"
output_folder = "OutputFiles"
input_filename = "WeekTracker.xlsx" #"Input.xlsx"
output_filename = "WeekTracker.xlsx" #"Output.xlsx"
performance_date_string = "Sunday, 18 September 2022"
#performance_date_test = pd.to_datetime("2022-09-10")
configuration_date = "Sunday, 18 September 2022"

if __name__ == '__main__':
    # READ DATA
    io = IO()
    df = io.ReadPerformanceRecords(input_folder + "/" + input_filename, date=pd.to_datetime(performance_date_string))

    # CREATE PERFORMANCE RECORDS FORM DATAFRAME
    performanceRecords = set()
    performanceTypes = set()
    for (colName, colData) in df.iteritems():
        performanceType = PerformanceType(colName.split(" - ")[1], colName.split(" - ")[0]) #PerformanceType(colData[1], colData[0])
        performanceTypes.add(performanceType)
        performanceRecords.add(PerformanceRecord(7, colData[performance_date_string], performanceType))

    # CREATE UTILITY FUNCTIONS
    utilityFunctionsSet = set()
    df2 = io.ReadUtilityFunctions(input_folder + "/" + input_filename)#, date=configuration_date)
    for (colName, colData) in df2.iteritems():
        try:
            array = colData[performance_date_string].split(", ")
        except:
            pass
        params = [float(i) for i in array[1:]]
        names = colName.split(" - ")
        match array[0]:
            case "Linear":
                utilityFunctionsSet.add(LinearUtilityFunction(params, PerformanceType(names[1], names[0])))
            case "DoubleLinear":
                utilityFunctionsSet.add(DoubleLinearUtilityFunction(params, PerformanceType(names[1], names[0])))
            case "Scaling":
                utilityFunctionsSet.add(ScalingUtilityFunction(params, PerformanceType(names[1], names[0])))
            case _:
                raise NotImplementedError("no utility function of the specified type")
    utilityFunctions = UtilityFunctions(utilityFunctionsSet)

    # CALCULATE SCORES
    calculator = Calculator()
    overall_score = calculator.CalculateOverallUtility(utilityFunctions, performanceRecords)
    reportRecord = calculator.CalculateUtilityReport(utilityFunctions, performanceRecords, performance_date_string)

    # SCORES TO EXCEL
    io.SavePerformanceReport(reportRecord, input_folder + "/" + input_filename, output_folder + "/" + output_filename)
    print("The overall score for " + performance_date_string + " was: " + str(overall_score))

