import minizinc
import time

import printer

def solve(input_matrix, matching_nights, lights, third_wheel=-1):
    # my_driver = minizinc.find_driver(PATH)
    # my_driver.make_default()
    are_you_the_one = minizinc.Model("./are_you_the_one.mzn")
    gecode = minizinc.Solver.lookup("gecode")
    instance = minizinc.Instance(gecode, are_you_the_one)

    instance["num_girls"] = len(input_matrix)
    instance["num_boys"] = len(input_matrix[0])
    instance["num_matching_nights"] = len(matching_nights)
    instance["num_couples"] = len(matching_nights[0])

    instance["input"] = input_matrix
    instance["nights_and_couples"] = matching_nights
    instance["lights"] = lights
    instance["third_wheel"] = third_wheel

    pre_mzn = time.localtime(time.time())
    results = instance.solve(all_solutions=True)
    post_mzn = time.localtime(time.time())
    printer.solver_stats(results, pre_mzn, post_mzn)
    return results, "matches"