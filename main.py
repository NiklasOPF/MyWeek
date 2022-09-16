from Calculator import Calculator
from InputFileReader import InputFileReader
from PerformanceRecord import PerformanceRecord
from PerformanceType import PerformanceType
from UtilityFunctions.UtilityFunction import LinearUtilityFunction, UtilityFunction
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
        performanceRecords.add(PerformanceRecord(7, colData.iloc[2], performanceType))

    # CREATE UTILITY FUNCTIONS
    utilityFunctionsSet = set()
    df2 = reader.ReadUtilityFunctions(input_folder + "/" + input_filename, date="Sunday, 18 September 2022")
    for (colName, colData) in df2.iteritems():
        array = colData.iloc[2].split(", ")
        name = array[0]
        params = [float(i) for i in array[1:]]

        performanceType = PerformanceType(colData[1], colData[0])
        match name:
            case "Linear":
                utilityFunctionsSet.add(LinearUtilityFunction(params, performanceType))
            case _:
                raise NotImplementedError("no utility function of the specified type")
    utilityFunctions = UtilityFunctions(utilityFunctionsSet)



    # calculate score
    calculator = Calculator()
    overall_score = calculator.CalculateUtility(utilityFunctions, performanceRecords)
    print(overall_score)

