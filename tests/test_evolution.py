from creature.creature import Creature
from simulation.evolution import Evolution, ClawsGenerousEvolution, ClawsRandomEvolution, SameKindTeethEvolution, \
    DifferentTeethEvolution


def test_evolution_legs() -> None:
    animal = Creature()
    evolution = Evolution(animal=animal)
    assert animal.num_legs == 0
    evolution.evolve_legs()
    assert animal.num_legs > 0


def test_evolution_wings() -> None:
    animal = Creature()
    evolution = Evolution(animal=animal)
    assert animal.num_wings == 0
    evolution.evolve_wings()
    assert animal.num_wings > 0


def test_random_evolution_claws() -> None:
    animal = Creature()
    evolution = Evolution(animal=animal, claws_evolution=ClawsRandomEvolution())
    assert animal.claws_size == 0
    evolution.evolve_claws()
    assert animal.claws_size > 0


def test_generous_claws_evolution() -> None:
    animal = Creature()
    evolution = Evolution(animal=animal, claws_evolution=ClawsGenerousEvolution())
    assert animal.claws_size == 0
    evolution.evolve_claws()
    assert animal.claws_size == 4


def test_same_kind_teeth_evolution() -> None:
    animal = Creature()
    evolution = Evolution(animal=animal, teeth_evolution=SameKindTeethEvolution())
    evolution.evolve_teeth()
    teeth = animal.teeth
    assert teeth.get_power() > 0


def test_different_teeth_evolution() -> None:
    animal = Creature()
    evolution = Evolution(animal=animal, teeth_evolution=DifferentTeethEvolution())
    evolution.evolve_teeth()
    teeth = animal.teeth
    assert teeth.get_power() > 0
