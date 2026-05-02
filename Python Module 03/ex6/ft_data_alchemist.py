import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    initial = ["Alice", "bob", "Charlie", "dylan", "Emma",
               "Gregory", "john", "kevin", "Liam"]

    new_list1 = [n.capitalize() for n in initial]
    new_list2 = [n for n in initial if n == n.capitalize()]

    dict1 = {n: random.randint(0, 1000) for n in new_list1}
    average = round(sum(dict1.values()) / len(new_list1), 2)
    dict2 = {key: value for key, value in dict1.items() if value > average}

    print(f"\nInitial list of players: {initial}")
    print(f"New list with all names capitalized: {new_list1}")
    print(f"New list of capitalized names only: {new_list2}")
    print(f"\nScore dict: {dict1}")
    print(f"Score average is {average}")
    print(f"\nHigh scores: {dict2}")


if __name__ == "__main__":
    main()
