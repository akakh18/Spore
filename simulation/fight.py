from dataclasses import field, dataclass

from creature.creature import Creature


@dataclass
class Fight:
    pray: Creature = field(default_factory=Creature)
    predator: Creature = field(default_factory=Creature)

    """counts creature strength considering their"""

    @staticmethod
    def count_strength(animal: Creature) -> int:
        return (animal.power + animal.teeth.get_power()) * animal.claws_size

    """this method returns 1, if pray beats predator, 0 otherwise"""

    def get_winner(self) -> int:
        return int(self.count_strength(self.pray) > self.count_strength(self.predator))

    def get_pray_power_log(self) -> str:
        return "Pray power: " + str(self.count_strength(self.pray))

    def get_predator_power_log(self) -> str:
        return "Predator power: " + str(self.count_strength(self.predator))
