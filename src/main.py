import csv
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


DISTRICTS = ["Town Square", "Market", "Park"]
TOTAL_TURNS = 6


@dataclass
class Citizen:
    name: str
    district_index: int = 0
    energy: int = 10

    def take_action(self) -> str:
        if self.energy <= 7:
            self.energy += 2
            district = DISTRICTS[self.district_index]
            return f"{self.name} rests in {district}. Energy: {self.energy}"

        self.district_index = (self.district_index + 1) % len(DISTRICTS)
        self.energy -= 1
        district = DISTRICTS[self.district_index]
        return f"{self.name} moves to {district}. Energy: {self.energy}"


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
            ])

    print("\nFinal status")
    for citizen in citizens:
        district = DISTRICTS[citizen.district_index]
        print(f"{citizen.name}: {district}, energy {citizen.energy}")

    output_folder = Path(__file__).resolve().parent.parent / "outputs"
    output_folder.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = output_folder / f"city_log_{timestamp}.csv"

    with log_path.open("w", newline="", encoding="utf-8") as csv_file:
        log_writer = csv.writer(csv_file)
        log_writer.writerow(["turn", "citizen", "event", "district", "energy"])
        log_writer.writerows(log_rows)

    print(f"\nSaved simulation log to: {log_path}")


if __name__ == "__main__":
    main()