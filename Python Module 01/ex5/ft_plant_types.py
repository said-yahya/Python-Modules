#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def grow(self) -> None:
        self.height += 1

    def aging(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.bloom_status: bool = False

    def bloom(self) -> None:
        self.bloom_status = True
        print(f"[asking the {self.name} to bloom]")

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloom_status:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        print(
                f"[asking the {self.name} to produce shade]\n"
                f"Tree {self.name} now produces a shade of {self.height:.1f}cm"
                f" long and {self.trunk_diameter:.1f}cm wide."
            )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = 0

    def show(self) -> None:
        super().show()
        print(
                f" Harvest season: {self.harvest_season}\n"
                f" Nutrition value: {self.nutritional_value}"
            )

    def growing(self, day: int) -> None:
        if day < 1:
            print("Invalid input, day cannot be les than 1!!!")
        else:
            print(f"[make {self.name} grow and age for {day} days]")
            for _ in range(day):
                self.aging()
                self.height += 2.1
                self.nutritional_value += 1


def main() -> None:
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25.0, 30, "red")
    lily = Flower("Lily", 35, 15, "white")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 400, 1000, 40)

    tomato = Vegetable("Tomato", 5, 10, "summer")
    carrot = Vegetable("Carrot", 10, 30, "autumn")

    print("\n=== Flower")
    rose.show()
    rose.bloom()
    rose.show()

    lily.show()
    lily.bloom()
    lily.show()

    print("\n=== Tree")
    oak.show()
    oak.produce_shade()

    pine.show()
    pine.produce_shade()

    print("\n=== Vegetable")
    tomato.show()
    tomato.growing(20)
    tomato.show()

    carrot.show()


if __name__ == "__main__":
    main()
