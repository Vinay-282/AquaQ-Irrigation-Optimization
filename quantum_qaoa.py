"""Experimental QAOA formulation for the same small irrigation toy model.

This uses binary variables x[farm, unit] indicating whether a particular water
unit is assigned to a farm. Constraints prevent assigning one unit to multiple
farms and prevent allocations beyond each farm's demand.
"""
from qiskit_optimization import QuadraticProgram
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit_algorithms import QAOA
from qiskit_algorithms.optimizers import COBYLA
from qiskit.primitives import Sampler

FARMS = ["Farm A", "Farm B", "Farm C"]
DEMAND = [3, 2, 4]
PRIORITY = [3, 2, 1]
SUPPLY = 5


def build_problem():
    qp = QuadraticProgram("toy_irrigation_allocation")
    # Binary x_i_j: water unit j is assigned to farm i.
    for i, farm in enumerate(FARMS):
        for j in range(SUPPLY):
            qp.binary_var(name=f"x_{i}_{j}")

    # Maximize priority-weighted delivered water.
    qp.maximize(
        linear={
            f"x_{i}_{j}": PRIORITY[i]
            for i in range(len(FARMS))
            for j in range(min(DEMAND[i], SUPPLY))
        }
    )

    # Every available unit can be allocated to at most one farm.
    for j in range(SUPPLY):
        qp.linear_constraint(
            linear={f"x_{i}_{j}": 1 for i in range(len(FARMS))},
            sense="<=",
            rhs=1,
            name=f"unit_{j}_at_most_one_farm",
        )

    # Each farm receives no more units than its demand.
    for i in range(len(FARMS)):
        qp.linear_constraint(
            linear={f"x_{i}_{j}": 1 for j in range(SUPPLY)},
            sense="<=",
            rhs=DEMAND[i],
            name=f"farm_{i}_demand_cap",
        )
    return qp


if __name__ == "__main__":
    problem = build_problem()
    print("Experimental QAOA run on a synthetic irrigation model")
    print(f"Variables: {problem.get_num_vars()}, constraints: {problem.get_num_linear_constraints()}")
    print("Running QAOA; simulator results can vary between runs.")
    qaoa = QAOA(sampler=Sampler(), optimizer=COBYLA(maxiter=60), reps=1)
    solver = MinimumEigenOptimizer(qaoa)
    result = solver.solve(problem)
    print("QAOA status:", result.status)
    print("QAOA objective score:", result.fval)
    print("QAOA decision variables:", result.x)
    print("Important: compare with `python classical_baseline.py`; do not infer speedup or quantum advantage from this toy run.")
