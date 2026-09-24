from enum import StrEnum, IntEnum


class HashsEnum(StrEnum):
    """
    Hashes the system accepts for converting the file.
    """
    SHA1 = 'sha1'
    SHA256 = 'sha256'
    SHA512 = 'sha512'
    SHA3_256 = 'sha3_256'
    SHA3_512 = 'sha3_512'
    BLAKE2B = 'blake2b'
    BLAKE2S = 'blake2s'
    MD5 = 'md5'


class FlagsEnum(StrEnum):
    """
    We declare here all the option flags that can be passed to the script.
    """
    HELP = '--help'


class ValuesEnum(StrEnum):
    """
    The value options that can be passed to the script are declared here.
    """
    FILE = '--file'
    HASH = '--hash'
    CHUNK_SIZE = '--chunk_size'


class ExitCodesEnum(IntEnum):
    """
    All the script termination codes are here.
    """
    SUCCESS = 0
    GENERIC_ERROR = 1
    INVALID_ARGUMENT = 2
    FILE_NOT_FOUND = 3
    INVALID_HASH = 4
    INVALID_VALUE = 5
    COMMNAD_CANNOT_EXECUTED = 126
    COMMAND_NOT_FOUND = 127
    CLOSING_SIGNAL = 128
