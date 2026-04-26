def input_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)

        if temp > 40:
            raise Exception(f"{temp_str}°C is too hot for plants (max 40°C)")
        elif temp < 0:
            raise Exception(f"{temp_str}°C is too cold for plants (min 0°C)")

        print(f"Temperature is now {temp}°C")
        return temp

    except ValueError:
        print(
                f"Caught input_temperature error: invalid literal"
                f" for int() with base 10: '{temp_str}'"
            )
        return -1
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
        return -1


def test_temperature() -> None:
    print("=== Garden Temperature Checker===")

    test_cases: list = ["25", "abc", "100", "-50"]

    for i in test_cases:
        print(f"\nInput data is '{i}'")
        input_temperature(i)

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
