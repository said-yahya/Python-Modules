import random


def gen_player_achievements(achivements: list[str]) -> set[str]:
    count = random.randint(0, len(achivements))
    achived = random.sample(achivements, count)
    return set(achived)


def main() -> None:
    achivements: list[str] = [
                            "Crafting Genius", "Strategist", "World Savior",
                            "Speed Runner", "Survivor", "Master Explorer",
                            "Treasure Hunter", "Unstoppable", "First Steps",
                            "Collector Supreme", "Untouchable", "Sharp Mind",
                            "Boss Slayer", "Hidden Path Finder"
                        ]
    achivements_set = set(achivements)
    print("=== Achievement Tracker System ===\n")
    user1 = gen_player_achievements(achivements)
    user2 = gen_player_achievements(achivements)
    user3 = gen_player_achievements(achivements)
    user4 = gen_player_achievements(achivements)

    print(f"User 1 achievements: {user1}")
    print(f"User 2 achievements: {user2}")
    print(f"User 3 achievements: {user3}")
    print(f"User 4 achievements: {user4}")

    print(
            f"\nAll distinct achievements: "
            f"{set.union(user1, user2, user3, user4)}")
    print(
            f"\nCommon Achievements : "
            f"{set.intersection(user1, user2, user3, user4)}")

    print(f"\nOnly User 1: {user1.difference(user2, user3, user4)}")
    print(f"Only User 2: {user2.difference(user1, user3, user4)}")
    print(f"Only User 3: {user3.difference(user1, user2, user4)}")
    print(f"Only User 4: {user4.difference(user1, user2, user3)}")

    print(f"\nUser 1 is missing: {achivements_set.difference(user1)}")
    print(f"User 2 is missing: {achivements_set.difference(user2)}")
    print(f"User 3 is missing: {achivements_set.difference(user3)}")
    print(f"User 4 is missing: {achivements_set.difference(user4)}")


if __name__ == "__main__":
    main()
