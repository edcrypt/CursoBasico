# -*- coding: utf-8 -*-

# Variaveis

# String
nome = 'Jefferson'

# Inteiro (numero)
idade = 24

# Float (numero quebrado) 75 kilos e 300 gramas
peso = 75.3

# Boleano, sim ou não
solteiro = True

# Lista pode contar nenhum ou varios elemntos
devendo = ['Bradesco', 'Claro']

# Dicionario, contem chaves associadas com valores
endereco = {
    'rua': '9 de julho',
    'cidade': 'São Paulo',
}


print 'Ola, meu nome é %s, tenho %d anos e peso %0.2fkg' % (
      nome, idade, peso
    )

for nome in devendo:
    print 'Devo a(ao) %s' % nome

# Verificando se estou solteiro ou não
if solteiro:
    print 'Estou solteiro'
else:
    print 'Não estou solteiro'


print 'Meu endereco é Rua {rua} e na cidade {cidade}'.format(**endereco)
