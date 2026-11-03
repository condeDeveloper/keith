# -*- coding: utf-8 -*-
import unittest

from keith import juiz, sequencia


class TestSequencia(unittest.TestCase):

    def test_a_sequencia_do_197(self):
        self.assertEqual(sequencia.cadeia_ate(197), [1, 9, 7, 17, 33, 57, 107, 197])
        self.assertTrue(sequencia.eh_keith(197))

    def test_a_sequencia_do_14(self):
        self.assertEqual(sequencia.cadeia_ate(14), [1, 4, 5, 9, 14])
        self.assertTrue(sequencia.eh_keith(14))

    def test_o_15_nao_e(self):
        c = sequencia.cadeia_ate(15)
        self.assertFalse(sequencia.eh_keith(15))
        self.assertGreater(c[-1], 15)

    def test_os_primeiros_conhecidos(self):
        for n in (14, 19, 28, 47, 61, 75, 197, 742, 1104, 1537):
            self.assertTrue(sequencia.eh_keith(n), n)

    def test_numero_de_um_digito_nao_conta(self):
        for n in range(10):
            self.assertFalse(sequencia.eh_keith(n), n)

    def test_cada_termo_e_a_soma_dos_n_anteriores(self):
        for n in (14, 197, 742, 1537, 7385):
            c = sequencia.cadeia_ate(n)
            largura = len(str(n))
            for i in range(largura, len(c)):
                self.assertEqual(c[i], sum(c[i - largura:i]), 'n = %d, termo %d' % (n, i))

    def test_a_sequencia_comeca_com_os_digitos(self):
        for n in (14, 197, 1537, 93993):
            c = sequencia.cadeia_ate(n)
            self.assertEqual(c[:len(str(n))], sequencia.digitos_de(n))

    def test_a_sequencia_e_crescente_depois_dos_digitos(self):
        for n in (197, 742, 7385):
            c = sequencia.cadeia_ate(n)
            largura = len(str(n))
            for a, b in zip(c[largura - 1:], c[largura:]):
                self.assertLess(a, b, 'n = %d' % n)

    def test_os_dois_caminhos_concordam(self):
        for n in range(10, 3000):
            self.assertEqual(sequencia.eh_keith(n), juiz.eh_keith(n), n)

    def test_entrada_invalida_e_recusada(self):
        with self.assertRaises(ValueError):
            sequencia.digitos_de(-1)
        with self.assertRaises(ValueError):
            juiz.eh_keith(-1)
        with self.assertRaises(ValueError):
            juiz.varrer(10, 5)


if __name__ == '__main__':
    unittest.main()
