results = []

with open("input_file.txt", "r") as f:
	for line in f:
		a, b, c = line.split()

		b = int(b)
		c = int(c)

		if a == "+":
			results.append(b + c)
		elif a == "-":
			results.append(b - c)
		elif a == "*":
			results.append(b * c)
		elif a == "//":
			results.append(b // c)
		elif a == "%":
			results.append(b % c)
		elif a == "**":
			results.append(b ** c)

last_result = results[-1]

with open("output_file.txt", "w") as file:
	for result in results:
		if result == last_result:
			file.write(str(result))
		else:
			file.write(str(result) + ', ')
