print("Imported my_module...")

test = "Test string"

def find_index(to_search, target):
	for i, val in enumerate(to_search):
		if val == target:
			return i;

	return -1
