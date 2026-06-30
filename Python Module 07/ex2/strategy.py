from abc import ABC, abstractmethod
from ex0.creature import Creature


class InvalidStrategyException(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyException(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )
        return creature.attack()


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return hasattr(creature, "transform")

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyException(
                f"Invalid Creature '{creature.name}'"
                "for this aggressive strategy")
        transform = getattr(creature, "transform")()
        attack = creature.attack()
        revert = getattr(creature, "revert")()
        return f"{transform}\n{attack}\n{revert}"


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return hasattr(creature, "heal")

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyException(
                f"Invalid Creature '{creature.name}'"
                " for this defensive strategy")
        attack = creature.attack()
        heal = getattr(creature, "heal")()
        return f"{attack}\n{heal}"
