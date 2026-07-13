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
    from pydantic import BaseModel, Field, ValidationError, model_validator
    from pydantic_core import InitErrorDetails, PydanticCustomError
except ImportError:
    print(
        "WARNING: Pydantic library is not installed in your environment!!!\n"
        "Please install the required library inside your activated environment"
        ":\n    pip3 install pydantic==2.13.4\n\n"
        "After that, run this program again."
    )
    sys.exit(1)

from enum import Enum
from datetime import datetime
import json
from pathlib import Path


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember]
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation_rules(self) -> SpaceMission:
        errors: list[InitErrorDetails] = []
        if not self.mission_id.startswith("M"):
            errors.append(InitErrorDetails(
                type=PydanticCustomError("value_error", "Mission ID must "
                                         "start with 'M'"),
                loc=("mission_id",), input=self.mission_id))

        has_leader = any(member.rank in [Rank.captain, Rank.commander]
                         for member in self.crew)
        if not has_leader:
            errors.append(InitErrorDetails(
                type=PydanticCustomError("value_error", "Must have at least "
                                         "one Commander or Captain"),
                loc=("crew",), input=self.crew))

        if self.duration_days > 365:
            counter: int = 0
            for i in self.crew:
                if i.years_experience >= 5:
                    counter += 1
            if not (counter >= len(self.crew) / 2):
                errors.append(InitErrorDetails(
                    type=PydanticCustomError("value_error", "Long missions "
                                             "(> 365 days) need 50% "
                                             "experienced crew (5+ years)"),
                    loc=("crew",), input=self.crew))

        for idx, i in enumerate(self.crew):
            if not i.is_active:
                errors.append(InitErrorDetails(
                    type=PydanticCustomError("value_error", "All crew members "
                                             "must be active"),
                    loc=("crew", idx), input=i))

        if errors:
            raise ValidationError.from_exception_data(self.__class__.__name__,
                                                      errors)
        return self


def main() -> None:
    print("Space Mission Crew Validation via JSON Files")
    print("=" * 60)

    missions_path = Path("generated_data/space_missions.json")

    if missions_path.exists():
        with open(missions_path, "r", encoding="utf-8") as f:
            missions_list = json.load(f)
            
        print(f"Loaded {len(missions_list)} complete missions from generator.\n")
        for data in missions_list:
            try:
                mission = SpaceMission(**data)
                print(f" Valid mission approved for launch:")
                print(f"   Name:        {mission.mission_name}")
                print(f"   ID:          {mission.mission_id}")
                print(f"   Destination: {mission.destination}")
                print(f"   Crew size:   {len(mission.crew)} active specialists")
                print(f"   Budget:      ${mission.budget_millions}M")
                print("   Crew roster:")
                for member in mission.crew:
                    print(f"     - {member.name:<18} ({member.rank:<11}) | "
                          f"Spec: {member.specialization}")
                print("-" * 60)
            except ValidationError as e:
                print(f" Unexpected error in generated mission dataset: {e}")
    else:
        print(f" File not found: {missions_path}. Run data_exporter.py first!")

    print("\n" + "=" * 60)
    print("Testing expected complex validation failures (Manual simulation):")
    
    bad_crew = [
        CrewMember(member_id="CM999", name="Inactive Cadet", rank=Rank.cadet,
                   age=19, specialization="Training", years_experience=0,
                   is_active=False)
    ]
    
    try:
        SpaceMission(
            mission_id="INVALID_ID",
            mission_name="Broken Mission",
            destination="Unknown",
            launch_date=datetime.now(),
            duration_days=500,
            crew=bad_crew,
            budget_millions=500.0
        )
    except ValidationError as e:
        print(" Successfully caught multiple nested block errors "
              "simultaneously:")
        for error in e.errors():
            clean_msg = error['msg'].replace("Value error, ", "")
            print(f"    Location {error['loc']}: {clean_msg}")


if __name__ == "__main__":
    main()
