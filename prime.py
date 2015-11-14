def isPrime(p):
	if p == 1:
		return False
	for n in range(2, p):
		if p % n == 0:
			return False
		n += 1
	return True
