#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._height: float = 0.0
        self._age: int = 0
        if height >= 0:
            self._height = height
        if age >= 0:
            self._age = age
        print(
                f"Plant created: {self.name}: "
                f"{self._height:.1f}cm, {self._age} days old\n"
            )

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"\n{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            if self._height != height:
                print(f"Height updated: {height:.1f}cm")
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"\n{self.name}: Error, age can't be negative")
            print("Age update rejected")
        elif self._age > age:
            print(f"{self.name}: Error, age can't decrease")
            print("Age update rejected")
        else:
            if self._age != age:
                print(f"Age updated: {age}")
            self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(
                f"{self.name}: {self.get_height():.1f}cm, "
                f"{self.get_age()} days old"
            )


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)

    rose.set_height(25.0)
    rose.set_age(30)

    rose.set_height(-5.0)
    rose.set_age(-1)

    print(
            f"\nCurrent state: {rose.name}: {rose.get_height():.1f}cm, "
            f"{rose.get_age()} days old"
        )


if __name__ == "__main__":
    main()
