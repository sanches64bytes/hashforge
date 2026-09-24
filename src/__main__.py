import sys, signal, types
from lib.errors import ScriptError, ProvidedFileDoesNotExist
from lib.texts import HELP_DOCUMENT, CALCULATED_FILE_HASH, WARNING_MESSAGE_SIGNAL_CLOSING_SIGNAL, SYMBOL_ASCII
from lib.args import read_args, ArgsDict
from lib.enums import ExitCodesEnum
from lib.file import create_file_generator, check_file_exists
from lib.hash import calculate_hash


def handle_shutdown(signum: int, frame: types.FrameType):
    """
    Function called when the operating system requests
    that the script be terminated.
    Args:
        signum (int): The value of the signal sent by the operating system
        frame (types.FrameType): Execution script context when the signal was sent
    """
    sys.stdout.write(WARNING_MESSAGE_SIGNAL_CLOSING_SIGNAL % signum)
    sys.exit(ExitCodesEnum.CLOSING_SIGNAL)
    

def show_symbol_ascii():
    """
    It shows the ARARA symbol, a mark I like to use in my projects.
    """
    sys.stdout.write(SYMBOL_ASCII)


def show_help_documentation(args: ArgsDict):
    """
    If the documentation flag has been provided, it displays the documentation.
    Args:
        args (ArgsDict): All arguments provided by the user
    """
    if not args["flags"]["help"]:
        return
    sys.stdout.write(HELP_DOCUMENT)
    sys.exit(ExitCodesEnum.SUCCESS)


def read_file_and_calculate_hash(args: ArgsDict):
    """
    Read the file and calculate the hash.
    Args:
        args (ArgsDict): Arguments required to read the file
    """
    if args["values"] is None:
        return
    file_path = args["values"]["file"]
    chunk_size = args["values"]["chunk_size"]
    hash_type = args["values"]["hash"]
    if not check_file_exists(file_path):
        raise ProvidedFileDoesNotExist(file_path)
    show_symbol_ascii()
    file_generator = create_file_generator(file_path, chunk_size)
    hash_file = calculate_hash(file_generator, hash_type)
    sys.stdout.write(CALCULATED_FILE_HASH % {
        'hash_type': hash_type,
        'hash_file': hash_file
    })
    sys.exit(ExitCodesEnum.SUCCESS)


def main():
    """
    This function starts the script and all the processes.
    """
    try:
        args = read_args()
        show_help_documentation(args)
        read_file_and_calculate_hash(args)
    except ScriptError as exc:
        sys.stdout.write(exc.message)
        sys.exit(exc.exit_code)


# Defining the function that will be called when the operating system sends a
# termination signal.
signal.signal(signal.SIGINT, handle_shutdown)
signal.signal(signal.SIGTERM, handle_shutdown)
if __name__ == "__main__":
    main()