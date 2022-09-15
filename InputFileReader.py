import pandas as pd
class InputFileReader:
    def __init__(self):
        self.a = 1
    def read_file(self, filename):
        # Use a breakpoint in the code line below to debug your script.
        df = pd.read_excel(filename)
        return df