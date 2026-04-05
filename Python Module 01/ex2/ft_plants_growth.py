#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, height: float, age: int):
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

    def grow(self) -> None:
<<<<<<< HEAD
        self.height += 1
=======
        self.height += 0.8
>>>>>>> b17fbc7 (subject v3.0)

    def aging(self) -> None:
        self.age += 1


def main() -> None:
    rose = Plant("Rose", 25, 30)
    first_height: float = rose.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.show()
        if (day != 7):
            rose.aging()
            rose.grow()

    print(f"Growth this week: {(rose.height - first_height):.1f}cm")


if __name__ == "__main__":
    main()
