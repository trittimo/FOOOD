ingredients = open('ingredients.txt', 'r')
out = open('ingredients.sql', 'w')

err_count = 0
lines = 0
cont = True
while (cont):
	try:
		line = ingredients.readline()
		if line == '':
			cont = False
			break
		out.write("INSERT INTO Ingredient VALUES ('" + line.strip() + "', 'Savory')\n")
		lines = lines + 1
	except:
		err_count = err_count + 1

ingredients.close()
out.close()

print("Errors: " + str(err_count))
print("Lines read: " + str(lines))