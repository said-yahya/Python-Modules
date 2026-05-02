import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        inpt = input("Enter new coordinates as floats in format 'x,y,z': ")
        coordinates = (inpt.replace(" ", "")).split(",")
        if len(coordinates) != 3:
            print("Invalid syntax")
            continue
        try:
            current_part = ""
            converted = []
            for part in coordinates:
                current_part = part
                converted.append(float(part))
            return (converted[0], converted[1], converted[2])
        except ValueError as e:
            error = str(e).split(":")[-1].strip()
            print(
                    f"Error on parameter '{error}': could not "
                    f"convert string to float: {current_part}"
                )
            continue


def program() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    x1, y1, z1 = get_player_pos()
    print(f"Got a first tuple: ({x1}, {y1}, {z1})")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    print(f"Distance to center: {(math.sqrt(x1**2 + y1**2 + z1**2)):.4f}\n")

    print("Get a second set of coordinates")
    x2, y2, z2 = get_player_pos()
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Distance between the 2 sets of coordinates: {distance:.4f}")


if __name__ == "__main__":
    program()
