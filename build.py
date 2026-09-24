import sys
from pathlib import Path
try:
    from PyInstaller.__main__ import run
except ModuleNotFoundError:
    sys.stdout.write(
        "O módulo `PyInstaller` não foi encontrado. Sincronize as dependências de desenvolvimento executando `uv sync --dev` e tente novamente."
    )
    sys.exit(1)


ROOT_DIR = Path(__file__).resolve().parent
NAME_SCRIPT = "hashforge"
ICON_PATH = "assets/icon.ico"
SCRIPT_MAIN="src/__main__.py"

def main():
    options = [
        SCRIPT_MAIN,
        f"--name={NAME_SCRIPT}",
        "--onefile",
        "--clean",
        f"--icon={ICON_PATH}",
        f"--add-data={ROOT_DIR/'src'/'lib'/'assets'};lib/assets"
    ]

    run(options)


if __name__ == "__main__":
    main()