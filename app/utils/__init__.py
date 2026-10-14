"""Utility modules for configuration, logging, and helpers."""

from .config import initialize_config
from .logging import setup_logging

# Singleton configuration instance
g_config = initialize_config()

__all__ = [
    "g_config",
    "setup_logging",
]
