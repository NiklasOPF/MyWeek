import sys
from Calculator import Calculator
from IO_writer import IO
from PerformanceRecord import PerformanceRecord
from PerformanceType import PerformanceType
from UtilityFunctions.UtilityFunction import LinearUtilityFunction, UtilityFunction, DoubleLinearUtilityFunction, \
    ScalingUtilityFunction, NormalCDFUtilityFunction, GenericLinearUtilityFunction, Points, OrderedPoints, \
    ListToOrderedPoints
from UtilityFunctions.UtilityFucntions import *
import pandas as pd




def InitiateCalculation(input_folder, input_filename, output_folder, output_filename, dateString):


    date = pd.to_datetime(dateString, format="%m/%d/%Y")
    # CONFIGURATION PARAMETER QUALITY CHECK
    try:
        date = pd.to_datetime(dateString, format="%m/%d/%Y")
    except ValueError:
        return "The string is not a date: " + dateString

    try:
        # READ DATA
        io = IO()
        recordDF = io.ReadPerformanceRecords(input_folder + "/" + input_filename)
        configurationDF = io.ReadUtilityFunctions(input_folder + "/" + input_filename)
        io.CheckCompatibilityBetweenReadDFs(recordDF, configurationDF)

        # CREATE PERFORMANCE RECORDS FORM DATAFRAME
        performanceRecords = set()
        performanceTypes = set()
        for (colName, colData) in recordDF.iteritems():
            performanceType = PerformanceType(colName.split(" - ")[1], colName.split(" - ")[0]) #PerformanceType(colData[1], colData[0])
            try:
                performanceMetric = colData[date]
                if performanceMetric != "-":
                    performanceTypes.add(performanceType)
                    performanceRecords.add(PerformanceRecord(7, performanceMetric, performanceType))
            except KeyError:
                return("The Records sheet does not have a record on the date: " + dateString)

        # CREATE UTILITY FUNCTIONS
        utilityFunctionsSet = set()
        for (colName, colData) in configurationDF.iteritems():
            try:
                array = colData[date].split(", ")
                params = [float(i) for i in array[1:]]
                names = colName.split(" - ")
                match array[0]:
                    case "Linear":
                        utilityFunctionsSet.add(LinearUtilityFunction(params, PerformanceType(names[1], names[0])))
                    case "DoubleLinear":
                        utilityFunctionsSet.add(
                            DoubleLinearUtilityFunction(params, PerformanceType(names[1], names[0])))
                    case "Scaling":
                        utilityFunctionsSet.add(ScalingUtilityFunction(params, PerformanceType(names[1], names[0])))
                    case "NormalCDF":
                        utilityFunctionsSet.add(NormalCDFUtilityFunction(params, PerformanceType(names[1], names[0])))
                    case "GenericLinear":
                        utilityFunctionsSet.add(GenericLinearUtilityFunction(ListToOrderedPoints(params), PerformanceType(names[1], names[0])))
                    case "-":
                        pass
                    case _:
                        raise NotImplementedError("No utility function of the specified type: '" + array[0] + "'")
            except:
                pass

        utilityFunctions = UtilityFunctions(utilityFunctionsSet)

        # CALCULATE SCORES
        calculator = Calculator()
        overall_score = calculator.CalculateOverallUtility(utilityFunctions, performanceRecords)
        reportRecord = calculator.CalculateUtilityReport(utilityFunctions, performanceRecords, date)

        # SCORES TO EXCEL
        io.SavePerformanceReport(reportRecord, input_folder + "/" + input_filename, output_folder + "/" + output_filename)
        return ("The overall score for " + dateString + " was: " + str(overall_score))
    except Exception as e:
        return e.args[0]
        #raise e