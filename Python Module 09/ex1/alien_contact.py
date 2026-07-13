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
import json
from pathlib import Path


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
    print("Alien Contact Log Validation via JSON Files")
    print("=" * 50)

    valid_path = Path("generated_data/alien_contacts.json")
    invalid_path = Path("generated_data/invalid_contacts.json")

    if valid_path.exists():
        with open(valid_path, "r", encoding="utf-8") as f:
            contacts_list = json.load(f)

        print(f"Loaded {len(contacts_list)} contact logs from generator.")
        for data in contacts_list:
            try:
                contact = AlienContact(**data)
                print(f"Valid contact: {contact.contact_id} | Type: "
                      f"{contact.contact_type.value}")
            except ValidationError as e:
                print(f"Unexpected error on valid contact: {e}")
    else:
        print(f"File not found: {valid_path}. Run data_exporter.py first!")

    print("-" * 50)

    print("Testing expected business logic validation errors:")
    if invalid_path.exists():
        with open(invalid_path, "r", encoding="utf-8") as f:
            invalid_list = json.load(f)

        for data in invalid_list:
            try:
                AlienContact(**data)
                print(f"Failure: Invalid contact {data.get('contact_id')} "
                      "passed!")
            except ValidationError as e:
                print("Caught expected custom error:")
                for error in e.errors():
                    clean_msg = error['msg'].replace("Value error, ", "")
                    print(f"   Field {error['loc']}: {clean_msg}")

    else:
        print(f"File not found: {invalid_path}")


if __name__ == "__main__":
    main()
