import hashlib
from typing import Generator, Any
from lib.enums import HashsEnum
from lib.errors import ProvidedHashIsInvalid


def get_buffer_hash(hash_type: HashsEnum) -> hashlib._Hash:
    """
    Returns the buffer corresponding to the hash type the user wants to calculate.
    Args:
        hash_type (str): The type of hash we will calculate
    Returns:
        (hashlib._Hash): Buffer built.
    """
    match hash_type:
        case HashsEnum.MD5:
            return hashlib.md5()
        case HashsEnum.SHA1:
            return hashlib.sha1()
        case HashsEnum.SHA256:
            return hashlib.sha256()
        case HashsEnum.SHA512:
            return hashlib.sha512()
        case HashsEnum.SHA3_256:
            return hashlib.sha3_256()
        case HashsEnum.SHA3_512:
            return hashlib.sha3_256()
        case HashsEnum.BLAKE2B:
            return hashlib.blake2b()
        case HashsEnum.BLAKE2S:
            return hashlib.blake2s()
    raise ProvidedHashIsInvalid(hash_type)


def calculate_hash(file_generator: Generator[bytes, Any, None], hash_type: HashsEnum) -> str:
    """
    It receives the file generator to read the file in chunks,
    processes the file byte by byte until completion,
    and calculates the file's hash.
    Args:
        file_generator (Generator[bytes, Any, None]): The file generator to read the file in parts;
        hash_type (str): Type of hash to be calculated
    Returns:
        (str): Hash of the file that was generated with the file.
    """
    buffer = get_buffer_hash(hash_type)
    for chunk in file_generator:
        buffer.update(chunk)
    return buffer.hexdigest()
