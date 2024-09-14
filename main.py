import numpy as np

import workbook_interface as workbook
import printer
from minizinc_interface import solve

LATEST = "13-09-2024"
WB_PATH = "excel/" + LATEST + ".xlsx"

def calculate_probabilities(input, results, keyword):
    print("num_results: ", len(results))
    probabilities = np.zeros_like(input)
    for i in range(len(results)):
        result = np.array(results[i, keyword])
        probabilities += result
    probabilities = probabilities.astype(float) / float(len(results))
    return probabilities

def main():
    printer.header()
    input_matrix, matching_nights, lights = workbook.load_input(WB_PATH)
    printer.input_stats(input_matrix)
    results, keyword = solve(input_matrix, matching_nights, lights)
    probabilities = calculate_probabilities(input_matrix, results, keyword)
    workbook.write_probabilities(WB_PATH, probabilities)

if __name__ == "__main__":
    main()
