import os
from typing import Generator, Any


def check_file_exists(file_path: str) -> bool:
    """
    Verify that the provided file actually exists.
    Args:
        file_path (str): The path to the file we are going to check
    Returns:
        (bool): If it exists, it returns true; otherwise, it returns false.
    """
    return os.path.exists(file_path) and os.path.isfile(file_path)


def create_file_generator(
    file_path: str,
    chunk_size: int
) -> Generator[bytes, Any, None]:
    """
    Read the complete file that was provided.
    Args:
        file_path (str): The path to the file we will read.
        chunk_size (int): Size of each piece
    Returns:
        (Generator[bytes, Any, None]): The generator returns chunks from the file.
    """
    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk


def read_file(file_path: str) -> str:
    """
    Loads the entire file content directly into memory.
    Args:
        file_path (str): The file path for the file we are going to load
    Returns:
        (str): Content of the uploaded file
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()