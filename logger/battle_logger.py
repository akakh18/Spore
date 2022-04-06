from dataclasses import dataclass, field

from logger import message_constants
from simulation.fight import Fight


@dataclass
class FightLogger:
    fight: Fight = field(default_factory=Fight)

    @property
    def messages(self) -> list[str]:
        return [message_constants.PREDATOR_WON_MESSAGE, message_constants.PRAY_WON_MESSAGE]

    def get_fight_result(self):
        return self.messages[self.fight.get_winner()]
