from abc import ABC, abstractmethod
from typing import List, TextIO, Dict

class Command(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        """Возвращает название команды"""
        pass

    @abstractmethod
    def excecute(self, args: List[str], stdin: TextIO, stdout: TextIO, stderr: TextIO, params: Dict[str, str], tools ) -> int:
        """Выполняет команду с переданными аргументами"""
        pass

    @property
    def description(self) -> str:
        """Возвращает описание команды"""
        return ""