from abc import ABC, abstractmethod
from .creature import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self, name: str) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self, name: str) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self, name: str) -> Creature:
        return Flameling(name)

    def create_evolved(self, name: str) -> Creature:
        return Pyrodon(name)


class AquaFactory(CreatureFactory):
    def create_base(self, name: str) -> Creature:
        return Aquabub(name)

    def create_evolved(self, name: str) -> Creature:
        return Torragon(name)
