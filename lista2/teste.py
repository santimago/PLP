from __future__ import print_function

for i in range(1000000):
	print("numero " + str(i / 1000000.0 * 100.0) , end='\r')
