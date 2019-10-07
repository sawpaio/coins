import unittest
from source.coins import Coins


teste1 = '2541 moeda(s) de R$ 1.00 1 moeda(s) de R$ 0.50 0 moeda(s) de R$ 0.25 0 moeda(s) de R$ 0.10 0 moeda(s) de R$ 0.05 2 moeda(s) de R$ 0.01'

teste2 = '255441 moeda(s) de R$ 1.00 1 moeda(s) de R$ 0.50 0 moeda(s) de R$ 0.25 1 moeda(s) de R$ 0.10 1 moeda(s) de R$ 0.05 0 moeda(s) de R$ 0.01'

teste3 = '0 moeda(s) de R$ 1.00 0 moeda(s) de R$ 0.50 0 moeda(s) de R$ 0.25 0 moeda(s) de R$ 0.10 0 moeda(s) de R$ 0.05 0 moeda(s) de R$ 0.01'

teste4 = '1 moeda(s) de R$ 1.00 0 moeda(s) de R$ 0.50 0 moeda(s) de R$ 0.25 0 moeda(s) de R$ 0.10 0 moeda(s) de R$ 0.05 0 moeda(s) de R$ 0.01'


class TestDistributor(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(Coins.moedas(2541.52), teste1)

    def test_case_2(self):
        self.assertEqual(Coins.moedas(255441.65), teste2)

    def test_case_3(self):
        self.assertEqual(Coins.moedas(0), teste3)  

    def test_case_4(self):
        self.assertEqual(Coins.moedas(1), teste4)
