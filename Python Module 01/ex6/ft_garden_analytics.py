#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age
        self.plant_type: str = "regular"

    def grow(self) -> int:
        self.height += 1
        return self.height

    def print_info(self) -> None:
        print(f"{self.name}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.plant_type: str = "flowering"
        self.color: str = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def print_info(self) -> None:
        print(
                f"{self.name}: {self.height}cm, "
                f"{self.color} flowers (blooming)"
            )


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int,
                 color: str, prize_points: int) -> None:

        super().__init__(name, height, age, color)
        self.plant_type: str = "prize flowers"
        self.prize_points: int = prize_points

    def print_info(self) -> None:
        print(
                f"{self.name}: {self.height}cm, {self.color} "
                f"flowers (blooming), Prize points: {self.prize_points}"
            )


class GardenManager:
    total_managers: int = 0

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.plants: list = []
        self._totalPlants: int = 0
        self._totalGrowth: int = 0
        GardenManager.create_garden_network()

    @classmethod
    def create_garden_network(cls) -> None:
        cls.total_managers += 1

    class GardenStats:
        @staticmethod
        def validate_height(height: int) -> bool:
            return height >= 0

        @staticmethod
        def calculate_score(manager: 'GardenManager') -> int:
            base_score: int = manager._totalPlants * 10 + manager._totalGrowth
            bonus: int = 0

            for i in range(manager._totalPlants):
                plant = manager.plants[i]
                if plant.plant_type == "prize flowers":
                    bonus += plant.prize_points

            return base_score + bonus

    def manager_info(self, other: 'GardenManager') -> None:
        test_val: bool = False
        if self.plants:
            test_val = self.GardenStats.validate_height(self.plants[0].height)
        print(f"Height validation test: {test_val}")

        my_score: int = self.GardenStats.calculate_score(self)
        other_score: int = self.GardenStats.calculate_score(other)

        print(
                f"Garden scores {self.name}: {my_score}, "
                f"{other.name}: {other_score}"
            )
        print(f"Total gardens managed: {GardenManager.total_managers}")

    def add_plant(self, plant: Plant) -> None:
        self._totalPlants += 1
        self.plants += [plant]

    def growing(self) -> None:
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self._totalGrowth += 1
            print(f"{plant.name} grew 1cm")

    def get_report(self) -> None:
        print(f"\n=== {self.name}'s Garden Report ===")
        reg: int = 0
        flow: int = 0
        prz: int = 0

        print("Plants in garden")
        for plant in self.plants:
            plant.print_info()
            if plant.plant_type == "regular":
                reg += 1
            elif plant.plant_type == "flowering":
                flow += 1
            elif plant.plant_type == "prize flowers":
                prz += 1
        print(
                f"\nPlants added: {self._totalPlants}, "
                f"Total growth: {self._totalGrowth}cm"
            )
        print(
                f"Plants types: {reg} regular, {flow} "
                f"flowering, {prz} prize flowers\n"
            )


def main() -> None:
    print("Garden Management System Demo")

    alice = GardenManager("Alice")
    bob = GardenManager("Bob")

    oak = Plant("Oak Tree", 100, 365)
    rose = FloweringPlant("Rose", 25, 30, "red")
    sunflower = PrizeFlower("Sunflower", 50, 45, "yellow", 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    alice.growing()

    alice.get_report()
    alice.manager_info(bob)


if __name__ == "__main__":
    main()
