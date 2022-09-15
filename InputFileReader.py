import pandas as pd

_configuration_sheet_name = 'Configuration' # used to identify the excel sheet of a configuration.
class InputFileReader:
    def __init__(self):
        self.a = 1
    def read_file(self, filename):
        # Use a breakpoint in the code line below to debug your script.
        df = pd.read_excel(filename)
        return df

    def ReadPerformanceTypes(self, filename):
        # Returns all performance types.
        # For now assumes that there is only one line of specification
        df = pd.read_excel(filename, sheet_name=_configuration_sheet_name, header=None)

        categories = df.iloc[0].dropna().drop_duplicates()


        a=1


        return df

