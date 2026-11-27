from __future__ import annotations
from enum import Enum


class Zone(Enum):
    NORMAL = "normal"
    BLOCKED = "blocked"
    RESTRICTED = "restricted"
    PRIORITY = "priority"

    @property
    def cost(self) -> int:
        return _COST[self]


_COST: dict[Zone, int] = {
    Zone.NORMAL: 1,
    Zone.RESTRICTED: 2,
    Zone.PRIORITY: 1,
}
