import random
from dataclasses import field, dataclass
from typing import Protocol

from creature.creature import Creature


class PredatorInterface(Protocol):
    predator: Creature

    def put_predator(self) -> None:
        return

    def get_predator_position(self) -> int:
        pass

    def get_predator_stamina(self) -> int:
        pass


class PrayInterface(Protocol):
    pray: Creature

    def put_pray(self) -> None:
        pass

    def get_pray_position(self) -> int:
        pass

    def get_pray_stamina(self) -> int:
        pass


@dataclass
class World:
    pray: Creature = field(default_factory=Creature)
    predator: Creature = field(default_factory=Creature)

    # 🤔 does it work?
    def put_pray(self) -> None:
        self.pray.set_position(random.randint(55, 100))

    def put_predator(self) -> None:
        self.predator.set_position(random.randint(0, 45))

    def get_pray_position(self) -> int:
        return self.pray.position

    def get_predator_position(self) -> int:
        return self.predator.position

    def get_pray_stamina(self) -> int:
        return self.pray.stamina

    def get_predator_stamina(self) -> int:
        return self.predator.stamina


@dataclass
class Predator:
    predator: PredatorInterface

    def put_predator(self) -> None:
        self.predator.put_predator()

    def get_predator_position(self) -> int:
        return self.predator.get_predator_position()

    def get_predator_stamina(self) -> int:
        return self.predator.get_predator_stamina()


@dataclass
class Pray:
    pray: PrayInterface

    def put_pray(self) -> None:
        self.pray.put_pray()

    def get_pray_position(self) -> int:
        return self.pray.get_pray_position()

    def get_pray_stamina(self) -> int:
        return self.pray.get_pray_stamina()
