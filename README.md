# Calculadora de Hash de Arquivos

## Sobre o projeto

Este script permite calcular o hash de arquivos utilizando diferentes algoritmos de hash disponíveis no Python.

O arquivo é lido em blocos (*chunks*) de dados binários, permitindo processar arquivos de diferentes tamanhos sem a necessidade de carregá-los integralmente na memória.

Ao final do processamento, o script retorna o hash calculado de acordo com o algoritmo selecionado pelo usuário.

## Como utilizar o script?

Execute o script pelo terminal, informando o caminho do arquivo e, opcionalmente, o algoritmo de hash e o tamanho dos blocos utilizados na leitura.

```shell
./main.py --file [CAMINHO_DO_ARQUIVO] --hash [ALGORITMO] --chunk_size [TAMANHO_DO_BLOCO]
```

### Exemplo de utilização

Para calcular o hash SHA-256 de um arquivo chamado `arquivo.txt`:

```shell
./main.py --file arquivo.txt --hash sha256
```

O tamanho padrão dos blocos é de **1024 bytes**. Esse valor pode ser alterado por meio da opção `--chunk_size`.

## Opções disponíveis

Para visualizar as opções disponíveis e suas respectivas descrições, execute:

```shell
./main.py --help
```

| Opção          | Descrição                                                               | Valor padrão |
| -------------- | ----------------------------------------------------------------------- | ------------ |
| `--help`       | Exibe a documentação de ajuda do script.                                | —            |
| `--file`       | Define o caminho do arquivo cujo hash será calculado.                   | Obrigatório  |
| `--hash`       | Especifica o algoritmo de hash utilizado.                               | `sha256`     |
| `--chunk_size` | Define o tamanho dos blocos utilizados na leitura do arquivo, em bytes. | `1024`       |

## Algoritmos de hash suportados

O script oferece suporte aos seguintes algoritmos:

| Algoritmo  | Descrição                                                                                                    |
| ---------- | ------------------------------------------------------------------------------------------------------------ |
| `md5`      | Algoritmo legado, utilizado principalmente para compatibilidade e verificações não relacionadas à segurança. |
| `sha1`     | Algoritmo legado, ainda encontrado em sistemas e ferramentas antigas.                                        |
| `sha256`   | Algoritmo da família SHA-2, amplamente utilizado para verificação de integridade.                            |
| `sha512`   | Algoritmo da família SHA-2, que produz um hash de 512 bits.                                                  |
| `sha3_256` | Algoritmo da família SHA-3, que produz um hash de 256 bits.                                                  |
| `sha3_512` | Algoritmo da família SHA-3, que produz um hash de 512 bits.                                                  |
| `blake2b`  | Algoritmo moderno de hash criptográfico, com foco em desempenho e segurança.                                 |
| `blake2s`  | Variante do BLAKE2 otimizada para plataformas com recursos mais limitados.                                   |

> **Observação:** MD5 e SHA-1 possuem vulnerabilidades conhecidas relacionadas a colisões. Para aplicações que exigem resistência a colisões, prefira algoritmos como SHA-256, SHA-512, SHA-3 ou BLAKE2.

## Funcionamento

O processo de cálculo do hash segue estas etapas:

1. O script recebe o caminho do arquivo e as opções informadas pelo usuário.
2. Verifica se o arquivo existe e se o caminho corresponde a um arquivo válido.
3. Abre o arquivo em modo binário e realiza sua leitura em blocos (*chunks*).
4. Atualiza o objeto de hash com os dados de cada bloco lido.
5. Finaliza o processamento e retorna o hash hexadecimal do arquivo.

O processamento em blocos permite calcular o hash de arquivos grandes com um consumo de memória reduzido, sem alterar o resultado final do hash.
