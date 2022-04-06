from dataclasses import dataclass
from typing import List

from creature.creature import Creature


@dataclass()
class MovementType:
    required_stamina: int
    required_legs_num: int
    required_wings_num: int
    used_stamina: int
    speed: int

    """returns if current animal can move with this specific movement"""

    def can_move(self, animal: Creature) -> bool:
        return animal.num_legs >= self.required_legs_num and animal.num_wings >= self.required_wings_num \
               and animal.stamina > self.required_stamina

    "moves one step forward"

    def move(self, animal: Creature) -> None:
        animal.position += self.speed
        animal.stamina -= self.used_stamina


class MovementTypesList:
    """returns list of all movement types"""

    @staticmethod
    def get_movement_types() -> List[MovementType]:
        crawling = MovementType(required_stamina=0, required_legs_num=0, required_wings_num=0, used_stamina=1, speed=1)
        hopping = MovementType(required_stamina=20, required_legs_num=1, required_wings_num=0, used_stamina=2, speed=3)
        walking = MovementType(required_stamina=40, required_legs_num=2, required_wings_num=0, used_stamina=2, speed=4)
        running = MovementType(required_stamina=60, required_legs_num=2, required_wings_num=0, used_stamina=4, speed=6)
        flying = MovementType(required_stamina=80, required_legs_num=0, required_wings_num=2, used_stamina=4, speed=8)
        return [crawling, hopping, walking, running, flying]
