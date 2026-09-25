"""
All the texts the project uses to interact with the user are here and must be stored here.
"""

from lib.constants import DEFAULT_CHUNK_SIZE, ASSETS_DIR
from lib.file import read_file


COLORS = {
    "R": "\033[91m",
    "Y": "\033[93m",
    "B": "\033[94m",
    "C": "\033[96m",
    "G": "\033[92m",
    "W": "\033[97m",
    "K": "\033[90m",
    ".": "\033[0m",
}


def apply_colors(value: str) -> str:
    """
    Apply colors to the text you have from a file.
    Args:
        value (str): Text without colors applied
    Returns:
        (str): Text with colors applied
    """
    for key, color in COLORS.items():
        value = value.replace(key, color)
    return value + COLORS["."]


SYMBOL_ASCII = apply_colors(read_file(ASSETS_DIR / "symbol_ascii.txt")+'\n')
HELP_DOCUMENT = """
Uso:
python main.py [OPÇÕES]

Opções:
--help               Exibe esta mensagem de ajuda.
--file [CAMINHO]     Caminho do arquivo cujo hash será calculado.
--hash [ALGORITMO]   Algoritmo de hash utilizado. O padrão é SHA-256.
--chunk_size [VALOR] Define o tamanho dos blocos (chunks) usados na leitura do arquivo. O valor padrão é %(default_chunk_size)s bytes.

Exemplo:
python main.py --file arquivo.txt --hash sha256
""" % {'default_chunk_size': DEFAULT_CHUNK_SIZE}
FILE_PATH_NOT_PROVIDED = (
    f"{COLORS['R']}O caminho do arquivo não foi informado.{COLORS['.']} "
    f"Use {COLORS['C']}--file [CAMINHO]{COLORS['.']}."
)
FILE_DOES_NOT_EXIST = (
    f"{COLORS['R']}O arquivo informado não existe.{COLORS['.']}"
)
CALCULATED_FILE_HASH = (
    f"{COLORS['G']}Hash %(hash_type)s do arquivo calculado com sucesso:"
    f"{COLORS['.']} {COLORS['W']}%(hash_file)s{COLORS['.']}"
)
ERROR_MESSAGE_DEFAULT = (
    f"{COLORS['R']}Ocorreu um erro inesperado durante a execução."
    f"{COLORS['.']}"
)
ERROR_MESSAGE_PROVIDED_HASH_IS_INVALID = (
    f"{COLORS['R']}O algoritmo de hash informado é inválido:"
    f"{COLORS['.']} {COLORS['W']}%s{COLORS['.']}"
)
ERROR_MESSAGE_REQUIRED_VALUE_NOT_PROVIDED = (
    f"{COLORS['R']}A opção %s requer um valor.{COLORS['.']} "
    f"Informe um valor válido após a opção."
)
ERROR_MESSAGE_INVALID_PROVIDED_VALUE_TYPE = (
    f"{COLORS['R']}Valor inválido para "
    f"\"{COLORS['W']}%(key)s{COLORS['R']}\": "
    f"\"{COLORS['W']}%(value)s{COLORS['R']}\". "
    f"Tipo esperado: {COLORS['C']}%(expected_type)s{COLORS['.']}."
)
ERROR_MESSAGE_PROVIDED_FILE_DOES_NOT_EXIST = (
    f"{COLORS['R']}O arquivo informado não foi encontrado no caminho:"
    f"{COLORS['.']} {COLORS['W']}%s{COLORS['.']}"
)
WARNING_MESSAGE_SIGNAL_CLOSING_SIGNAL = (
    f"{COLORS['Y']}Solicitação de encerramento recebida "
    f"(sinal: %s).{COLORS['.']} "
    f"Encerrando o programa..."
)