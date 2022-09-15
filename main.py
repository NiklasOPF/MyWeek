from InputFileReader import InputFileReader

input_folder = "InputFiles"
input_filename = "Input.xlsx"

if __name__ == '__main__':
    reader = InputFileReader()
    df = reader.read_file(input_folder + "/" + input_filename)
    a=1
