def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "grams":
        result = f"{quantity} {unit} total"
    elif unit == "packets":
        result = f"{quantity} {unit} available"
    elif unit == "area":
        result = f"covers {quantity} square meters"
    else:
        print("Unknown unit type")
        return
    print(f"{seed_type.capitalize()} seeds: {result}")
