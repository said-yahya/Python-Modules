class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name.capitalize() != plant_name:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")

    print("Testing valid plant...")
    test_watering_system(["Rose", "Tulip", "Daisy"])

    print("\nTesting invalid plant...")
    test_watering_system(["Rose", "tulip", "Daisy"])

    print("\nCleanup always happens, even with errors!")
