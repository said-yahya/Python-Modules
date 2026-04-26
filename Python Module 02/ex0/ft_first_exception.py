def input_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)
        print(f"Temperature is now {temp}°C")
        return temp

    except ValueError:
        print(
                f"Caught input_temperature error: invalid literal"
                f" for int() with base 10: '{temp_str}'"
            )
        return 0


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    print("Input data is '25'")
    input_temperature("25")

    print("\nInput data is 'abc'")
    input_temperature("abc")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
