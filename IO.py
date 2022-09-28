import pandas as pd

_configuration_sheet_name = 'Configuration' # used to identify the excel sheet of a configuration.
_records_sheet_name = 'Records' # used to identify the excel sheet of a configuration.
perormance_report_sheet_name = 'PerformanceReport' # Used to summarize the

class IO:
    def __init__(self):
        self.a = 1

    ################################### READ FUNCTIONS ###################################

    def ReadSheetWithSingleHeader(self, fileName, sheetName):
        inputDF = pd.read_excel(fileName, sheet_name=sheetName)
        inputDF['Date'] = pd.to_datetime(inputDF['Date'])
        return inputDF.set_index('Date').dropna(how='all')

    def ReadUtilityFunctions(self, fileName):
        df = self.ReadSheetWithSingleHeader(fileName, sheetName=_configuration_sheet_name)
        if df.isnull().values.any():
            raise ValueError("Configuration tab of the input dataframe contains empty cells")
        return df

    def ReadPerformanceRecords(self, fileName, date):
        df = self.ReadSheetWithSingleHeader(fileName, sheetName=_records_sheet_name)
        if df.isnull().values.any():
            raise ValueError("Records tab of the input dataframe contains empty cells")
        return df

    ################################### WRITE FUNCTIONS ###################################

    def WriteDataFrameToExcel(self, df, fileName, sheetname):
        #TODO: first initiate a check if the file already exists. if not, then generate a new file
        with pd.ExcelWriter(fileName, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
            df.to_excel(writer, sheetname)

    def SavePerformanceReport(self, perfromanceReportRecord, inputFileName, outputFileName):
        # Read existing performance report
        performanceReport = self.ReadSheetWithSingleHeader(inputFileName, perormance_report_sheet_name)

        # Merge existing performance report with new record
        df = perfromanceReportRecord.combine_first(performanceReport).sort_index()
        df = df.reindex(sorted(df.columns), axis=1)
        column_to_move = df.pop("Total")
        df.insert(len(df.columns), "Total", column_to_move)
        df.index.name = 'Date'

        self.WriteDataFrameToExcel(df, outputFileName, perormance_report_sheet_name)

    ################################### OUTDATED METHODS ###################################

    def ReadSheetWithMultiHeader(self, fileName, sheetName):
        inputDF = pd.read_excel(fileName, sheet_name=sheetName, header=None)
        header = []
        for i in range(inputDF.shape[1]): # skip fist index since it's only the date
            if inputDF.iloc[0, i] == 'Total':
                header.append('Total')
            else:
                header.append(inputDF.iloc[0, i] + " - " + inputDF.iloc[1, i])
        body = inputDF.iloc[2:]
        body.iloc[:,0] = pd.to_datetime(body.iloc[:,0])
        df = pd.concat([pd.DataFrame(header).T.set_index(0), body.set_index(0).dropna(how='all')])
        df.columns = df.iloc[0]
        return df[1:]

