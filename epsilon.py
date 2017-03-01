def hitungEpsilon(a):
  while (a + 1.0) > 1:
		a = a / 2.0
		print a
		if a + 1.0 < 1:
			break
	return a * 2
