# PROMETHEUS

A small Python city simulation with two citizens who move between districts and manage their energy.

## What it does

- Simulates six turns in the city.
- Moves Mira and Jon between Town Square, Market, and Park.
- Citizens spend energy while moving and rest when their energy is low.
- Prints each turn and the citizens' final locations and energy.
- Saves a CSV log of each action in the `outputs` folder.

## Run the simulation

From the project folder, run:

```powershell
py src\main.py
```

## Project files

- `src\main.py` — simulation code
- `outputs\` — generated CSV logs
- `data\` — reserved for future simulation data

## CSV log columns

Each log includes the turn, citizen, event, district, and energy.