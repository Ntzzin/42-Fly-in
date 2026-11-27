from __future__ import annotations
from enum import Enum


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    YELLOW = "yellow"
    MAGENTA = "magenta"
    WHITE = "white"

    @property
    def ansi(self) -> str:
        return _ANSI[self]


_ANSI: dict[Color, str] = {
    Color.RED: "\033[1;91m",
    Color.GREEN: "\033[1;92m",
    Color.BLUE: "\033[1;94m",
    Color.YELLOW: "\033[1;93m",
    Color.MAGENTA: "\033[1;95m",
    Color.WHITE: "\033[1m",
}
