import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    args = sys.argv[1:]
    inventory: dict = {}
    for arg in args:
        if ":" in arg:
            arg_list: list = arg.split(":", 1)
            key: str = arg_list[0]
            v: str = arg_list[1]
            if key not in inventory:
                try:
                    value: int = int(v)
                    inventory.update({key: value})
                except ValueError:
                    print(
                            f"Quantity error for '{key}': invalid "
                            f"literal for int() with base 10:'{v}'")
                    continue
            else:
                print(f"Redundant item '{key}' - discarding")
        else:
            print(f"Error - invalid parameter '{arg}'")

    print(f"Got inventory: {inventory}")
    item_list: list = list(inventory.keys())
    print(f"Item list: {item_list}")
    sum_v = sum(inventory.values())
    print(f"Total quantity of the {len(item_list)} items: {sum_v}")
    most_abundant_value: float = inventory[item_list[0]]
    most_abundant_key: str = item_list[0]
    least_abundant_value: float = inventory[item_list[0]]
    least_abundant_key: str = item_list[0]
    for item in item_list:
        percentage = (100 / sum_v)*inventory[item]
        if inventory[item] > most_abundant_value:
            most_abundant_value = inventory[item]
            most_abundant_key = item
        if inventory[item] < least_abundant_value:
            least_abundant_value = inventory[item]
            least_abundant_key = item
        print(f"Item {item} represents {percentage:.1f}%")
    print(
            f"Item most abundant: {most_abundant_key} "
            f"with quantity {most_abundant_value}")
    print(
            f"Item least abundant: {least_abundant_key} "
            f"with quantity {least_abundant_value}")
    inventory.update({"special_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
