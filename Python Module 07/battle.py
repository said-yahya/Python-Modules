from ex0 import FlameFactory, AquaFactory
from ex0.creature_factory import CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    if isinstance(factory, FlameFactory):
        base_name = "Flameling"
        evolved_name = "Pyrodon"
    elif isinstance(factory, AquaFactory):
        base_name = "Aquabub"
        evolved_name = "Torragon"
    else:
        base_name = "Base_Creature"
        evolved_name = "Evolved_Creature"

    base = factory.create_base(base_name)
    evolved = factory.create_evolved(evolved_name)

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(factory_a: CreatureFactory,
                factory_b: CreatureFactory) -> None:
    creature_1 = factory_a.create_base("Flameling")
    creature_2 = factory_b.create_base("Aquabub")

    print(f"{creature_1.describe()}\n VS.")
    print(f"{creature_2.describe()}")
    print("fight!")
    print(creature_1.attack())
    print(creature_2.attack())


if __name__ == "__main__":
    flame_fac = FlameFactory()
    aqua_fac = AquaFactory()

    print("Testing factory")
    test_factory(flame_fac)

    print("\nTesting factory")
    test_factory(aqua_fac)

    print("\nTesting battle")
    test_battle(flame_fac, aqua_fac)
