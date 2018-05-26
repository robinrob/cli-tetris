"""Classes: ElementConflictException, ElementOutOfBoundsException, InvalidMoveException, GameOverException."""


class ElementConflictException(Exception):
    """Element position is in conflict with another element."""

    pass


class ElementOutOfBoundsException(Exception):
    """Element position is out of bounds."""

    pass


class InvalidMoveException(Exception):
    """Player move is invalid."""

    pass


class GameOverException(Exception):
    """Game over mate."""

    pass