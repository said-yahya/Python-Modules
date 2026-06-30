from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy, \
                      InvalidStrategyException
from ex0.creature_factory import CreatureFactory
from ex2.strategy import BattleStrategy


def run_battle_tournament(opponents: list[tuple[CreatureFactory,
                                                BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            fac_a, strat_a = opponents[i]
            fac_b, strat_b = opponents[j]
            if isinstance(fac_a, FlameFactory):
                name_a = "Flameling"
            elif isinstance(fac_a, AquaFactory):
                name_a = "Aquabub"
            elif isinstance(fac_a, HealingCreatureFactory):
                name_a = "Sproutling"
            else:
                name_a = "Shiftling"

            if isinstance(fac_b, FlameFactory):
                name_b = "Flameling"
            elif isinstance(fac_b, AquaFactory):
                name_b = "Aquabub"
            elif isinstance(fac_b, HealingCreatureFactory):
                name_b = "Sproutling"
            else:
                name_b = "Shiftling"

            c_a = fac_a.create_base(name_a)
            c_b = fac_b.create_base(name_b)

            print("* Battle *")
            print(c_a.describe())
            print("VS.")
            print(c_b.describe())
            print("now fight!")

            try:
                print(strat_a.act(c_a))
                print(strat_b.act(c_b))
            except InvalidStrategyException as e:
                print(f"Battle error, aborting tournament: {e}")
                return
            print()


if __name__ == "__main__":
    flame_fac = FlameFactory()
    aqua_fac = AquaFactory()
    healing_fac = HealingCreatureFactory()
    transform_fac = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament  (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive)]")
    run_battle_tournament([
        (flame_fac, normal),
        (healing_fac, defensive)
    ])

    print("-" * 40)

    print("Tournament 1 (error)")
    print("[(Flameling+Aggressive), (Healing+Defensive) ]")
    run_battle_tournament([
        (flame_fac, aggressive),
        (healing_fac, defensive)
    ])

    print("-" * 40)

    print("Tournament 2 (multiple)")
    print("[(Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive)]")
    run_battle_tournament([
        (aqua_fac, normal),
        (healing_fac, defensive),
        (transform_fac, aggressive)
    ])
