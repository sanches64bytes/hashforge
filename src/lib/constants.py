"""
All values ​​contained in the project are present and must be stored here.
"""

from lib.enums import HashsEnum
from pathlib import Path


ASSETS_DIR = Path(__file__).resolve().parent / "assets"
DEFAULT_CHUNK_SIZE = 1024
DEFAULT_HASH = HashsEnum.SHA256

