from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Character(ABC):
    """ゲーム内のすべてのキャラクターの抽象基底クラス。"""
    name: str = ""
    health: int = None
    mp : int = None
    attack_point:int = None
    
    @abstractmethod
    def attack(self, target):
        """対象キャラクターに攻撃を行う。"""
        pass

    @abstractmethod
    def heal(self, amount):
        """指定された量だけキャラクターを回復させる。"""
        pass

    @abstractmethod
    def change_health(self, amount):
        """指定された量だけキャラクターの体力を変更する。"""
        pass