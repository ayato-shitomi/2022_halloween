black = "  "
yellow = "\033[43m  \033[0m"
purple = "\033[48;5;5m  \033[0m"
orange = "\033[48;5;166m  \033[0m"
red = "\033[41m  \033[0m"
white = "\033[47m  \033[0m"

pumpkin = [
	[],
	[[6, 6, black]],
	[[5, 6, black]],
	[[4, 7, black]],
	[[4, 11, black]],
	[[5, 12, black]],
	[[5, 15, black]],
	[[6, 16, black]],
	[[8, 10, black], [11, 14, yellow], [15, 17, black]],
	[[8, 10, purple], [11, 11, yellow], [12, 13, purple], [14, 14, yellow], [15, 17, purple], [23, 24, black]],
	[[7, 10, purple], [11, 14, yellow], [15, 16, purple], [17, 23, black]],
	[[6, 8, purple], [9, 22, black]],
	[[5, 20, black]],
	[[3, 10, black], [11, 19, orange]],
	[[2, 6, black], [7, 10, orange], [11, 11, red], [12, 14, orange], [15, 15, red], [16, 19, orange]],
	[[2, 3, black], [7, 10, orange], [11, 12, red], [13, 13, orange], [14, 15, red], [16, 19, orange]],
	[[7, 8, orange], [9, 9, black], [10, 19, orange]],
	[[7, 8, orange], [9, 10, black], [11, 15, orange], [16, 17, black], [18, 19, orange]],
	[[8, 9, orange], [10, 16, black], [17, 18, orange]],
	[[9, 10, orange], [11, 15, black], [16, 17, orange]],
	[[10, 16, orange]],
	[]
]

def check(number, lis):
	q = 0
	color = 0
	for i in lis:
		if (i[0] <= number and number <= i[1]):
			q = 1
			color = i[2]
	return q, color

for i in pumpkin:
	f = 1
	if i == []:
		print(white * 25)
	else:
		while f <= 25:
			q, color = check(f, i)
			if (q == 1):
				if (color == black):
					print("  ", end="")
				elif (color == yellow):
					print(yellow, end="")
				elif (color == purple):
					print(purple, end="")
				elif (color == orange):
					print(orange, end="")
				elif (color == red):
					print(red, end="")
			else:
				print(white, end="")
			f = f + 1
		print()
