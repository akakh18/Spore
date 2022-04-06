from creature.creature import Creature, HighSharpnessTooth, LowSharpnessTooth
from simulation.fight import Fight


def test_strength():
    creature = Creature(teeth=HighSharpnessTooth(), claws_size=2)

    assert Fight.count_strength(animal=creature) == 20


def test_predator_beats():
    predator = Creature(teeth=HighSharpnessTooth(), claws_size=4)
    pray = Creature(teeth=LowSharpnessTooth(), claws_size=2)

    assert Fight(pray=pray, predator=predator).get_winner() == 0
