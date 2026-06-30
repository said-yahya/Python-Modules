from .capability import HealCapability, TransformCapability
from ex0.creature import Creature
from ex0.creature_factory import CreatureFactory


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str) -> None:
        Creature.__init__(self, name, "Grass")
        HealCapability.__init__(self)

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str) -> None:
        Creature.__init__(self, name, "Grass/Fairy")
        HealCapability.__init__(self)

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


class HealingCreatureFactory(CreatureFactory):
    def create_base(self, name: str) -> Creature:
        return Sproutling(name)

    def create_evolved(self, name: str) -> Creature:
        return Bloomelle(name)


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str) -> None:
        Creature.__init__(self, name, "Normal")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self.name} returns to normal."

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str) -> None:
        Creature.__init__(self, name, "Normal/Dragon")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self.name} stabilizes its form."

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attack normally."


class TransformCreatureFactory(CreatureFactory):
    def create_base(self, name: str) -> Creature:
        return Shiftling(name)

    def create_evolved(self, name: str) -> Creature:
        return Morphagon(name)
