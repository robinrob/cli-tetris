import inspect
import os

PROJECT_ROOT = os.path.dirname(
    os.path.abspath(
        inspect.getfile(
            inspect.currentframe()
        )
    )
)
