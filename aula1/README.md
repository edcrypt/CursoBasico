Aula 01
=======

Vamos ver algumas partes básicas da sintaxe. Sintaxe é o conjunto de regras que define a estrutura da linguagem, por exemplo, pense no portugues, não da para sair escrevendo palavras aleatorias: isso não faria nenhum sentido e por isso é preciso usar regras de escrita para que a linguagem seja legivel. 

Mesmo assim, você ainda pode fazer uma frase que seja sintaticamente correta (obedeça todas as regras de como juntar as palavras e pontuações), mas que não faça sentido lógico: não quer dizer que esteja *semanticamente* correta. Da mesma forma, o interpretador de Python pode não reclamar da forma como você usa seus simbolos (`SyntaxError`) e ainda reclamar que não consegue executá-lo até o fim.

### Váriaveis

Variaveis representam valores através de atribuições, por exemplo:

```python
nome = 'Rafael'
idade = 28
```

A variavel 'nome', após a operação de atribuição, representa o valor 'Rafael'. Em seguida, usamos novamente o operador `=` para atribuir o valor `28` ao nome `idade`. A regra geral da atribuição é: `nome_da_variavel = expressao`. 

O nome da variável deve começar com uma letra (`a`, `b`, `c`, etc) ou undescore (`_`), e pode ser seguida de qualquer combinação de numeros, underscores e letras. Por exemplo, são nomes válidos: `aaaaaaa`, `nome2`, `minha_variavel_01`, `_1_variavel`, etc.

A expressão, do lado direito do `=`, pode ser tanto um valor simples, como 'Rafael' ou 28 no exemplo acima, ou algo um pouco mais complexo, como uma conta:

```python
minutos_por_dia = 60 * 24
```

Nesse caso, o Python primeiro executa o lado direito (ou seja, faz a conta `60 * 24`, e depois atribui o resultado ao nome do lado esquerdo (nesse caso, `minutos_por_dia`). Depois, você pode usar a variável `minutos_por_dia` para outras contas ou comparções, conforme você precisar.

Python é uma linguagem dinamicamente tipada, ou seja, uma variável pode apontar para qualquer tipo de valor, não existe uma regra que proiba uma variavel 'nome' de conter por exemplo a idade 19. Em uma linguagem estáticamente tipada o código a seguir não funcionaria:

```python
nome = 'Rafael'
nome = 29
```

Pense em variáveis como nomes que fazem referência para algum valor guardado na memória. Esses nomes podem passar a apontar para outros valores a qualquer momento, de qualquer tipo. O tipo daquele valor, que determina que operações você pode fazer com ele, é uma informação que está atrelada ao *valor* em sí, não ao(s) nome(s).
