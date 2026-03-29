#!/usr/bin/env python3

class SecurePlant():
    def __init__(self, name: str) -> None:
        self.name: str = name
        self._height: int = 0
        self._age: int = 0
        print(f"Created: {self.name}")

    def set_height(self, height) -> None:
        if (height < 0):
            print(
                    f"\nInvalid operation attempted:"
                    f" height {height}cm [REJECTED]"
                )
            print("Security: Negative height rejected\n")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, age) -> None:
        if (age < 0):
            print(f"\nInvalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self._age = age
            print(f"Age updated: {self._age} days [OK]")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age


def main() -> None:
    print("=== Garden Security System ===")

    rose = SecurePlant("Rose")

    rose.set_height(25)
    rose.set_age(30)

    rose.set_height(-5)

    curr_name: str = rose.name
    curr_h: int = rose.get_height()
    curr_a: int = rose.get_age()

    print(f"Current plant: {curr_name} ({curr_h}cm, {curr_a} days)")


if __name__ == "__main__":
    main()
