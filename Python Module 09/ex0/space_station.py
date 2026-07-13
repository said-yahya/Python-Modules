import sys


if sys.prefix == sys.base_prefix:
    print(
        "WARNING: Virtual Environment not activated!!!\n"
        "Follow instructions below:\n"
        "To create Virtual Environment use this command:\n"
        "    python3 -m venv venv\n"
        "Then activate venv by using this command:\n"
        "    source venv/bin/activate\n"
    )
    sys.exit(1)

try:
    from pydantic import BaseModel, Field, ValidationError
except ImportError:
    print(
        "WARNING: Pydantic library is not installed in your environment!!!\n"
        "Please install the required library inside your activated environment"
        ":\n    pip3 install pydantic==2.13.4\n\n"
        "After that, run this program again."
    )
    sys.exit(1)


from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("-" * 30)

    try:
        valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.fromisoformat("2026-07-09T12:00:00"),
            is_operational=True,
            notes="Routine systems check nominal."
        )
        print("Valid station created:")
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        if valid_station.is_operational:
            print("Status: Operational")
        else:
            print("Status: Non-Operational")
        if valid_station.notes:
            print(f"Notes: {valid_station.notes}")

    except ValidationError as e:
        print(f"Unexpected error creating valid station: {e}")

    print("-" * 30)

    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="MIR002",
            name="Deep Space Outpost",
            crew_size=25,
            power_level=99.0,
            oxygen_level=95.0,
            last_maintenance=datetime.now(),
        )
    except ValidationError as e:
        for error in e.errors():
            if error['loc'] == ('crew_size',):
                print(error['msg'])


if __name__ == "__main__":
    main()
