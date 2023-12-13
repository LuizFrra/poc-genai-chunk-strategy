from abc import ABC, abstractmethod


class ChunckStrategy(ABC):
    @abstractmethod
    def split(self, text: str) -> list:
        pass