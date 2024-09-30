<<<<<<< HEAD
# desafio-dio-otimizando-o-sitema-bancario-com-funcoes-python
=======
# Sistema Bancário Simples com Python

Este projeto é uma aplicação de terminal para simular operações bancárias simples, como depósito, saque, consulta de extrato, criação de usuários, e criação/acesso a contas correntes. O sistema permite gerenciar usuários e suas respectivas contas bancárias de maneira eficiente.

## Funcionalidades

O programa possui um menu com as seguintes opções:

- `[d] Depositar`: Realiza depósitos na conta corrente.
- `[s] Sacar`: Realiza saques na conta corrente, com limite de valor e quantidade de saques diários.
- `[e] Extrato`: Exibe o extrato bancário contendo as movimentações realizadas.
- `[u] Novo usuário`: Permite o cadastro de novos usuários no sistema.
- `[c] Criar conta corrente`: Cria uma nova conta corrente vinculada a um CPF já cadastrado.
- `[a] Acessar conta corrente`: Permite acessar uma conta corrente específica, validando agência e número da conta.
- `[l] Lista de usuários`: Lista todos os usuários cadastrados.
- `[q] Sair`: Encerra o programa.

## Variáveis Globais

O programa utiliza algumas variáveis globais para armazenar dados temporários:

- `saldo`: Armazena o saldo atual da conta.
- `limite`: Define o limite máximo para saques.
- `extrato`: Armazena o histórico de movimentações da conta.
- `numero_saques`: Controla o número de saques realizados no dia.
- `LIMITE_SAQUES`: Define o limite diário de saques.
- `contador`: Controla o número de contas correntes criadas.
- `usuarios`: Lista de dicionários que armazenam os dados dos usuários.

## Funções

### `funcao_deposito(saldo, valor, extrato)`

Essa função permite realizar um depósito em uma conta corrente. Ela recebe o saldo atual, o valor a ser depositado e o extrato da conta.

- Verifica se o valor é maior que zero para proceder com o depósito.
- Atualiza o saldo e o extrato da conta.
- Retorna o saldo e o extrato atualizados.

### `funcao_saque(saldo, valor, extrato, limite, numero_saques, limite_saques)`

Essa função realiza o saque de uma conta, validando as regras de saldo, limite diário e quantidade máxima de saques.

- Verifica se o valor do saque excede o saldo, o limite ou o número máximo de saques.
- Se tudo estiver correto, o saldo e o extrato são atualizados, e o número de saques é incrementado.
- Retorna o saldo, extrato e número de saques atualizados.

### `funcao_extrato(saldo, extrato)`

Exibe o extrato das movimentações da conta e o saldo atual.

- Caso não haja movimentações, exibe uma mensagem informando que não foram realizadas movimentações.

### `funcao_formata_cpf(cpf)`

Remove caracteres não numéricos de um CPF informado, retornando apenas os números.

### `funcao_cpf_existe(cpf)`

Verifica se um CPF já está cadastrado na lista de usuários.

- Retorna `True` se o CPF existir e `False` caso contrário.

### `funcao_novo_usuario(cpf, nome, data_de_nascimento, logradouro, numero, bairro, cidade, estado)`

Permite o cadastro de um novo usuário no sistema.

- Verifica se o CPF informado já existe no sistema.
- Armazena os dados do novo usuário, como CPF, nome, data de nascimento e endereço.
- Adiciona o novo usuário à lista de usuários.

### `funcao_cria_conta_corrente(cpf)`

Cria uma nova conta corrente para um usuário já cadastrado.

- Cada conta corrente é vinculada a um CPF e possui um número único gerado automaticamente.
- A conta é adicionada ao campo `contas_correntes` do usuário correspondente.

### `funcao_acessar_conta(agencia, conta_corrente, cpf)`

Permite acessar uma conta corrente específica, verificando se a agência e o número da conta estão corretamente vinculados ao CPF informado.

- Se as informações forem válidas, exibe uma mensagem de acesso autorizado.
- Caso contrário, informa se houve erro nos dados da agência, conta ou CPF.

## Como Executar

1. Clone ou baixe este repositório para o seu ambiente local.
2. Abra o terminal na pasta do projeto.
3. Execute o arquivo Python:

```bash
python sistema_bancario.py
```

4. Siga as instruções no menu para realizar as operações bancárias.

## Estrutura de Dados

- Os dados dos usuários são armazenados em uma lista de dicionários. Cada dicionário contém as seguintes chaves:
  - `cpf`: CPF do usuário.
  - `nome`: Nome completo do usuário.
  - `data_de_nascimento`: Data de nascimento do usuário.
  - `endereco`: Um dicionário contendo logradouro, número, bairro, cidade e estado.
  - `contas_correntes`: Uma lista de dicionários, onde cada dicionário representa uma conta corrente associada ao usuário.

Exemplo de estrutura de um usuário:

```python
usuarios = [
    {
        "cpf": "12345678900",
        "nome": "João Silva",
        "data_de_nascimento": "01/01/1990",
        "endereco": {
            "logradouro": "Rua ABC",
            "numero": "100",
            "bairro": "Centro",
            "cidade": "São Paulo",
            "estado": "SP"
        },
        "contas_correntes": [
            {
                "agencia": "0001",
                "conta_corrente": "1"
            }
        ]
    }
]
```

## Considerações Finais

Este projeto serve como um exemplo didático para reforçar conceitos de funções, manipulação de dicionários e listas, controle de fluxo e lógica de negócios com Python. Pode ser expandido para incluir mais funcionalidades, como persistência de dados em banco de dados ou autenticação de usuários.
>>>>>>> 9d0e947 (Adiciona sistema bancário e README)
