from dataclasses import dataclass

from world.world import World


@dataclass
class WorldLogger:
    world: World = None

    def display_beginning(self) -> str:
        world_image = "".join("_" for _ in range(101))
        lst = list(world_image)
        lst[self.world.get_pray_position() + 1] = '*'
        lst[self.world.get_predator_position() + 1] = '#'
        world_image = "".join(lst)
        return world_image[1:]

    def display_from_predator(self) -> str:
        world_image = "".join("_" for _ in range(101))
        lst = list(world_image)
        lst[self.world.get_pray_position() - self.world.get_predator_position() + 1] = '*'
        lst[1] = '#'
        world_image = "".join(lst)
        return world_image[1:]

    def display_world(self) -> str:
        world_image = "".join("_" for _ in range(350))
        lst = list(world_image)
        lst[self.world.get_pray_position() + 1] = '*'
        lst[self.world.get_predator_position() + 1] = '#'
        world_image = "".join(lst)
        return world_image[1:]
