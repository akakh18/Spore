import random

from creature.creature import Creature
from movement.movement import Movement, RandomMove, EconomyMove, QuickMove


def single_random_movement_check() -> None:
    animal = Creature(position=random.randint(10, 25), num_legs=random.randint(0, 3), num_wings=random.randint(0, 4))
    movement = Movement(animal=animal, logic=RandomMove())
    pos_before = animal.position
    stamina_before = animal.stamina

    for _ in range(4):
        movement.move()
        assert animal.position > pos_before and animal.stamina < stamina_before
        pos_before, stamina_before = (animal.position, animal.stamina)


def test_random_movement():
    for i in range(10):
        single_random_movement_check()


def test_random_can_only_crawl() -> None:
    snail = Creature(position=1, num_wings=0, num_legs=0, stamina=10)
    movement = Movement(animal=snail, logic=RandomMove())
    prev = 1
    for _ in range(5):
        res = movement.move()
        assert res and snail.position - prev == 1
        prev = snail.position


def test_economy_animal_should_fly() -> None:
    economy_animal = Creature(position=1, num_wings=4, num_legs=6, stamina=100)
    movement = Movement(animal=economy_animal, logic=EconomyMove())
    pos_before = 1
    stamina_before = 100

    for _ in range(5):
        movement.move()
        pos_after = economy_animal.position
        stamina_after = economy_animal.stamina
        assert pos_after - pos_before == 8 and stamina_before - stamina_after == 4
        pos_before = pos_after
        stamina_before = stamina_after


def test_economy_animal_should_not_run() -> None:
    economy_animal = Creature(position=1, num_wings=0, num_legs=6, stamina=80)
    movement = Movement(animal=economy_animal, logic=EconomyMove())
    pos_before = 1
    stamina_before = 80

    for _ in range(5):
        movement.move()
        pos_after = economy_animal.position
        stamina_after = economy_animal.stamina
        assert pos_after - pos_before == 4 and stamina_before - stamina_after == 2
        pos_before = pos_after
        stamina_before = stamina_after


def test_economy_animal_should_walk():
    economy_animal = Creature(position=1, num_wings=0, num_legs=6, stamina=60)
    movement = Movement(animal=economy_animal, logic=EconomyMove())
    pos_before = 1
    stamina_before = 60

    for _ in range(5):
        movement.move()
        pos_after = economy_animal.position
        stamina_after = economy_animal.stamina
        assert pos_after - pos_before == 4 and stamina_before - stamina_after == 2
        pos_before = pos_after
        stamina_before = stamina_after


def test_economy_animal_should_crawl():
    economy_animal = Creature(position=1, num_wings=0, num_legs=0, stamina=10)
    movement = Movement(animal=economy_animal, logic=EconomyMove())
    pos_before = 1
    stamina_before = 10

    for _ in range(5):
        movement.move()
        pos_after = economy_animal.position
        stamina_after = economy_animal.stamina
        assert pos_after - pos_before == 1 and stamina_before - stamina_after == 1
        pos_before = pos_after
        stamina_before = stamina_after


def test_predator_should_fly():
    flying_animal = Creature(position=0, num_wings=2, num_legs=0, stamina=90)
    movement = Movement(animal=flying_animal, logic=QuickMove())
    movement.move()
    assert flying_animal.position == 8 and flying_animal.stamina == 86
