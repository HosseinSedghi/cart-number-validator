# Cart Number detector (CN detector)

from bank_codes import bank_codes

test1_code = '5894631165640921'
test2_code = '6274129005473742'
test3_code = '6277603023438041'

class Detector():
	def __init__(self, number):
		self.number = number
		self.bank_code = number[:6]
		self.cart_type_code = number[6:8]
		self.serial_code = number[8:16]
		self.check_code = number[-1]

	def valid_length(self):
		if len(self.number) == 16:
			return True
		else:
			return False

	def find_bank(self):
		try:
			return bank_codes[self.bank_code]
		except KeyError:
			return False

	def is_valid_type(self):
		try:
			int(self.number)
			return True
		except ValueError:
			return False

	def is_valid(self):
		index = 1
		output = 0
		for i in self.number:
			if (index % 2) == 0:
				output += int(i)
			else:
				if (int(i) * 2) > 9:
					output += (int(i) * 2) - 9
				else:
					output += (int(i) * 2)
			index += 1

		if (output % 10) == 0:
			return True
		else:
			return False


if __name__ == "__main__":
	cart = Detector(test3_code)

	print('length : ', cart.valid_length())
	print('is integer : ', cart.is_valid_type())
	print('is valid : ', cart.is_valid())
	print('bank name : ', cart.find_bank())