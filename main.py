from simulation.game_simulation import GameSimulation


def simulate():
    for i in range(0, 100):
        game_simulation = GameSimulation()
        game_simulation.evolve_pray()
        game_simulation.evolve_predator()
        game_simulation.start_game()


if __name__ == "__main__":
    simulate()
