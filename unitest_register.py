import application
import unittest

class RegisterMachineTest(unittest.TestCase):

	#Test1
	def test_product_isalpha(self):
		self.assertTrue(application.product_isalpha("Hola"))
		self.assertFalse(application.product_isalpha("1"))

	#Test2
	def test_minuscule(self):
		self.assertTrue(application.minuscule("CARRO").islower())

	#Test3
	def test_gol_card(self):
		self.assertEqual(application.gold_card(5), 0.25)

	#Test4
	def test_silver_card(self):
		self.assertEqual(application.silver_card(100), 2)

	#Test5
	def test_tax(self):
		self.assertEqual(application.tax(100, 0), 12)

	#Test6
	def test_my_total_final(self):
		self.assertEqual(application.my_total_final(100, 0, 12), 112)

if __name__ == '__main__':
    unittest.main()