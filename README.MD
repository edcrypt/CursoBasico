Começando a bagaça
==================
Ola? Fiquei sabendo que você esta querendo aprender um pouco de python, certo?
Então você veio ao lugar certo, vamos começar pelo básico:


Mas o que fodendo é Python?
===========================

Python é uma linguagem de programação criada pelo holandês Guido van Rossum.
Python é uma linguagem interpretada, de alto nível e dinamicamente/fortemente tipada. Vamos tratar de todas essas logo em seguida, mas por enquanto vamos focar no seguinte fato: Python é a melhor linguagem de programação do universo. Tendo dito isso, vamos começar!

### Linguagem interpretada
Isso significa que Python não é uma linguagem compilada (pelo menos não diretamente para linguagem de máquina, mas há um processo de compilação para uma linguagem intermediária, semelhante a Java). Segundo a wikipédia significa:

  Linguagem interpretada é uma linguagem de programação onde o código fonte nessa linguagem é executado por um programa de computador chamado interpretador, que em seguida é executado pelo sistema operacional ou processador.

Ou seja, o código em Python é lido por um programa (interpretador) que transforma o código python em código de maquina e o executa, passo a passo.


### Linguagem de Alto Nível

Uma linguagem de alto nível é uma linguagem que se aproxima mais da linguagem humana do que da maquina, sendo assim mais fácil de se compreender e escrever.


### Linguagem com tipagem dinamica e fortemente tipada.

Linguagens dinamicamente tipadas são aquelas que não associam uma variável (um nome que faz referência a um valor) a um tipo específico. Elas permitem que o programador escreva um código que aceite qualquer objeto que obedeça um a "protocolo" informal (que atue como um arquivo, por exemplo), independente do tipo. 

Mas tipos ainda são importantes: Python não assume o que você quer dizer ao tentar somar um tipo de texto (string, unicode) com um número (inteiros, ponto flutuantes). Ele vai dar um `TypeError`, que basicamente quer dizer: você quer concatenar (como em Javascript) ou transformar o texto em número e fazer uma soma?


Esse são algumas das caracteristicas básicas da linguagem, veremos outras em breve.

Para abrir o apetite, abra o python num terminal (ou abra o Idle, se tiver instalado), digite uma conta simples e aperte Enter:

```python
2 + 2
```

O resultado deve ter aparecido em seguida, e uma nova linha começando com `>>>` deve ter aparecido para você entrar outro comando.

Nada surpreendente por enquanto, certo? Mas é bom se acostumar com o terminal do Python. É uma forma interativa de aprender a linguagem.
