import alchemy


if __name__ == "__main__":
    print("=== Distillation 1 ===")
    print("Using:'import alchemy' structure to access potions")
    heal: str = alchemy.heal()
    strength: str = alchemy.strength_potion()
    print(f"Testing strength_potion: {strength}")
    print(f"Testing heal alias: {heal}")
