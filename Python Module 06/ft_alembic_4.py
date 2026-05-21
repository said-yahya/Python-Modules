import alchemy


if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print("Accessing alchemy/elements.py using'from ... import ...'structure")
    air: str = alchemy.elements.create_air()
    print(f"Testing create_earth: {air}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    try:
        earth: str = alchemy.create_earth()
    except Exception as e:
        print(e)
