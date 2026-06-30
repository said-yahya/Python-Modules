from ex0.creature_factory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing_factory() -> None:
    print("Testing Creature with healing capability")
    factory: CreatureFactory = HealingCreatureFactory()

    print("base:")
    base = factory.create_base("Sproutling")
    print(base.describe())
    print(base.attack())
    if hasattr(base, "heal"):
        print(base.heal())

    print("evolved:")
    evolved = factory.create_evolved("Bloomelle")
    print(evolved.describe())
    print(evolved.attack())
    if hasattr(evolved, "heal"):
        print(evolved.heal())


def test_transforming_factory() -> None:
    print("\nTesting Creature with transform capability")
    factory: CreatureFactory = TransformCreatureFactory()

    print("base:")
    base = factory.create_base("Shiftling")
    print(base.describe())
    print(base.attack())
    if hasattr(base, "transform"):
        print(base.transform())
    print(base.attack())
    if hasattr(base, "revert"):
        print(base.revert())

    print("evolved:")
    evolved = factory.create_evolved("Morphagon")
    print(evolved.describe())
    print(evolved.attack())
    if hasattr(evolved, "transform"):
        print(evolved.transform())
    print(evolved.attack())
    if hasattr(evolved, "revert"):
        print(evolved.revert())


if __name__ == "__main__":
    test_healing_factory()
    test_transforming_factory()
