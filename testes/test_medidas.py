# -*- coding: utf-8 -*-
"""Os numeros do README, presos. Todos sairam do medidor."""
import unittest

from ferramentas import medidor
from keith import juiz, sequencia, varredura


class TestMedidas(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.achados = varredura.ate(medidor.LIMITE)

    def test_trinta_numeros_de_keith_ate_duzentos_mil(self):
        self.assertEqual(len(self.achados), 30)
        self.assertEqual(self.achados[:7], [14, 19, 28, 47, 61, 75, 197])
        self.assertEqual(self.achados[-1], 183_186)

    def test_a_contagem_por_quantidade_de_digitos(self):
        conta = varredura.por_quantidade_de_digitos(medidor.LIMITE)
        self.assertEqual(conta, {2: 6, 3: 2, 4: 9, 5: 7, 6: 6})
        self.assertEqual(sum(conta.values()), 30)

    def test_a_densidade_cai_dez_vezes_por_digito(self):
        conta = varredura.por_quantidade_de_digitos(medidor.LIMITE)
        densidades = {d: conta[d] / (9 * 10 ** (d - 1)) for d in conta}
        self.assertAlmostEqual(densidades[2], 6.667e-02, places=5)
        self.assertAlmostEqual(densidades[6], 6.667e-06, places=9)
        # a quantidade absoluta por faixa quase nao muda, mas a faixa cresce dez vezes
        self.assertEqual(conta[2], 6)
        self.assertEqual(conta[6], 6)
        self.assertAlmostEqual(densidades[2] / densidades[6], 10_000.0, places=1)

    def test_os_passos_dos_primeiros(self):
        passos = dict(varredura.passos_dos_achados(self.achados))
        self.assertEqual(passos[14], 3)
        self.assertEqual(passos[19], 2)
        self.assertEqual(passos[197], 5)
        self.assertEqual(passos[742], 8)

    def test_decidir_um_numero_e_barato(self):
        media, quantos = varredura.custo_de_decidir(medidor.LIMITE)
        self.assertAlmostEqual(media, 14.45, places=2)
        self.assertGreater(quantos, 900)

    def test_o_custo_cresce_com_os_bits_e_nao_com_o_numero(self):
        self.assertEqual(juiz.quantos_termos_bastam(197), 11)
        self.assertEqual(juiz.quantos_termos_bastam(7_385), 17)
        self.assertEqual(juiz.quantos_termos_bastam(93_993), 22)
        self.assertEqual(juiz.quantos_termos_bastam(1_084_051), 28)
        # 1.084.051 e cinco mil vezes maior que 197 e custa menos de tres vezes mais
        self.assertLess(28 / 11, 3.0)
        self.assertGreater(1_084_051 / 197, 5000)

    def test_as_duas_conferencias(self):
        self.assertEqual(varredura.conferir_contra_juiz(medidor.LIMITE_JUIZ), 19_991)
        self.assertEqual(varredura.conferir_sequencias(self.achados), 292)

    def test_a_primeira_faixa_concentra_mais_da_metade(self):
        faixas = varredura.densidade_por_faixa(medidor.LIMITE, 7)
        self.assertEqual(faixas[0][2], 17)
        self.assertGreater(faixas[0][2], 30 / 2)
        for _, _, quantos, _ in faixas[1:]:
            self.assertLessEqual(quantos, 4)


if __name__ == '__main__':
    unittest.main()
