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
import json
from pathlib import Path


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
    print("Space Station Data Validation via JSON Files")
    print("=" * 40)

    valid_path = Path("../generated_data/space_stations.json")
    invalid_path = Path("../generated_data/invalid_stations.json")

    if valid_path.exists():
        with open(valid_path, "r", encoding="utf-8") as f:
            stations_list = json.load(f)

        print(f"Loaded {len(stations_list)} stations from generator.")
        for data in stations_list:
            try:
                station = SpaceStation(**data)
                print(f" Successfully validated: {station.name} "
                      f"({station.station_id})")
            except ValidationError as e:
                print(f" Unexpected error on valid data: {e}")
    else:
        print(f" File not found: {valid_path}. Run data_exporter.py first!")

    print("-" * 40)

    print("Testing expected validation errors:")
    if invalid_path.exists():
        with open(invalid_path, "r", encoding="utf-8") as f:
            invalid_list = json.load(f)

        for data in invalid_list:
            try:
                SpaceStation(**data)
                print(" Failure: Invalid data passed validation unchecked!")
            except ValidationError as e:
                print(" Caught expected error(s):")
                for error in e.errors():
                    print(f"   Field {error['loc']}: {error['msg']}")
    else:
        print(f" File not found: {invalid_path}")


if __name__ == "__main__":
    main()
