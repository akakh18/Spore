import random
from dataclasses import dataclass, field
from typing import Protocol

from creature.creature import Creature
from movement.movement_types import MovementTypesList


class Logic(Protocol):
    def single_move(self, animal: Creature) -> bool:
        pass


class EconomyMove:
    def single_move(self, animal: Creature) -> bool:
        movements = MovementTypesList.get_movement_types()
        running_index = 3
        movements.pop(running_index)

        for movement in movements[::-1]:
            if movement.can_move(animal):
                movement.move(animal)
                return True

        return False


class QuickMove:
    def single_move(self, animal: Creature) -> bool:
        movements = MovementTypesList.get_movement_types()

        for movement in movements[::-1]:
            if movement.can_move(animal):
                movement.move(animal)
                return True

        return False


class RandomMove:
    def single_move(self, animal: Creature) -> bool:
        if animal.stamina <= 0:
            return False

        movements = MovementTypesList.get_movement_types()

        while True:
            index = random.randint(0, len(movements) - 1)
            movement = movements[index]

            if movement.can_move(animal):
                movement.move(animal)
                return True


@dataclass
class Movement:
    animal: Creature = field(default_factory=Creature)
    logic: Logic = field(default_factory=RandomMove)

    def move(self) -> bool:
        return self.logic.single_move(animal=self.animal)

    def change_movement_logic(self, new_logic: Logic) -> None:
        self.logic = new_logic
