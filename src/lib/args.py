import sys
from typing import Any, TypedDict
from lib.errors import RequiredValueNotProvided, InvalidProvidedValueType
from lib.enums import ValuesEnum, FlagsEnum, HashsEnum
from lib.constants import DEFAULT_CHUNK_SIZE


class FlagsDict(TypedDict):
    help: bool


class ValuesDict(TypedDict):
    file: str
    hash: str
    chunk_size: int    


class ArgsDict(TypedDict):
    flags: FlagsDict
    values: ValuesDict | None


def _verify_key(key: str) -> bool:
    """
    Checks if the key was provided in the script and returns the status.
    Args:
        key (str): Key that the system will verify
    Returns:
        (bool): Whether or not it was provided
    """
    return key in sys.argv


def _get(key: str) -> str | None:
    """
    Gets the value of the provided key
    Args:
        key (str): Key from which we will get the value
    Returns:
        (str | None): Value of the key we retrieved
    """
    if not _verify_key(key):
        return None
    index = sys.argv.index(key)
    try:
        return sys.argv[index+1]
    except IndexError:
        return None


def _required(key: ValuesEnum, value: str | None) -> str:
    """
    If the user has not provided a value for the option, it throws an exception.
    Args:
        key (ValuesEnum): The option where the value is mandatory
        value (str | None): Value provides the given option.
    Returns:
        (str): The provided value
    """
    if value is not None:
        return value
    raise RequiredValueNotProvided(key)


def _default(value: str | None, default: Any) -> Any:
    """
    If the value is not provided, it returns the default value.
    Args:
        value (str | None): Valor que o usuário pode ou não ter fornecido
        default (Any): Default value that the system will return
    Returns:
        (Any): Value provided by the user or the default
    """
    return value or default


def _int(key: ValuesEnum, value: str | None) -> int | None:
    """
    Converts the received string value into an integer; if it is null, it returns null, 
    or we throw an exception if the value is invalid.
    Args:
        key (ValuesEnum): The key to the value provided
        value (str): The value we are going to convert into an integer
    Returns:
        (int | None): The value converted to an integer, or null if the value is null.
    """
    if value is None:
        return None
    if not value.isnumeric():
        raise InvalidProvidedValueType(key, value, 'inteiro')
    return int(value)

def read_args() -> ArgsDict:
    """
    Reads all arguments provided so that the system can operate.
    Returns:
        (ArgsDict): All arguments read by the system.
    """
    flags: FlagsDict = {
        'help': _verify_key(FlagsEnum.HELP)
    }
    if flags["help"]:
        return {"flags": flags, "values": None}
    values: ValuesDict = {
        'file': _required(ValuesEnum.FILE, _get(ValuesEnum.FILE)),
        'hash': _default(_get(ValuesEnum.HASH), HashsEnum.SHA256),
        'chunk_size': _default(_int(ValuesEnum.CHUNK_SIZE, _get(ValuesEnum.CHUNK_SIZE)), DEFAULT_CHUNK_SIZE)
    }
    return {
        'flags': flags,
        'values': values
    }