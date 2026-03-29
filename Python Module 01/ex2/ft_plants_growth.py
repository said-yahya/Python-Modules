#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self):
        self.height += 1

    def aging(self) -> None:
        self.age += 1
        self.grow()


def main() -> None:
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    rose.get_info()
    first_age = rose.height

    for _ in range(6):
        rose.aging()

    print("=== Day 7 ===")
    rose.get_info()
    print(f"Growth this week: +{rose.height - first_age}cm")


if __name__ == "__main__":
    main()
