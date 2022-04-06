import random

from creature.creature import Creature
from movement.movement import Movement, QuickMove, RandomMove, EconomyMove
from simulation.chase import Chase
from world.world import World

PRAY_STARTING = 10
PREDATOR_STARTING = 5


def test_chasing_starting() -> None:
    pray = Creature(position=PRAY_STARTING, num_legs=random.randint(0, 10), num_wings=random.randint(0, 8))
    predator = Creature(position=PREDATOR_STARTING, num_legs=random.randint(0, 10), num_wings=random.randint(0, 8))

    world = World(pray=pray, predator=predator)

    pray_movement = Movement(animal=pray, logic=EconomyMove())
    predator_movement = Movement(animal=predator, logic=EconomyMove())

    chasing = Chase(world=world, pray_movement=pray_movement, predator_movement=predator_movement)

    chasing.start_chasing()

    assert pray.position > PRAY_STARTING and predator.position > PREDATOR_STARTING


def test_predator_cant_catch() -> None:
    pray = Creature(position=PRAY_STARTING, num_legs=4, num_wings=2)
    predator = Creature(position=PREDATOR_STARTING, num_legs=1, num_wings=2)

    world = World(pray=pray, predator=predator)

    pray_movement = Movement(animal=pray, logic=QuickMove())
    predator_movement = Movement(animal=predator, logic=EconomyMove())

    chasing = Chase(world=world, pray_movement=pray_movement, predator_movement=predator_movement)

    chasing.start_chasing()

    assert chasing.predator_catch() == 0


def test_predator_must_catch() -> None:
    for _ in range(400):
        pray = Creature(position=PRAY_STARTING, num_legs=1, num_wings=0)
        predator = Creature(position=PREDATOR_STARTING, num_legs=6, num_wings=2)

        world = World(pray=pray, predator=predator)

        pray_movement = Movement(animal=pray, logic=RandomMove())
        predator_movement = Movement(animal=predator, logic=QuickMove())

        chasing = Chase(world=world, pray_movement=pray_movement, predator_movement=predator_movement)

        chasing.start_chasing()

        assert chasing.predator_catch() == 1
