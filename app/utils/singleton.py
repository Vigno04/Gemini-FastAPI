"""Thread-safe singleton metaclass implementation."""

from typing import ClassVar


class Singleton(type):
    """Metaclass that creates a singleton instance of a class."""

    _instances: ClassVar[dict[type, object]] = {}

    def __call__(cls, *args, **kwargs):
        """Return the singleton instance of the class, creating it if needed."""
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
