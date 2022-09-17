from Calculator import Calculator
from InputFileReader import InputFileReader
from OutputFileWriter import OutputFileWriter
from PerformanceRecord import PerformanceRecord
from PerformanceType import PerformanceType
from UtilityFunctions.UtilityFunction import LinearUtilityFunction, UtilityFunction, DoubleLinearUtilityFunction, \
    ScalingUtilityFunction
from UtilityFunctions.UtilityFucntions import *

input_folder = "InputFiles"
output_folder = "OutputFiles"
input_filename = "Input.xlsx"
performance_date = "Sunday, 4 September 2022"
configuration_date = "Sunday, 18 September 2022"

if __name__ == '__main__':
    # READ DATA
    reader = InputFileReader()
    df = reader.ReadPerformanceRecords(input_folder + "/" + input_filename, date=performance_date)

    # CREATE PERFORMANCE RECORDS FORM DATAFRAME
    performanceRecords = set()
    performanceTypes = set()
    for (colName, colData) in df.iteritems():
        performanceType = PerformanceType(colData[1], colData[0])
        performanceTypes.add(performanceType)
        performanceRecords.add(PerformanceRecord(7, colData.iloc[2], performanceType))

    # CREATE UTILITY FUNCTIONS
    utilityFunctionsSet = set()
    df2 = reader.ReadUtilityFunctions(input_folder + "/" + input_filename, date=configuration_date)
    for (colName, colData) in df2.iteritems():
        try:
            array = colData.iloc[2].split(", ")
        except:
            pass
        params = [float(i) for i in array[1:]]
        match array[0]:
            case "Linear":
                utilityFunctionsSet.add(LinearUtilityFunction(params, PerformanceType(colData[1], colData[0])))
            case "DoubleLinear":
                utilityFunctionsSet.add(DoubleLinearUtilityFunction(params, PerformanceType(colData[1], colData[0])))
            case "Scaling":
                utilityFunctionsSet.add(ScalingUtilityFunction(params, PerformanceType(colData[1], colData[0])))
            case _:
                raise NotImplementedError("no utility function of the specified type")
    utilityFunctions = UtilityFunctions(utilityFunctionsSet)

    # CALCULATE SCORES
    calculator = Calculator()
    overall_score = calculator.CalculateOverallUtility(utilityFunctions, performanceRecords)
    report = calculator.CalculateUtilityReport(utilityFunctions, performanceRecords, performance_date)

    # SCORES TO EXCEL
    writer = OutputFileWriter()
    writer.write_file(report, output_folder + "/PerformanceReport.xlsx")


    print(overall_score)

