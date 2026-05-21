from elements import create_fire as c_fire
import alchemy.potions as p
from ..elements import create_air as c_air


def lead_to_gold() -> str:
    output: str = (f"Recipe transmuting Lead to Gold: brew '{c_air()}'"
                   f"and '{p.strength_potion()}' mixed with '{c_fire()}'")
    return (output)
