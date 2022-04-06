from simulation.game_simulation import GameSimulation


def test_game_simulation() -> None:
    game_simulation = GameSimulation()
    game_simulation.evolve_pray()
    game_simulation.evolve_predator()
    game_simulation.start_game()
