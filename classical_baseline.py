"""Small exact classical baseline for discrete irrigation allocation."""
from itertools import product

FARMS = ["Farm A", "Farm B", "Farm C"]
DEMAND = [3, 2, 4]       # water units requested
PRIORITY = [3, 2, 1]     # value per unit delivered
SUPPLY = 5


def solve_exact():
    best_score = -1
    best_alloc = None
    # Each farm allocation is an integer from 0 to its demand.
    for allocation in product(*(range(d + 1) for d in DEMAND)):
        if sum(allocation) > SUPPLY:
            continue
        score = sum(a * p for a, p in zip(allocation, PRIORITY))
        if score > best_score:
            best_score, best_alloc = score, allocation
    return best_score, best_alloc


if __name__ == "__main__":
    score, allocation = solve_exact()
    print("Toy irrigation allocation — exact classical baseline")
    print(f"Available water units: {SUPPLY}")
    print(f"Weighted allocation score: {score}")
    for farm, amount, demand in zip(FARMS, allocation, DEMAND):
        print(f"{farm}: allocate {amount}/{demand} units")
    print("Note: this is a synthetic example, not a real-world recommendation.")
