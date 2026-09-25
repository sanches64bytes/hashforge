from lib.enums import ExitCodesEnum
from lib.texts import (
    ERROR_MESSAGE_DEFAULT,
    ERROR_MESSAGE_PROVIDED_HASH_IS_INVALID,
    ERROR_MESSAGE_REQUIRED_VALUE_NOT_PROVIDED,
    ERROR_MESSAGE_INVALID_PROVIDED_VALUE_TYPE,
    ERROR_MESSAGE_PROVIDED_FILE_DOES_NOT_EXIST
)


class ScriptError(Exception):
    """
    All system errors inherit this single exception.
    """

    default_exit_code: ExitCodesEnum = ExitCodesEnum.GENERIC_ERROR
    default_message = ERROR_MESSAGE_DEFAULT

    def __init__(
        self,
        exit_code: ExitCodesEnum | None = None,
        message: str | None = None
    ):
        super().__init__(message)

        self.message = self.default_message if message is None else message
        self.exit_code = self.default_exit_code if exit_code is None else exit_code


class ProvidedHashIsInvalid(ScriptError):
    """The hash provided by the user is invalid."""
    
    def __init__(self, provided_hash: str):
        super().__init__(ExitCodesEnum.INVALID_HASH, ERROR_MESSAGE_PROVIDED_HASH_IS_INVALID % provided_hash)


class RequiredValueNotProvided(ScriptError):
    """A required value for the script to function was not provided."""

    def __init__(self, key: str):
        super().__init__(
            ExitCodesEnum.INVALID_ARGUMENT,
            ERROR_MESSAGE_REQUIRED_VALUE_NOT_PROVIDED % key
        )


class InvalidProvidedValueType(ScriptError):
    """The type of the provided value is invalid."""

    def __init__(self, key: str, value: str, expected_type: str):
        super().__init__(
            ExitCodesEnum.INVALID_VALUE,
            (
                ERROR_MESSAGE_INVALID_PROVIDED_VALUE_TYPE % {
                    'key': key,
                    'value': value,
                    'expected_type': expected_type
                }
            )
        )


class ProvidedFileDoesNotExist(ScriptError):
    """The provided file was not found."""

    def __init__(self, file_path: str):
        super().__init__(ExitCodesEnum.FILE_NOT_FOUND, ERROR_MESSAGE_PROVIDED_FILE_DOES_NOT_EXIST % file_path)