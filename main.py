from Calculator import Calculator
from IO import IO
from PerformanceRecord import PerformanceRecord
from PerformanceType import PerformanceType
from UtilityFunctions.UtilityFunction import LinearUtilityFunction, UtilityFunction, DoubleLinearUtilityFunction, \
    ScalingUtilityFunction, NormalCDFUtilityFunction
from UtilityFunctions.UtilityFucntions import *
import pandas as pd

# DYNAMIC CONFIGURATION PARAMETERS
input_filename = "WeekTracker.xlsx" #"Input.xlsx"
output_filename = "WeekTracker.xlsx" #"Output.xlsx"
date_string = "Sunday, 18 September 2022"

# STATIC CONFIGURATION PARAMETERS
input_folder = "InputFiles"
output_folder = "OutputFiles"

if __name__ == '__main__':
    # READ DATA
    io = IO()
    df = io.ReadPerformanceRecords(input_folder + "/" + input_filename)

    # CREATE PERFORMANCE RECORDS FORM DATAFRAME
    performanceRecords = set()
    performanceTypes = set()
    for (colName, colData) in df.iteritems():
        performanceType = PerformanceType(colName.split(" - ")[1], colName.split(" - ")[0]) #PerformanceType(colData[1], colData[0])
        try:
            performanceMetric = colData[date_string]
            if performanceMetric != "-":
                performanceTypes.add(performanceType)
                performanceRecords.add(PerformanceRecord(7, performanceMetric, performanceType))
        except KeyError:
            print("The Records sheet does not have a record on the date: " + date_string)
            exit()

    # CREATE UTILITY FUNCTIONS
    utilityFunctionsSet = set()
    df2 = io.ReadUtilityFunctions(input_folder + "/" + input_filename)#, date=configuration_date)
    for (colName, colData) in df2.iteritems():
        try:
            array = colData[date_string].split(", ")
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
            case "-":
                pass
            case _:
                raise NotImplementedError("No utility function of the specified type: '" + array[0] +"'")
    utilityFunctions = UtilityFunctions(utilityFunctionsSet)

    # CALCULATE SCORES
    calculator = Calculator()
    overall_score = calculator.CalculateOverallUtility(utilityFunctions, performanceRecords)
    reportRecord = calculator.CalculateUtilityReport(utilityFunctions, performanceRecords, date_string)

    # SCORES TO EXCEL
    io.SavePerformanceReport(reportRecord, input_folder + "/" + input_filename, output_folder + "/" + output_filename)
    print("The overall score for " + date_string + " was: " + str(overall_score))