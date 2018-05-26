"""Classes: ElementType."""

from enum import Enum


class ElementType(Enum):
    """Enumerates possible types for Element instances."""

    WALL = 1
    PIECE = 2