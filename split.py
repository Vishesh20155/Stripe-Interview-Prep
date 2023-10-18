input_string = "Apple, Banana; Mango-Orange"
delimiters = [",", ";", "-"]

for delimiter in delimiters:
    input_string = " ".join(input_string.split(delimiter))

result = input_string.split()
print(result)
