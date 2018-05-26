#!/usr/bin/env python3

"""Executable script to run CLI Tetris."""

from src.tetris import Tetris
from src.console_interface import ConsoleInterface


if __name__ == '__main__':
    Tetris(ConsoleInterface()).play()