#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age
        print(f"Created: {self.name} ({self.height:.1f}cm, {self.age} days)")

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

    def grow(self) -> None:
        self.height += 1

    def aging(self) -> None:
        self.age += 1
        self.grow()


def main() -> None:
    count: int = 0

    print("=== Plant Factory Output ===")
    plants: list[Plant] = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]

    for _ in plants:
        count += 1

    print(f"\nTotal plants created: {count}")


if __name__ == "__main__":
    main()
