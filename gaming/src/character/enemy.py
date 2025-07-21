from dataclasses import dataclass

from .character import Character


@dataclass
class EnemyCharacter(Character):
    """Concrete implementation of a character in the game."""

    def attack(self, target):
        pass

    def heal(self, amount):
        pass

    def change_health(self, amount):
        """指定された量だけキャラクターの体力を変更する。"""
        pass