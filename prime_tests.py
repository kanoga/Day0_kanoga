import unittest
from prime_numbers import Prime

class PrimeTests(unittest.TestCase):
	def test_input_must_not_be_float(self):
		self.assertTrue(isPrime(10.5),"The number must be a whole number")

	def test_not_big_integer(self):
		self.assertTrue(isPrime(>1000),'The number must be less than 1000')

    def test_input_must_not_be_a _boolean(self):
		self.assertTrue(isPrime(True),"The number must not be a boolean")

	def test_input_must_be_a_number(self):
        self.assertTrue(isPrime(1),"The input must be a number only")

	def test_input_must_not_be_blank(self):
        self.assertTrue(isPrime(),"The input must not be blank")

    def test_input_must_not_be_a_list(self):
        self.assertTrue(isPrime(1,2),"The input must not be a list")

    def test_input_must_not_be_a_special_character(self):
        self.assertTrue(isPrime(*),"The input must not be a special character")

    def test_input_must_not_be_a_tuple(self):
        self.assertTrue(isPrime(1,),"The input must not be a tuple")

    def test_input_must_not_be_a_dictionary(self):
        self.assertTrue(isPrime({1:'a'}),"The input must not be a dictionary")

    def test_input_must_not_be_a_set(self):
        self.assertTrue(isPrime([1,2]),"The input must not be a set")
        

if __name__ == 'main':
	unittest.main()
