from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Configuration:
    nb_drones: int
    start_hub: str
    end_hub: str
    hubs: list[tuple[str, int, int, Optional[dict]]]
    connections: list[tuple[str, str, Optional[dict]]]


