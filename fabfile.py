"""Fabfile for CLI Tetris."""

import subprocess

from fabric.decorators import task


@task
def lint(message="Auto-update."):
    """Lint source code in project."""
    subprocess.call("flake8", shell=True)
