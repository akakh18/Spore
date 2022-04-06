import random

from creature.creature import *


def test_initial_creature() -> None:
    animal = Creature()
    assert animal.health == 100
    assert animal.stamina == 100


def test_creature_set_position() -> None:
    animal = Creature()

    for i in range(0, 20):
        pos = random.randint(0, 100)
        animal.set_position(pos)
        assert animal.position == pos
