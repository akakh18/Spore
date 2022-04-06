from dataclasses import dataclass, field
from typing import Protocol, List


class Tooth(Protocol):
    def get_power(self) -> int:
        pass


@dataclass
class LowSharpnessTooth:
    POWER: int = 3

    def get_power(self) -> int:
        return self.POWER


class MediumSharpnessTooth:
    POWER: int = 6

    def get_power(self) -> int:
        return self.POWER


class HighSharpnessTooth:
    POWER: int = 9

    def get_power(self) -> int:
        return self.POWER


@dataclass
class Teeth:
    teeth: List[Tooth] = field(default_factory=list)

    def get_power(self) -> int:
        return sum(tooth.get_power() for tooth in self.teeth)


class ToothFactory:
    @staticmethod
    def get_categories() -> List[Tooth]:
        return [LowSharpnessTooth(), MediumSharpnessTooth(), LowSharpnessTooth()]


@dataclass
class Creature:
    position: int = -1
    power: int = 1
    health: int = 100
    stamina: int = 100
    num_legs: int = 0
    num_wings: int = 0
    claws_size: int = 0
    teeth: Tooth = field(default_factory=Teeth)

    def set_position(self, index: int) -> None:
        self.position = index
