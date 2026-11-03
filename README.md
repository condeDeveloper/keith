# keith

Pegue os dígitos de `197`: **1, 9, 7**. Agora some os três últimos, repetidamente:

```
1, 9, 7, 17, 33, 57, 107, 197
```

O próprio `197` apareceu. Números assim chamam-se **números de Keith**, e eles são raros
de um jeito desconfortável: existem **36 abaixo de dez milhões**, e a busca inteira já
feita no mundo encontrou pouco mais de cem.

```bash
python -m unittest discover -s testes -t . -v   # 18 testes
python -m ferramentas.medidor                   # todas as tabelas
python -m ferramentas.medidor --completo        # até 10 milhões (job próprio)
```

Python 3.11+, sem dependência nenhuma fora da biblioteca padrão.

## Como são

```
14    → 1, 4            | 5, 9, 14
19    → 1, 9            | 10, 19
197   → 1, 9, 7         | 17, 33, 57, 107, 197
742   → 7, 4, 2         | 13, 19, 34, 66, 119, 219, 404, 742
1537  → 1, 5, 3, 7      | 16, 31, 57, 111, 215, 414, 797, 1537
```

E um que não é:

```
15    → 1, 5, 6, 11, 17   (passou de 15 sem acertar)
```

## Os 36 até dez milhões

```
14        19        28        47        61        75
197       742       1104      1537      2208      2580
3684      4788      7385      7647      7909      31331
34285     34348     55604     62662     86935     93993
120284    129106    147640    156146    174680    183186
298320    355419    694280    925993    1084051   7913837
```

Repare no fim: entre `1084051` e `7913837` existem quase sete milhões de inteiros e
**nenhum** número de Keith.

## A raridade

```
dígitos   quantos   números da faixa   densidade
2         6         90                 6,667 × 10⁻²
3         2         900                2,222 × 10⁻³
4         9         9.000              1,000 × 10⁻³
5         7         90.000             7,778 × 10⁻⁵
6         10        900.000            1,111 × 10⁻⁵
7         2         9.000.000          2,222 × 10⁻⁷
```

A densidade cai de **6,7%** para **0,00002%** — cinco ordens de grandeza em cinco
dígitos. Mas repare na coluna do meio: a **quantidade absoluta** não cai junto. Ela
oscila entre 2 e 10 enquanto a faixa fica dez vezes maior a cada linha.

## Decidir é barato; procurar é que é caro

A sequência de Keith quase dobra a cada termo, então ela alcança qualquer número em
poucas dezenas de passos:

```
número      termos que bastam
197         11
7385        17
93993       22
1084051     28
```

`1.084.051` é **cinco mil vezes** maior que `197` e custa **menos de três vezes** mais
para decidir. O custo é proporcional ao número de bits, não ao número.

```
média de passos para decidir um número qualquer até 200.000: 14,45
```

E, no entanto, a varredura até dez milhões leva três minutos. O motivo é que **não se
conhece jeito de pular nenhum número**: cada inteiro precisa ser testado individualmente.
Um teste barato, dez milhões de vezes.

## Dois caminhos

O caminho principal mantém uma **janela** dos últimos `n` termos e para assim que
ultrapassa o número — nunca guarda a sequência inteira, nunca calcula um termo a mais do
que precisa.

O juiz gera uma quantidade fixa de termos, guarda tudo numa lista e procura o número
nela. Gasta memória e tempo à toa, e **não corre o risco de parar cedo demais**, que é o
único jeito de a janela errar.

```
janela que para cedo x lista que guarda tudo : 19.991 números conferidos
cada termo é a soma dos n anteriores         : 292 passos conferidos
```

## O que as medidas me corrigiram

**Esperei a quantidade por faixa constante.** Vendo 6 números com dois dígitos e 9 com
quatro, imaginei uma taxa estável — algo em torno de meia dúzia por tamanho. São **2** com
três dígitos, **10** com seis e **2** com sete. A sequência não tem taxa: tem sorte.

**Confundi "barato de testar" com "rápido de achar".** Decidir um número custa 14 passos
em média, e isso me fez escrever no rascunho que a busca era eficiente. A varredura até
dez milhões leva **três minutos** — porque o teste barato precisa rodar dez milhões de
vezes, e não existe peneira que pule candidatos. Os dois fatos são verdadeiros e dizem
coisas opostas; o README precisa dos dois.

**Números de um dígito tornariam a definição trivial.** Para `n < 10`, a "sequência"
começaria no próprio número e ele se alcançaria em zero passos. Todos os dez seriam
números de Keith, e a lista começaria com lixo. A função recusa esse caso
explicitamente, e um teste cobre os dez.

**O juiz precisava de um teto honesto.** Ele gera 200 termos e procura o número entre
eles. Como a sequência quase dobra a cada passo, 200 termos cobrem números de 60 dígitos
— folgado para o que se varre aqui, mas é um teto, e está escrito como tal em vez de
"suficiente".

## Quatro achados

1. São apenas **36 números de Keith abaixo de dez milhões**, e entre `1.084.051` e
   `7.913.837` existem quase **sete milhões de inteiros sem nenhum**.
2. A densidade cai **cinco ordens de grandeza em cinco dígitos** — de 6,7% para 0,00002% —
   enquanto a quantidade absoluta por faixa **oscila entre 2 e 10**, sem tendência.
3. **Decidir custa logaritmo:** `1.084.051` é cinco mil vezes maior que `197` e precisa de
   28 termos contra 11 — menos de três vezes mais.
4. E mesmo assim a varredura leva **três minutos para dez milhões**, porque o teste barato
   tem que rodar uma vez para cada inteiro: não se conhece peneira que pule candidatos.
