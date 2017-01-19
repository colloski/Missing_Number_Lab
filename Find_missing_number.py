def missing_num(x, y):
	set_x = set(x)
	set_y = set(y)
	
	if (set_x) == (set_y):
		return 0
	else:
		z = set_x ^ set_y
		return (list(z)[0])
