import pandas as pd

_configuration_sheet_name = 'Configuration' # used to identify the excel sheet of a configuration.
_records_sheet_name = 'Records' # used to identify the excel sheet of a configuration.

class OutputFileWriter:
    def __init__(self):
        self.a = 1
    def write_file(self, df, fileName):
        # Use a breakpoint in the code line below to debug your script.
        df.to_excel(fileName)


