import random
from typing import Protocol
from dataclasses import dataclass, field

from creature.creature import Creature, ToothFactory, Teeth

MIN_TEETH_NUM = 10
MAX_TEETH_NUM = 50

MIN_TOOTH_INDEX = 0
MAX_TOOTH_INDEX = 2

MIN_LEGS_NUM = 0
MAX_LEGS_NUM = 8

MIN_WINGS_NUM = 0
MAX_WINGS_NUM = 6

MIN_CLAWS_SIZE = 2
MAX_CLAWS_SIZE = 4


class ClawsEvolution(Protocol):
    def evolve_claws(self, animal: Creature) -> None:
        pass


class ClawsRandomEvolution:
    def evolve_claws(self, animal: Creature) -> None:
        animal.claws_size = random.randint(MIN_CLAWS_SIZE, MAX_CLAWS_SIZE)


class ClawsGenerousEvolution:
    def evolve_claws(self, animal: Creature) -> None:
        animal.claws_size = MAX_CLAWS_SIZE


class TeethEvolution(Protocol):
    def evolve_teeth(self, animal: Creature) -> None:
        pass


class SameKindTeethEvolution:
    def evolve_teeth(self, animal: Creature) -> None:
        teeth = []
        num_teeth = random.randint(MIN_TEETH_NUM, MAX_TEETH_NUM)
        tooth_index = random.randint(MIN_TOOTH_INDEX, MAX_TOOTH_INDEX)
        for _ in range(num_teeth):
            categories = ToothFactory.get_categories()
            teeth.append(categories[tooth_index])

        animal.teeth = Teeth(teeth)


class DifferentTeethEvolution:
    def evolve_teeth(self, animal: Creature) -> None:
        teeth = []
        num_teeth = random.randint(MIN_TEETH_NUM, MAX_TEETH_NUM)
        for _ in range(num_teeth):
            tooth_index = random.randint(MIN_TOOTH_INDEX, MAX_TOOTH_INDEX)
            categories = ToothFactory.get_categories()
            teeth.append(categories[tooth_index])

        animal.teeth = Teeth(teeth)


@dataclass
class Evolution:
    animal: Creature = field(default_factory=Creature)
    claws_evolution: ClawsEvolution = field(default_factory=ClawsRandomEvolution)
    teeth_evolution: TeethEvolution = field(default_factory=DifferentTeethEvolution)

    def evolve_claws(self) -> None:
        self.claws_evolution.evolve_claws(self.animal)

    def evolve_teeth(self) -> None:
        self.teeth_evolution.evolve_teeth(self.animal)

    def evolve_legs(self) -> None:
        self.animal.num_legs = random.randint(MIN_LEGS_NUM, MAX_LEGS_NUM)

    def evolve_wings(self) -> None:
        self.animal.num_wings = random.randint(MIN_WINGS_NUM, MAX_WINGS_NUM)
