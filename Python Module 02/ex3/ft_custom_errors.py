class GardenError(Exception):
    def __init__(self, message="Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Not enough water") -> None:
        super().__init__(message)


def check_water(water_level: int) -> None:
    if water_level < 10:
        raise WaterError(f"Water level {water_level} is too low for plants")


def check_plant(status: str):
    if status == "wilting":
        raise PlantError("The plant is wilting!")


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")

    try:
        check_water(5)
    except WaterError as e:
        print(f"Caught a water error: {e}")

    try:
        check_plant("wilting")
    except PlantError as e:
        print(f"Caught a plant error: {e}")

    print("Testing catching all garden errors...")
    errors_to_test = [
        lambda: check_plant("wilting"),
        lambda: check_water(5)
    ]

    for action in errors_to_test:
        try:
            action()
        except GardenError as e:
            print(f"Caught GardenError: {e}")

    print("\nAll custom error tests completed successfully!")


if __name__ == "__main__":
    test_custom_errors()
