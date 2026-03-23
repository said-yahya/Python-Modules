def recursion(day: int):
    if day == 1:
        print("Day 1")
    elif day > 1:
        recursion(day - 1)
        print(f"Day {day}")


def ft_count_harvest_recursive():
    day = int(input("Days until harvest: "))
    recursion(day)
    print("Harvest time!")
