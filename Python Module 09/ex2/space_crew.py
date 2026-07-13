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
    print("Space Mission Crew Validation")
    print("======================================")

    sarah = CrewMember(
        member_id="C001", name="Sarah Connor", rank=Rank.commander,
        age=45, specialization="Mission Command", years_experience=15)
    john = CrewMember(
        member_id="C002", name="John Smith", rank=Rank.lieutenant,
        age=32, specialization="Navigation", years_experience=6)
    alice = CrewMember(
        member_id="C003", name="Alice Johnson", rank=Rank.officer,
        age=28, specialization="Engineering", years_experience=3)

    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.fromisoformat("2026-07-20T08:00:00"),
            duration_days=900,
            crew=[sarah, john, alice],
            budget_millions=2500.0
        )

        print("Valid mission created:")
        print(f"Mission: {valid_mission.mission_name}")
        print(f"ID: {valid_mission.mission_id}")
        print(f"Destination: {valid_mission.destination}")
        print(f"Duration: {valid_mission.duration_days} days")
        print(f"Budget: ${valid_mission.budget_millions}M")
        print(f"Crew size: {len(valid_mission.crew)}")
        print("Crew members:")
        for m in valid_mission.crew:
            print(f"  {m.name:<15} ({m.rank:<11}) {m.specialization}")

    except ValidationError as e:
        for error in e.errors():
            print(error['msg'].replace("Value error, ", ""))

    print("======================================")
    print("Expected validation error:")

    cadet_bob = CrewMember(
        member_id="C004", name="Bob Evans", rank=Rank.cadet,
        age=20, specialization="Engineering", years_experience=0
    )

    try:
        SpaceMission(
            mission_id="M2026_MOON",
            mission_name="Lunar Training Operations",
            destination="Moon",
            launch_date=datetime.fromisoformat("2026-08-15T12:00:00"),
            duration_days=30,
            crew=[john, cadet_bob],
            budget_millions=150.0
        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
