a = 1
b = 2
c = 3
tougle = 0

bi_a = format(a, 'b').rjust(32, '0')
bi_b = format(b, 'b').rjust(32, '0')
bi_c = format(c, 'b').rjust(32, '0')

for x in range(0, 32):
	if bi_c[x] == '0':
		if bi_a[x] == '0' and bi_b[x] == '0':
			pass
		elif bi_a[x] == '1' and bi_b[x] == '1':
			tougle += 2
		else:
			tougle += 1
	else:
		if bi_a[x] == '0' and bi_b[x] == '0':
			tougle += 1

print(tougle)