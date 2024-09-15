import numpy as np

import workbook_interface as workbook
import printer
from minizinc_interface import solve

EXCEL_DIR = "excel/"

def get_wb_path(season, night):
    return EXCEL_DIR + "season " + str(season) + "/" + str(night) + "_nights.xlsx"

def calculate_probabilities(input, results, keyword):
    probabilities = np.zeros_like(input)
    for i in range(len(results)):
        probabilities += results[i, keyword]
    probabilities = probabilities.astype(float) / float(len(results))
    return probabilities

def main():
    printer.header()
    season, night = printer.init()
    wb_path = get_wb_path(season, night)
    input_matrix, matching_nights, lights = workbook.load_input(wb_path)
    printer.input_stats(input_matrix)
    results, keyword = solve(input_matrix, matching_nights, lights)
    probabilities = calculate_probabilities(input_matrix, results, keyword)
    workbook.write_probabilities(wb_path, probabilities)

if __name__ == "__main__":
    main()
