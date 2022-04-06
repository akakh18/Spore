from dataclasses import field, dataclass

from logger.world_logger import WorldLogger
from movement.movement import Movement, RandomMove
from world.world import World, Pray, Predator


@dataclass
class Chase:
    world: World = field(default_factory=World)

    pray_movement: Movement = field(default_factory=RandomMove)
    predator_movement: Movement = field(default_factory=RandomMove)

    def start_chasing(self) -> None:
        world_logger = WorldLogger(self.world)

        pray = Pray(self.world)
        predator = Predator(self.world)

        print("\n")

        while predator.get_predator_stamina() > 0 and predator.get_predator_position() < pray.get_pray_position():
            self.predator_movement.move()
            self.pray_movement.move()
            print(world_logger.display_world())

    """this method returns 1 if predator catches pray, 0 otherwise"""

    def predator_catch(self) -> int:
        pray = Pray(self.world)
        predator = Predator(self.world)

        return int(pray.get_pray_position() <= predator.get_predator_position())
