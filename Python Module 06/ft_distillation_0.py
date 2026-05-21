from alchemy import potions


if __name__ == "__main__":
    print("=== Distillation 0 ===\nDirect access to alchemy/potions.py")
    heal: str = potions.healing_potion()
    strength: str = potions.strength_potion()
    print(f"Testing strength_potion: {heal}")
    print(f"Testing healing_potion:{strength}")
