n = int(input())

iter = True
i = 1
j = n-i

while iter and i < n:
	i_str = str(i)
	j_str = str(j)
	if '0' in i_str or '0' in j_str:
		iter = True
		i += 1
		j = n-i
	else:
		iter = False

print([i, j])