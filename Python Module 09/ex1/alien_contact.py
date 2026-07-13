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
from typing import Optional


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_cosmic_rules(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')

        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError('Physical contact reports must be verified')

        if self.contact_type == ContactType.telepathic and \
           self.witness_count < 3:
            raise ValueError("Telepathic contact requires at"
                             " least 3 witnesses")

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include "
                             "received messages")

        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")

    try:
        valid_report = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.fromisoformat("2026-07-12T05:00:00"),
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=False
        )
        print("Valid contact report:")
        print(f"ID: {valid_report.contact_id}")
        print(f"Type: {valid_report.contact_type.value}")
        print(f"Location: {valid_report.location}")
        print(f"Signal: {valid_report.signal_strength}/10")
        print(f"Duration: {valid_report.duration_minutes} minutes")
        print(f"Witnesses: {valid_report.witness_count}")
        if valid_report.message_received:
            print(f"Message: '{valid_report.message_received}'")

    except ValidationError as e:
        print(f"Unexpected error validation: {e}")

    print("======================================")
    print("Expected validation error:")

    try:
        AlienContact(
            contact_id="AC_2026_002",
            timestamp=datetime.now(),
            location="Secret Base",
            contact_type=ContactType.telepathic,
            signal_strength=4.0,
            duration_minutes=10,
            witness_count=1,
            message_received="Mind meld complete",
            is_verified=False
        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
