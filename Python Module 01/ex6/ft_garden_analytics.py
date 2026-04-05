#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def display(self) -> None:
            print(
                    f"Stats: {self._grow_calls} grow, "
                    f"{self._age_calls} age, {self._show_calls} show"
                )

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age
        self._analytics: Plant.Stats = self.Stats()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> 'Plant':
        return cls("Unknown plant", 0.0, 0)

    def grow(self, x: float) -> None:
        if x > 0:
            self.height += x
        self._analytics._grow_calls += 1

    def aging(self, days: int) -> None:
        if days > 0:
            self.age += days
        self._analytics._age_calls += 1

    def show(self) -> None:
        self._analytics._show_calls += 1
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.is_blooming: bool = False

    def bloom(self) -> None:
        self.is_blooming = True
        print(f" {self.name} is blooming beautifully!")

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if not self.is_blooming:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")


class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def display(self) -> None:
            super().display()
            print(f"{self._shade_calls} shade")

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter
        self._analytics: Tree.TreeStats = self.TreeStats()

    def produce_shade(self) -> None:
        self._analytics._shade_calls += 1
        print(f"Tree {self.name} now produces a shade of {self.height:.1f}cm "
              f"long and {self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


def display_plant_analytics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant._analytics.display()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    age1, age2 = 30, 400
    print(
            f"Is {age1} days more than a year? -> "
            f"{Plant.is_older_than_year(age1)}"
        )
    print(
            f"Is {age2} days more than a year? -> "
            f"{Plant.is_older_than_year(age2)}"
        )

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_analytics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    display_plant_analytics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_analytics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_analytics(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.aging(20)
    sunflower.bloom()
    sunflower.show()
    display_plant_analytics(sunflower)

    print("\n=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    display_plant_analytics(anon)


if __name__ == "__main__":
    main()
