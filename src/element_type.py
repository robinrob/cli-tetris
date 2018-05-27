"""Classes: ElementType."""

from enum import Enum


class ElementType(Enum):
    """Enumerates possible types for Element instances."""

    NONE = 0
    WALL = 1
    PIECE = 2