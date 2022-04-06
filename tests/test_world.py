from creature.creature import Creature
from logger.world_logger import WorldLogger
from world.world import Pray, Predator, World


def test_initial_world() -> None:
    world_logger = WorldLogger(World(Creature(), Creature()))
    assert world_logger.display_beginning() == "".join('_' for _ in range(100))


def test_pray_inits_once() -> None:
    world = World(pray=Creature(), predator=Creature())
    positions = []
    for i in range(0, 10):
        world.put_pray()
        positions.append(world.get_pray_position())
        if i == 0:
            continue
        assert positions[i] == positions[i - 1] and positions[i] != -1


def test_predator_exists() -> None:
    world = World(Creature(), Creature())
    world.put_predator()
    world_logger = WorldLogger(world)
    world_image = world_logger.display_beginning()
    count = 0

    print("\n World Image:\n", world_image)
    print("predator position:", world.get_predator_position())

    for c in list(world_image):
        if c == '#':
            count += 1
        assert count <= 1

    assert count == 1


def test_pray_exists() -> None:
    world = World(Creature(), Creature())
    world.put_pray()
    world_logger = WorldLogger(world)
    world_image = world_logger.display_beginning()
    count = 0

    print("\n World Image:\n", world_image)
    print("predator position:", world.get_predator_position())

    for c in list(world_image):
        if c == '*':
            count += 1
        assert count <= 1

    assert count == 1


def test_pray_is_in_front() -> None:
    for i in range(0, 10):
        pray_first = World(Creature(), Creature())
        pray_first.put_pray()
        pray_first.put_predator()
        assert pray_first.get_pray_position() > pray_first.get_predator_position()

        predator_first = World(Creature(), Creature())
        predator_first.put_predator()
        predator_first.put_pray()
        assert predator_first.get_pray_position() > predator_first.get_predator_position()


def test_predator_init() -> None:
    world = World(Creature(), Creature())
    predator = Predator(world)
    predator.put_predator()
    assert world.get_predator_position() > -1


def test_pray_init() -> None:
    world = World(Creature(), Creature())
    pray = Pray(world)
    pray.put_pray()
    assert world.get_predator_position() > -1
