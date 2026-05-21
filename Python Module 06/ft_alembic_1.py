from elements import create_water


if __name__ == "__main__":
    print("=== Alembic 1 ===")
    print("Using:'from ... import ...' structure to access elements.py")
    water: str = create_water()
    print(f"Testing create_fire: {water}")
