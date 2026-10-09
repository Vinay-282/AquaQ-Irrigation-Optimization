# Submission description draft (edit team name/repository link before submitting)

## 1. Novelty (under 50 words)
AquaQ explores priority-aware irrigation allocation when water supply is limited. It models farm demand and priority as a discrete optimization problem, making trade-offs explicit and allowing the same scenario to be tested with classical and quantum-inspired/quantum optimization workflows. The current prototype uses synthetic data and is not a field deployment.

## 2. Level of Qiskit programming (under 50 words)
The experimental implementation formulates binary allocation decisions and linear constraints in Qiskit Optimization, then submits the model to QAOA through a minimum-eigenvalue optimizer. The QAOA script is an experimental prototype; its successful execution and output must be verified in the target environment before claiming a completed quantum run.

## 3. Measurable results and classical benchmark (under 50 words)
The repository includes an exhaustive classical solver for the small synthetic instance and a QAOA experiment targeting the same priority-weighted objective. Report the actual objective values, feasibility, runtime, and repeated-run variation after executing both scripts. No performance figures are claimed in this draft because results have not yet been measured.

## 4. Technical quantum advantage (under 50 words)
This prototype investigates whether a variational quantum algorithm can produce feasible, high-quality allocations for a constrained binary optimization model. It does not establish quantum advantage. A defensible advantage claim would require repeated, controlled comparisons against strong classical solvers on appropriately sized instances, including runtime and solution quality.
