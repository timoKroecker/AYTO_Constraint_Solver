from minizinc import Instance, Model, Solver

def solve(input):
    are_you_the_one = Model("./are_you_the_one.mzn")
    gecode = Solver.lookup("gecode")
    instance = Instance(gecode, are_you_the_one)
    instance["num_girls"] = len(input)
    instance["num_boys"] = len(input[0])
    instance["input"] = input

    result = instance.solve()
    for row in result["solution"]:
        print(row)
