#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self) -> None:
        self.height += 1

    def aging(self) -> None:
        self.age += 1
        self.grow()


def main() -> None:
    plants_list = [
        ["Rose", 25, 30],
        ["Dak", 200, 365],
        ["Cactus", 5, 90],
        ["Sunflower", 80, 45],
        ["Fern", 15, 120]
    ]
    plants_class_list: list = []
    count: int = 0
    print("=== Plant Factory Output ===")
    for data in plants_list:
        plants_class_list += [Plant(data[0], data[1], data[2])]
        count += 1

    print(f"\nTotal plants created: {count}")


if __name__ == "__main__":
    main()
