# TelZir
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

Com o novo produto FaleMais da Telzir o cliente adquire um plano e pode falar de graça até
um determinado tempo (em minutos) e só paga os minutos excedentes. Os minutos excedentes
tem um acréscimo de 10% sobre a tarifa normal do minuto. Os planos são FaleMais 30 (30
minutos), FaleMais 60 (60 minutos) e FaleMais 120 (120 minutos).
A Telzir, preocupada com a transparência junto aos seus clientes, quer disponibilizar uma
página na web onde o cliente pode calcular o valor da ligação. Ali, o cliente pode escolher os
códigos das cidades de origem e destino, o tempo da ligação em minutos e escolher qual o
plano FaleMais. O sistema deve mostrar dois valores: (1) o valor da ligação com o plano e (2)
sem o plano. O custo inicial de aquisição do plano deve ser desconsiderado para este problema.

# Tecnologia
- `Sistema desenvolvido em Python versão:3.10`
- `Base de dado utilizada: SQLITE`

## Requisitos

Esse projeto exige a utilização do [Docker](https://www.docker.com/) localmente.


# Instalação
- Tenha o python versao 3.10 instalado em sua maquina;
- Copie todo conteudo para uma pasta:
- instala o venv em seu ambiente como o coamndo:
    ```bash
    python3 -m venv nome_do_ambiente_virtual
    ```
- Ative seu ambinete criado com o comando:
    ```bash
    source nome_do_ambiente_virtual/bin/activate
    ```

# URL
- `O sistema ira rodar no endereçõ 127.0.0.1/5000`

# Testes Unitários
***Para rodar os testes unitários, netre na pasta raiz do sistema e rode o comnado***
```bash
    python -m unittest -v
```

## Orientações para contribuidores

Antes de efetuar qualquer contribuição para esse projeto, certifique-se de seguir as orientações documentadas no arquivo [CONTRIBUTING.md](/CONTRIBUTING.md)