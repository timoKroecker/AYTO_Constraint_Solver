import openpyxl

from minizinc_interface import solve

WB_PATH = "excel/13-09-2024.xlsx"

RED = "FF0000"
GREEN = "00A933"
WHITE = "000000"

def load_worksheet(path, sheet_name):
    return openpyxl.load_workbook(path)[sheet_name]

def load_input_matrix(path):
    map_ = {
    RED: -1,
    GREEN: 1,
    WHITE: 0
    }
    sheet = load_worksheet(WB_PATH, "Input")
    input_matrix = []
    for i in range(11):
        row = []
        girl = str(i + 2)
        for j in range(10):
            boy = chr(j + 98)
            hex_color = sheet[boy + girl].fill.fgColor.index[2:]
            row.append(map_[hex_color])
        input_matrix.append(row)
    return input_matrix

if __name__ == "__main__":
    input_matrix = load_input_matrix(WB_PATH)
    solve(input_matrix)