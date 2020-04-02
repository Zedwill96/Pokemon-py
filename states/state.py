from enum import IntEnum
from typing import List, Type, TypeVar

from readchar import readkey

from config.config import TEXT

T = TypeVar("T")


class StateOptions(IntEnum):
    """Gives Menu Option values"""

    def __repr__(self) -> str:
        return f"{self.value} - {self.name}"

    @classmethod
    def list_options(cls: Type[T]) -> List[str]:
        return [repr(option) for option in cls]


class State:
    """Function for main state and error catcher"""

    @staticmethod
    def check_input(option_type: Type[T]) -> T:
        print(*option_type.list_options(), sep="\n")
        print(TEXT["MISC"]["PROMPT"])
        try:
            choice = readkey()
            print(choice)
            return option_type(int(choice))
        except ValueError:
            print(TEXT["MISC"]["ERROR"])
