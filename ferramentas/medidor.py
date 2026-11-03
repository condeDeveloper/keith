# -*- coding: utf-8 -*-
"""Roda as tabelas que vao para o README.

    python -m ferramentas.medidor
    python -m ferramentas.medidor --completo
"""
import sys
import time

from keith import juiz, sequencia, varredura

LIMITE = 200_000
LIMITE_JUIZ = 20_000
LIMITE_COMPLETO = 10_000_000


def titulo(texto):
    print()
    print(texto)
    print('-' * len(texto))


def as_sequencias():
    titulo('Algumas sequencias')
    for n in (14, 19, 197, 742, 1537):
        c = sequencia.cadeia_ate(n)
        largura = len(str(n))
        print('%-8d  %s  |  %s' % (
            n,
            ', '.join(str(x) for x in c[:largura]),
            ', '.join(str(x) for x in c[largura:])))
    print()
    print('E um que nao e:')
    c = sequencia.cadeia_ate(15)
    print('%-8d  %s  (passou de 15 sem acertar)'
          % (15, ', '.join(str(x) for x in c)))


def a_lista():
    titulo('Os numeros de Keith ate %d' % LIMITE)
    achados = varredura.ate(LIMITE)
    print('sao %d:' % len(achados))
    for i in range(0, len(achados), 8):
        print('   ' + '  '.join('%-8d' % n for n in achados[i:i + 8]))
    print()
    conta = varredura.por_quantidade_de_digitos(LIMITE)
    print('%-10s %-12s %-16s %s' % ('digitos', 'quantos', 'numeros da faixa', 'densidade'))
    for d in sorted(conta):
        total = 9 * 10 ** (d - 1)
        print('%-10d %-12d %-16d %.3e' % (d, conta[d], total, conta[d] / total))


def os_passos():
    titulo('Quantos passos cada um leva para se alcancar')
    achados = varredura.ate(LIMITE)
    print('%-10s %-10s %s' % ('numero', 'digitos', 'passos'))
    for n, passos in varredura.passos_dos_achados(achados)[:14]:
        print('%-10d %-10d %d' % (n, len(str(n)), passos))
    media, quantos = varredura.custo_de_decidir(LIMITE)
    print()
    print('media de passos para decidir um numero qualquer ate %d: %.2f'
          % (LIMITE, media))
    print('   (amostra de %d numeros)' % quantos)
    print('O teste de UM numero e barato. O caro e que nao da para pular nenhum.')


def a_raridade():
    titulo('A raridade, por faixa')
    print('%-26s %-10s %s' % ('faixa', 'quantos', 'quais'))
    for baixo, alto, quantos, quais in varredura.densidade_por_faixa(LIMITE, 7):
        texto = ', '.join(str(n) for n in quais) if quais else '(nenhum)'
        if len(texto) > 44:
            texto = texto[:41] + '...'
        print('%-26s %-10d %s' % ('%d a %d' % (baixo, alto), quantos, texto))


def o_juiz():
    titulo('As duas conferencias')
    print('janela que para cedo x lista que guarda tudo: %d numeros conferidos'
          % varredura.conferir_contra_juiz(LIMITE_JUIZ))
    achados = varredura.ate(LIMITE)
    print('cada termo e a soma dos n anteriores        : %d passos conferidos'
          % varredura.conferir_sequencias(achados))
    print()
    print('quantos termos bastam para decidir um numero:')
    for n in (197, 7385, 93993, 1084051):
        print('   %-10d  %d termos' % (n, juiz.quantos_termos_bastam(n)))


def completo():
    titulo('Varredura ate %d' % LIMITE_COMPLETO)
    comeco = time.time()
    achados = varredura.ate(LIMITE_COMPLETO)
    print('numeros de Keith ate %d: %d' % (LIMITE_COMPLETO, len(achados)))
    print()
    for i in range(0, len(achados), 6):
        print('   ' + '  '.join('%-10d' % n for n in achados[i:i + 6]))
    print()
    conta = varredura.por_quantidade_de_digitos(LIMITE_COMPLETO)
    print('%-10s %-12s %s' % ('digitos', 'quantos', 'densidade'))
    for d in sorted(conta):
        total = 9 * 10 ** (d - 1)
        print('%-10d %-12d %.3e' % (d, conta[d], conta[d] / total))
    print()
    print('tempo: %.1f s' % (time.time() - comeco))

    if achados[:7] != [14, 19, 28, 47, 61, 75, 197]:
        print('MEDIDA MUDOU: os sete menores deveriam ser 14, 19, 28, 47, 61, 75, 197')
        sys.exit(1)
    print('os sete menores bateram')


def main():
    if '--completo' in sys.argv:
        completo()
        return
    as_sequencias()
    a_lista()
    os_passos()
    a_raridade()
    o_juiz()


if __name__ == '__main__':
    main()
