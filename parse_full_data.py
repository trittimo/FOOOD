data = open('data.txt', 'r')
export = open('export.sql', 'w')


current_title = ""
current_ingredients = []
current_instructions = []

parse_errors = 0
lines = 0

recipeID = 0

continue_parsing = True
while (continue_parsing):
    if lines % 1000 == 0:
        print("Lines: " + str(lines))
        print("Parse errors: " + str(parse_errors))
    try:
        line = data.readline()
        lines = lines + 1
        if line == '':
            continue_parsing = False
            break
        line = line.strip()
        if line[0] == '*':
            current_ingredients.append(line[1:])
        elif line[0] == '#':
            current_instructions.append(line[1:])
        else:
            if len(current_ingredients) > 0 and len(current_instructions) > 0:
                current = "INSERT INTO Recipe VALUES ( " + str(recipeID) + ", '" + current_title + "', '"

                for i in current_instructions:
                    current = current + (i + "\n")
                current = current + "', 0)"
                export.write(current + "\n")

                recipeID = recipeID + 1

            current_title = line
            current_ingredients = []
            current_instructions = []
    except:
        parse_errors = parse_errors + 1

print("Encountered " + str(parse_errors) + " parse errors")

data.close()
export.close()