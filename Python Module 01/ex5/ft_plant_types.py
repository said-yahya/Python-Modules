#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def print_info(self) -> None:
        print(
                f"\n{self.name} (Flower): {self.height}cm, "
                f"{self.age} days, {self.color} color"
            )


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 diameter: int) -> None:
        super().__init__(name, height, age)
        self.diameter: int = diameter

    def produce_shade(self) -> None:
        shade: int = (self.diameter / 10) ** 2 * 3.14
        print(f"{self.name} provides {shade} square meters of shade")

    def print_info(self) -> None:
        print(
                f"\n{self.name} (Tree): {self.height}cm, "
                f"{self.age} days, {self.diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str,  nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def include(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")

    def print_info(self) -> None:
        print(
                f"\n{self.name} (Vagetable): {self.height}cm, "
                f"{self.age} days, {self.harvest_season} harvest"
            )


def main() -> None:
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "red")
    lily = Flower("Lily", 35, 15, "white")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 400, 1000, 40)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 20, 70, "autumn", "beta-carotene")

    rose.print_info()
    rose.bloom()

    lily.print_info()
    lily.bloom()

    oak.print_info()
    oak.produce_shade()

    pine.print_info()
    pine.produce_shade()

    tomato.print_info()
    tomato.include()

    carrot.print_info()
    carrot.include()


if __name__ == "__main__":
    main()
