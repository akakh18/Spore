import random

from creature.creature import Creature
from logger import message_constants
from logger.battle_logger import FightLogger
from logger.world_logger import WorldLogger
from movement.movement import EconomyMove, RandomMove, QuickMove, Movement
from simulation.chase import Chase
from simulation.evolution import Evolution, ClawsRandomEvolution, ClawsGenerousEvolution, SameKindTeethEvolution, \
    DifferentTeethEvolution
from simulation.fight import Fight
from world.world import World, Pray, Predator


def evolve(evolution: Evolution) -> None:
    evolution.evolve_teeth()
    evolution.evolve_claws()
    evolution.evolve_legs()
    evolution.evolve_wings()


class GameSimulation:
    def __init__(self) -> None:
        self.pray = Creature()
        self.predator = Creature()

        self.world = World(pray=self.pray, predator=self.predator)

        self.pray_world = Pray(self.world)
        self.predator_world = Predator(self.world)

        self.pray_world.put_pray()
        self.predator_world.put_predator()

        if self.pray_world.get_pray_position() - self.predator_world.get_predator_position() < 15:
            pray_movement_logic = [RandomMove(), EconomyMove()][random.randint(0, 1)]
        else:
            pray_movement_logic = QuickMove()

        self.pray_movement = Movement(animal=self.pray, logic=pray_movement_logic)
        self.predator_movement = Movement(animal=self.predator, logic=QuickMove())

        self.chasing = Chase(self.world, pray_movement=self.pray_movement, predator_movement=self.predator_movement)

        self.pray_claws_evolution = ClawsRandomEvolution()
        self.predator_claws_evolution = ClawsGenerousEvolution()

        self.pray_teeth_evolution = SameKindTeethEvolution()
        self.predator_teeth_evolution = DifferentTeethEvolution()

    def evolve_pray(self) -> None:
        pray_evolution = Evolution(claws_evolution=self.pray_claws_evolution,
                                   teeth_evolution=self.pray_teeth_evolution,
                                   animal=self.pray)
        evolve(pray_evolution)

    def evolve_predator(self) -> None:
        predator_evolution = Evolution(claws_evolution=self.predator_claws_evolution,
                                       teeth_evolution=self.predator_teeth_evolution,
                                       animal=self.predator)
        evolve(predator_evolution)

    def start_game(self) -> None:
        world_logger = WorldLogger(world=self.world)
        world_logger.display_world()
        self.chasing.start_chasing()

        if self.chasing.predator_catch() == 0:
            print("Predator couldn't catch\n", message_constants.PRAY_WON_MESSAGE)
        else:
            print("Predator caught pray")
            fight = Fight(pray=self.pray, predator=self.predator)
            print(fight.get_pray_power_log())
            print(fight.get_predator_power_log())
            print(FightLogger(fight).get_fight_result())
