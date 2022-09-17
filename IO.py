import pandas as pd

_configuration_sheet_name = 'Configuration' # used to identify the excel sheet of a configuration.
_records_sheet_name = 'Records' # used to identify the excel sheet of a configuration.
perormance_report_sheet_name = 'PerformanceReport' # Used to summarize the

class IO:
    def __init__(self):
        self.a = 1
    def read_file(self, filename):
        # Use a breakpoint in the code line below to debug your script.
        df = pd.read_excel(filename)
        return df

    def ReadUtilityFunctions(self, filename, date):
        df = pd.read_excel(filename, sheet_name=_configuration_sheet_name, header=None)
        headers = df.iloc[0:2, 1:]
        body = (df.iloc[2:]).set_index(0).dropna(how='all')
        entry = body.loc[date]
        return pd.concat([headers, pd.DataFrame(entry).T], axis=0)

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

    def ReadSheetWithSingleHeader(self, fileName, sheetName):
        inputDF = pd.read_excel(fileName, sheet_name=sheetName)
        inputDF['Date'] = pd.to_datetime(inputDF['Date'])
        return inputDF.set_index('Date').dropna(how='all')

    def ReadPerformanceRecords(self, filename, date):
        #TODO: leverage ReadSheetWithHeader() function
                # Returns all performance types.
        # For now assumes that there is only one line of specification
        df = pd.read_excel(filename, sheet_name=_records_sheet_name, header=None)
        df = (df.loc[:, (df.iloc[2] != 'Comment')]).drop(2)
        headers = df.iloc[0:2, 1:]
        body = df.iloc[2:]
        body.iloc[:,0] = pd.to_datetime(body.iloc[:,0])
        body = body.set_index(0).dropna(how='all')
        entry = body.loc[date]
        return pd.concat([headers, pd.DataFrame(entry).T], axis=0)

    def WriteExcel(self, df, fileName, sheetname):
        with pd.ExcelWriter(fileName, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
            df.to_excel(writer, sheetname)

    def SavePerformanceReport(self, perfromanceReportRecord, fileName):
        # Read existing performance report
        performanceReport = self.ReadSheetWithSingleHeader(fileName, perormance_report_sheet_name)

        # Merge existing performance report with new record
        df = perfromanceReportRecord.combine_first(performanceReport).sort_index()
        df = df.reindex(sorted(df.columns), axis=1)
        column_to_move = df.pop("Total")
        df.insert(len(df.columns), "Total", column_to_move)
        df.index.name = 'Date'

        self.WriteExcel(df, fileName, perormance_report_sheet_name)



