from enums import Color, Zone
from exceptions import FlyInError


class Hub:
    def __init__(self,
                 name: str,
                 x: int,
                 y: int,
                 color: Color = Color.WHITE,
                 zone: Zone = Zone.NORMAL,
                 max_drones: int = 1) -> None:
        self.__name = name
        self.__x = x
        self.__y = y
        self.__color = color
        self.__zone = zone
        self.__max_drones = max_drones
        self.__connections: list[Hub] = []
        self.__expected_load: int = 0
        self.__validate()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Hub):
            return NotImplemented
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def zone(self) -> Zone:
        return self.__zone

    @property
    def cost(self) -> int:
        return self.zone.cost

    @classmethod
    def from_str(cls, hub: str) -> Hub:
        ...

    def __validate(self) -> None:
        if self.name == "" or "-" in self.name or " " in self.name:
            raise FlyInError("Name cannot be empty or contain dashes/spaces")
        if self.__max_drones < 1:
            raise FlyInError("Max drones cannot be less than 1")
