# Calculadora de Hash de Arquivos

Ferramenta de linha de comando para calcular o hash de arquivos utilizando diferentes algoritmos criptográficos disponíveis na biblioteca padrão do Python.

O arquivo é processado em pequenos blocos (*chunks*) de dados binários, permitindo calcular o hash de arquivos grandes sem a necessidade de carregá-los integralmente na memória.

---

## Sobre o projeto

A **Calculadora de Hash de Arquivos** foi desenvolvida para facilitar a verificação da integridade de arquivos por meio de funções de hash.

A ferramenta permite:

* Calcular hashes de arquivos de diferentes tamanhos.
* Escolher entre diversos algoritmos de hash.
* Definir o tamanho dos blocos utilizados durante a leitura.
* Processar arquivos grandes com baixo consumo de memória.
* Executar diretamente pelo código-fonte ou por meio de um executável.
* Utilizar o programa diretamente pelo terminal.

O processamento é realizado em modo binário e o resultado é apresentado em formato hexadecimal.

---

## Requisitos

Para executar o projeto a partir do código-fonte, é necessário ter:

* **Python 3.14 ou superior**
* [uv](https://docs.astral.sh/uv/) — recomendado para gerenciamento do ambiente e execução do projeto.

Para gerar o executável, o projeto utiliza o **PyInstaller**.

---

## Instalação

Clone o repositório e acesse o diretório do projeto:

```shell
git clone <URL_DO_REPOSITORIO>
cd file-hash
```

Sincronize as dependências do projeto:

```shell
uv sync
```

Depois disso, o programa pode ser executado utilizando:

```shell
uv run src/__main__.py --file arquivo.txt
```

---

## Como utilizar

A ferramenta pode ser executada pelo terminal informando o caminho do arquivo.

A sintaxe básica é:

```shell
uv run src/__main__.py --file [CAMINHO_DO_ARQUIVO]
```

Também é possível especificar o algoritmo de hash e o tamanho dos blocos:

```shell
uv run src/__main__.py \
    --file [CAMINHO_DO_ARQUIVO] \
    --hash [ALGORITMO] \
    --chunk_size [TAMANHO_DO_BLOCO]
```

### Exemplo

Para calcular o hash SHA-256 de um arquivo chamado `arquivo.txt`:

```shell
uv run src/__main__.py --file arquivo.txt --hash sha256
```

O resultado será exibido no terminal.

### Tamanho dos blocos

O tamanho padrão dos blocos é de **1024 bytes**.

Esse valor pode ser alterado utilizando a opção `--chunk_size`:

```shell
uv run src/__main__.py --file arquivo.txt --chunk_size 4096
```

Nesse exemplo, o arquivo será processado em blocos de **4096 bytes (4 KiB)**.

Alterar o tamanho do bloco pode modificar o desempenho da leitura, mas **não altera o hash final do arquivo**.

---

## Gerando o executável

O projeto possui um script `build.py` responsável por automatizar a geração do executável utilizando o PyInstaller.

Para gerar o executável, execute:

```shell
uv run build.py
```

O processo de build irá empacotar a aplicação e seus arquivos necessários em um executável.

Após a construção, o executável estará disponível no diretório:

```text
dist/
```

Por exemplo:

```text
dist/
└── file-hash.exe
```

No Windows, o programa pode então ser executado diretamente:

```powershell
.\dist\file-hash.exe --file arquivo.txt
```

### Build manual

Caso seja necessário executar o PyInstaller diretamente, o processo pode ser realizado com:

```shell
uv run pyinstaller
```

Entretanto, recomenda-se utilizar o `build.py`, pois ele centraliza as configurações necessárias para a construção do executável e inclusão dos arquivos adicionais do projeto.

---

## Opções disponíveis

Para visualizar todas as opções disponíveis:

```shell
uv run src/__main__.py --help
```

| Opção          | Descrição                                                    | Valor padrão    |
| -------------- | ------------------------------------------------------------ | --------------- |
| `--help`       | Exibe a documentação de ajuda da aplicação.                  | —               |
| `--file`       | Define o caminho do arquivo cujo hash será calculado.        | **Obrigatório** |
| `--hash`       | Define o algoritmo de hash utilizado no cálculo.             | `sha256`        |
| `--chunk_size` | Define o tamanho dos blocos utilizados na leitura, em bytes. | `1024`          |

---

## Algoritmos de hash suportados

A aplicação utiliza algoritmos disponibilizados pela biblioteca `hashlib` do Python.

| Algoritmo  | Descrição                                                                                                                   |
| ---------- | --------------------------------------------------------------------------------------------------------------------------- |
| `md5`      | Algoritmo legado, utilizado principalmente para compatibilidade e verificações de integridade não relacionadas à segurança. |
| `sha1`     | Algoritmo legado, ainda encontrado em sistemas e ferramentas antigas.                                                       |
| `sha256`   | Algoritmo da família SHA-2, amplamente utilizado para verificação de integridade.                                           |
| `sha512`   | Algoritmo da família SHA-2 que produz um digest de 512 bits.                                                                |
| `sha3_256` | Algoritmo da família SHA-3 que produz um digest de 256 bits.                                                                |
| `sha3_512` | Algoritmo da família SHA-3 que produz um digest de 512 bits.                                                                |
| `blake2b`  | Função de hash criptográfico da família BLAKE2, projetada para oferecer alto desempenho e segurança.                        |
| `blake2s`  | Variante do BLAKE2 otimizada para arquiteturas com recursos mais limitados.                                                 |

> **Observação:** MD5 e SHA-1 possuem vulnerabilidades conhecidas relacionadas a colisões. Para aplicações que exigem resistência a colisões, prefira algoritmos como SHA-256, SHA-512, SHA-3 ou BLAKE2.

---

## Funcionamento

O cálculo do hash segue as seguintes etapas:

1. A aplicação recebe o caminho do arquivo e as opções informadas pelo usuário.
2. Verifica se o caminho informado existe.
3. Verifica se o caminho corresponde a um arquivo válido.
4. Cria o objeto correspondente ao algoritmo de hash selecionado.
5. Abre o arquivo em modo binário.
6. Lê o arquivo em blocos (*chunks*).
7. Atualiza o objeto de hash com os dados de cada bloco.
8. Continua o processamento até o final do arquivo.
9. Obtém o digest hexadecimal resultante.
10. Exibe o hash calculado no terminal.

O processamento em blocos permite trabalhar com arquivos grandes utilizando uma quantidade reduzida e previsível de memória.

Por exemplo, considerando um arquivo de **10 GB** e um `chunk_size` de **1024 bytes**, a aplicação não precisa carregar os 10 GB na memória de uma só vez. Ela processa os dados progressivamente.

---

## Exemplo completo

Calculando o SHA-256 de `arquivo.txt`:

```shell
uv run src/__main__.py --file arquivo.txt --hash sha256
```

Calculando SHA-512 com blocos de 4096 bytes:

```shell
uv run src/__main__.py --file arquivo.txt --hash sha512 --chunk_size 4096
```

Calculando BLAKE2b:

```shell
uv run src/__main__.py --file arquivo.txt --hash blake2b
```

Utilizando o executável no Windows:

```powershell
.\dist\file-hash.exe --file arquivo.txt --hash sha256
```

---

## Estrutura do projeto

```text
file-hash/
├── assets/
├── src/
│   ├── __main__.py
│   └── lib/
│       ├── assets/
│       │   └── symbol_ascii.txt
│       ├── errors.py
│       ├── file.py
│       └── texts.py
├── build.py
├── pyproject.toml
├── uv.lock
└── README.md
```

### Principais arquivos

| Arquivo             | Responsabilidade                                              |
| ------------------- | ------------------------------------------------------------- |
| `src/__main__.py`   | Ponto de entrada da aplicação.                                |
| `src/lib/file.py`   | Operações relacionadas à leitura e processamento de arquivos. |
| `src/lib/errors.py` | Definição e tratamento dos erros da aplicação.                |
| `src/lib/texts.py`  | Textos e elementos visuais utilizados pela CLI.               |
| `src/lib/assets/`   | Arquivos adicionais utilizados pela aplicação.                |
| `build.py`          | Automatiza a construção do executável com PyInstaller.        |
| `pyproject.toml`    | Configuração e metadados do projeto.                          |
| `uv.lock`           | Versões exatas das dependências utilizadas pelo ambiente.     |

---

## Tecnologias utilizadas

* **Python 3.14+**
* **hashlib** — cálculo dos hashes.
* **PyInstaller** — geração do executável.
* **uv** — gerenciamento do ambiente e dependências.

---

## Licença

Este projeto está disponível sob a licença definida no repositório.
