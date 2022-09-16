import pandas as pd

_configuration_sheet_name = 'Configuration' # used to identify the excel sheet of a configuration.
_records_sheet_name = 'Records' # used to identify the excel sheet of a configuration.

class InputFileReader:
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

        df2 = headers.append(entry, ignore_index = True)



        return df2
    def ReadPerformanceRecords(self, filename, date):
                # Returns all performance types.
        # For now assumes that there is only one line of specification
        df = pd.read_excel(filename, sheet_name=_records_sheet_name, header=None)
        df = (df.loc[:, (df.iloc[2] != 'Comment')]).drop(2)

        headers = df.iloc[0:2, 1:]
        body = (df.iloc[2:]).set_index(0).dropna(how='all')
        entry = body.loc[date]

        df2 = headers.append(entry, ignore_index = True)


        return df2


