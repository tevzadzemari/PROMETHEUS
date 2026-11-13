import csv
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


DISTRICTS = ["Town Square", "Market", "Park"]
TOTAL_TURNS = 6
HUNGER_LIMIT = 3
HUNGER_REDUCTION = 4
LOW_ENERGY = 7


@dataclass
class Citizen:
    name: str
    district_index: int = 0
    energy: int = 10
    hunger: int = 0

    def take_action(self) -> str:
        self.hunger += 1
        current_district = DISTRICTS[self.district_index]

        if self.hunger >= HUNGER_LIMIT and current_district == "Market":
            self.hunger = max(0, self.hunger - HUNGER_REDUCTION)
            return (
                f"{self.name} eats at the Market. "
                f"Energy: {self.energy}, Hunger: {self.hunger}"
            )

        if self.energy <= LOW_ENERGY:
            self.energy += 2
            return (
                f"{self.name} rests in {current_district}. "
                f"Energy: {self.energy}, Hunger: {self.hunger}"
            )

        if self.hunger >= HUNGER_LIMIT:
            market_index = DISTRICTS.index("Market")

            if self.district_index < market_index:
                self.district_index += 1
            else:
                self.district_index -= 1

            self.energy -= 1
            district = DISTRICTS[self.district_index]
            return (
                f"{self.name} looks for food and moves to {district}. "
                f"Energy: {self.energy}, Hunger: {self.hunger}"
            )

        self.district_index = (self.district_index + 1) % len(DISTRICTS)
        self.energy -= 1
        district = DISTRICTS[self.district_index]
        return (
            f"{self.name} moves to {district}. "
            f"Energy: {self.energy}, Hunger: {self.hunger}"
        )


def main() -> None:
    citizens = [
        Citizen("Mira"),
        Citizen("Jon", district_index=1),
    ]
    log_rows = []

    print("PROMETHEUS city simulation")

    for turn in range(1, TOTAL_TURNS + 1):
        print(f"\nTurn {turn}")

        for citizen in citizens:
            event = citizen.take_action()
            print(event)

            log_rows.append([
                turn,
                citizen.name,
                event,
                DISTRICTS[citizen.district_index],
                citizen.energy,
                citizen.hunger,
            ])

    print("\nFinal status")
    for citizen in citizens:
        district = DISTRICTS[citizen.district_index]
        print(
            f"{citizen.name}: {district}, "
            f"energy {citizen.energy}, hunger {citizen.hunger}"
        )

    output_folder = Path(__file__).resolve().parent.parent / "outputs"
    output_folder.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = output_folder / f"city_log_{timestamp}.csv"

    with log_path.open("w", newline="", encoding="utf-8") as csv_file:
        log_writer = csv.writer(csv_file)
        log_writer.writerow([
            "turn",
            "citizen",
            "event",
            "district",
            "energy",
            "hunger",
        ])
        log_writer.writerows(log_rows)

    print(f"\nSaved simulation log to: {log_path}")


if __name__ == "__main__":
    main()