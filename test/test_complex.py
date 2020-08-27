from complex import Complex

def test_complex():
	x, y = Complex(2, 1), Complex(5, 6)
	su, sub, mul, div, mod_x, mod_y = x+y, x-y, x*y, x/y, x.mod(), y.mod()
	assert su.__str__() == '7.00+7.00i'
	assert sub.__str__() == '-3.00-5.00i'
	assert mul.__str__() == '4.00+17.00i'
	assert div.__str__() == '0.26-0.11i'
	assert mod_x.__str__() == '2.24+0.00i'
	assert mod_y.__str__() == '7.81+0.00i'






