import pandas as pd

_output_sheet_name = 'PerformanceReport' # Used to summarize the

class OutputFileWriter:
    def __init__(self):
        self.a = 1
    def write_file(self, df, fileName):
        # Use a breakpoint in the code line below to debug your script.
        df.to_excel(fileName, sheet_name=_output_sheet_name)


    def WriteExcel(self, df, filename, sheetname):
        with pd.ExcelWriter(filename, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
            df.to_excel(writer, sheetname, index=False)


