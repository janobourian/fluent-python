from abc import ABC, abstractmethod
from typing import NamedTuple, Optional
from collections.abc import Sequence

class Customer(NamedTuple):
    username: str
    current_level: int

class GameSession(NamedTuple):
    player: Customer
    strategy: Optional['GameStrategy'] = None

    def current_message(self) -> int:
        if self.strategy is None:
            message = 'No bonus'
        else:
            message = f'Bonus points: {self.strategy.bonus(self)}'
        return message

    def __repr__(self) -> str:
        return f'<GameSession current_level: {self.player.current_level} final_score: {self.current_message()}>'


class GameStrategy(ABC):
    @abstractmethod
    def bonus(self, session: GameSession) -> int:
        """Return bonus points for the given game session"""
        pass
    
class LevelUpStrategy(GameStrategy):
    def bonus(self, session: GameSession) -> int:
        if session.player.current_level >= 10:
            return '50'
        return '0'

class AchievementStrategy(GameStrategy):
    def bonus(self, session: GameSession) -> int:
        if session.player.current_level >= 100:
            return '50'
        return '0'

class HighScoreStrategy(GameStrategy):
    def bonus(self, session: GameSession) -> int:
        if session.player.current_level >= 5:
            return '50'
        return '0'

john = Customer('john_doe', 12)
session = GameSession(john, LevelUpStrategy())
print(session)
carl = Customer('carl_smith', 5)
session2 = GameSession(carl, HighScoreStrategy())
print(session2)
maria = Customer('maria_jones', 8)
session3 = GameSession(maria, AchievementStrategy())
print(session3)