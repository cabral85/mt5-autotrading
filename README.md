# MT5 AutoTrader - Setups Larry Willians

Projeto criado para validar diversos setups em diversos papeis na B3.

A lista de ações pode ser editada através do arquivo "stock-list.txt" bastando adicionar uma nova linha no padrão \ n
A lista de contratos futuros pode ser editada através do arquivo "future-contracts.txt" bastando editar as linhas, ou adicionar uma nova

Para adicionar um par de moedas deverá ser feito através do arquivo "stock-list" pois a ideia do arquivo de contratos futuros é que ele leia o papel e adicione automaticamente a variavel de contrato atual, exemplo: WDO deve passar para WDOK22, WIN deve passar para WINM22, e esse papel deverá ser atualizado automaticamente, algo que não ocorre com ações ou pares de moedas.

## Requisitos
* Ter o MetaTrader5 instalado no computador
* Ter ao menos o python 3.x instalado
* Ter o gerenciador de pacotes "pip" instalado

## Para executar o projeto

```
$ python -m venv mt5_env

$ .\env\Scripts\activate.bat

$ pip install -r requirements

$ python app.py
```

## Etapas do Projeto
* Etapa 1 - Pegar os preços :heavy_check_mark:
* Etapa 2 - Criar média exponencial - :hourglass:
* Etapa 3 - Setup 9.2 do Larry Williams e enviar mensagem na tela
* Etapa 4 - Adicionar preço de entrada, stop loss e take profit na notificação de tela
* Etapa 5 - Adicionar setups 9.0 e 9.1 do Larry Willians
* Etapa 6 - Automatizar as entradas de acordo com os preços e stops com razão de ganho de ao menos 1x1
* Etapa 7 - Adicionar leitura de figuras gráficas: OCO e OCOI - e notificar
* Etapa 8 - Adicionar leitura de figuras gráficas: triangulo e retangulo - e notificar
* Etapa 9 - Automatizar a entrada das figuras gráficas após pull-back