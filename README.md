# PROMETHEUS

A Python city simulation featuring rule-based citizens, district movement, energy management, and hunger.

## What it does

- Simulates six turns in the city.
- Moves Mira and Jon between Town Square, Market, and Park.
- Citizens spend energy while moving and rest when their energy is low.
- Hunger increases each turn. Hungry citizens travel to the Market to eat.
- Prints each turn and the citizens' final locations, energy, and hunger.
- Saves a timestamped CSV log in the `outputs` folder.

## Run the simulation

From the project folder, run `py src\main.py`.

## Project files

- `src\main.py` — simulation code
- `outputs\` — generated CSV logs

## CSV log columns

Each log includes the turn, citizen, event, district, energy, and hunger.