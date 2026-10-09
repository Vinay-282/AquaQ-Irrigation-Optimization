# AquaQ: Quantum-Assisted Irrigation Allocation (Prototype)

**Status:** Emergency submission prototype for Qiskit Fall Fest 2026. This repository contains a small classical baseline and an experimental Qiskit/QAOA implementation. Results must be generated locally before reporting numerical claims.

## Problem
Allocate a limited number of water units among farms with different demands and priorities. The objective is to favor high-priority unmet demand while never exceeding the available supply or a farm's demand.

## Prototype assumptions
- Water is discretized into equal-sized units.
- Each unit can be assigned to at most one farm.
- Each farm can receive no more than its demand.
- Priority weights represent the value of satisfying a farm's demand.
- This is a toy model, not a field-ready irrigation recommendation system.

## Files
- `classical_baseline.py`: exhaustive classical solver for the small example.
- `quantum_qaoa.py`: Qiskit Optimization + QAOA experiment for the same model.
- `requirements.txt`: Python dependencies.
- `SUBMISSION_DRAFT.md`: concise descriptions aligned to the four organizer criteria.

## Run the classical baseline
```bash
python classical_baseline.py
```

## Run the QAOA experiment
Use Python 3.10 or 3.11 in a virtual environment, then:
```bash
pip install -r requirements.txt
python quantum_qaoa.py
```
The QAOA run is stochastic and may return a suboptimal result. Compare objective scores on the same toy instance; do not claim quantum advantage unless measured evidence supports it.

## Limitations / next steps
This is a small, synthetic proof of concept. It does not use live weather, soil moisture, reservoir telemetry, crop science data, or real farm constraints. Future work should validate the model with domain experts and compare repeated runs across larger instances.
